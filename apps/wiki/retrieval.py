import os
import re
import sqlite3
from typing import Any, Dict, List, Optional, Tuple

APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, "..", ".."))
DEFAULT_KNOWLEDGE_PATH = os.path.join(PROJECT_ROOT, "knowledge")
BASE_PATH = os.environ.get("KNOWLEDGE_BASE_PATH", DEFAULT_KNOWLEDGE_PATH)
WIKI_PATH = os.path.join(BASE_PATH, "wiki")
INDEX_DB_PATH = os.path.join(BASE_PATH, "_index.db")

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
TOKEN_RE = re.compile(r"[\w가-힣]+", re.UNICODE)

# 가중치 (최소 튜닝)
WEIGHT_TITLE_EXACT = 80.0
WEIGHT_TITLE_SUBSTRING = 25.0
WEIGHT_TITLE_TOKEN = 12.0
WEIGHT_FILENAME = 15.0
WEIGHT_BODY_PER_HIT = 1.0
WEIGHT_INCOMING_LINK = 3.0
WEIGHT_RECENCY_MAX = 4.0


def _extract_title(markdown: str, fallback: str = "") -> str:
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("#"):
            t = line.lstrip("#").strip()
            if t:
                return t
    return fallback


def _tokenize(text: str) -> List[str]:
    raw = TOKEN_RE.findall(text.lower())
    out = []
    for t in raw:
        if len(t) >= 2 or ("\uac00" <= t <= "\ud7a3"):
            out.append(t)
    return out


def _norm(s: str) -> str:
    return re.sub(r"\s+", "", s.strip().lower())


def _load_all_wiki() -> Tuple[List[str], Dict[str, str], Dict[str, str]]:
    paths: List[str] = []
    contents: Dict[str, str] = {}
    titles: Dict[str, str] = {}
    if not os.path.isdir(WIKI_PATH):
        return paths, contents, titles
    for name in sorted(os.listdir(WIKI_PATH)):
        if not name.endswith(".md"):
            continue
        full = os.path.join(WIKI_PATH, name)
        if not os.path.isfile(full):
            continue
        paths.append(full)
        text = open(full, "r", encoding="utf-8", errors="ignore").read()
        contents[name] = text
        titles[name] = _extract_title(text, fallback=name.replace(".md", ""))
    return paths, contents, titles


def _incoming_link_bonus(
    all_contents: Dict[str, str], all_titles: Dict[str, str]
) -> Dict[str, float]:
    incoming: Dict[str, float] = {name: 0.0 for name in all_contents}

    def resolve_target(target: str) -> List[str]:
        t = target.strip()
        if not t:
            return []
        hits: List[str] = []
        tl = t.lower()
        for fname, title in all_titles.items():
            stem = fname.replace(".md", "").lower()
            if tl == stem or tl in stem or stem in tl:
                hits.append(fname)
                continue
            if title and (tl in title.lower() or _norm(t) in _norm(title)):
                hits.append(fname)
        return list(dict.fromkeys(hits))

    for fname, content in all_contents.items():
        for m in WIKILINK_RE.finditer(content):
            for resolved in resolve_target(m.group(1)):
                incoming[resolved] += 1.0
    return incoming


def _score_one(
    fname: str,
    content: str,
    h1: str,
    question: str,
    q_tokens: List[str],
    incoming: float,
    mtime: float,
    mt_min: float,
    mt_max: float,
) -> float:
    base = fname
    stem = base.replace(".md", "").lower()
    text_l = content.lower()
    title_l = h1.lower()
    q_l = question.lower()

    score = 0.0

    if h1 and _norm(h1) == _norm(question):
        score += WEIGHT_TITLE_EXACT
    elif h1 and (h1.lower() in q_l or q_l in title_l):
        score += WEIGHT_TITLE_SUBSTRING

    for tok in q_tokens:
        if len(tok) < 2:
            continue
        if tok in title_l:
            score += WEIGHT_TITLE_TOKEN
        if tok in stem:
            score += WEIGHT_FILENAME
        score += text_l.count(tok) * WEIGHT_BODY_PER_HIT

    score += incoming * WEIGHT_INCOMING_LINK

    span = mt_max - mt_min
    if span > 1e-9:
        score += WEIGHT_RECENCY_MAX * (mtime - mt_min) / span
    return score


def search_wiki_candidates(question: str, top_k: int = 5) -> List[Dict[str, Any]]:
    question = (question or "").strip()
    top_k = max(1, min(top_k, 20))
    _, contents, titles = _load_all_wiki()
    if not contents:
        return []

    q_tokens = _tokenize(question)
    incoming = _incoming_link_bonus(contents, titles)

    mtimes: Dict[str, float] = {}
    for fname in contents:
        full = os.path.join(WIKI_PATH, fname)
        try:
            mtimes[fname] = os.path.getmtime(full)
        except OSError:
            mtimes[fname] = 0.0
    mt_vals = list(mtimes.values())
    mt_min = min(mt_vals) if mt_vals else 0.0
    mt_max = max(mt_vals) if mt_vals else 1.0

    ranked: List[Tuple[str, float]] = []
    for fname, text in contents.items():
        h1 = titles.get(fname, "")
        sc = _score_one(
            fname,
            text,
            h1,
            question,
            q_tokens,
            incoming.get(fname, 0.0),
            mtimes[fname],
            mt_min,
            mt_max,
        )
        ranked.append((fname, sc))

    ranked.sort(key=lambda x: (x[1], mtimes[x[0]]), reverse=True)
    out: List[Dict[str, Any]] = []
    for fname, sc in ranked[:top_k]:
        out.append({"file": fname, "score": round(float(sc), 2)})
    return out


# ─── K5 index DB queries (V2.3) ──────────────────────────────────────────────


def _open_index_db() -> Optional[sqlite3.Connection]:
    if not os.path.isfile(INDEX_DB_PATH):
        return None
    conn = sqlite3.connect(INDEX_DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def query_matrix(
    industry: Optional[str] = None,
    area: Optional[str] = None,
    level: Optional[str] = None,
    lane: Optional[str] = "reference",
    limit: int = 50,
) -> List[Dict[str, Any]]:
    """K5-① matrix exact-match query against documents."""
    conn = _open_index_db()
    if conn is None:
        return []
    try:
        where, params = [], []
        if industry is not None:
            where.append("industry = ?")
            params.append(industry)
        if area is not None:
            where.append("area = ?")
            params.append(area)
        if level is not None:
            where.append("level = ?")
            params.append(level)
        if lane is not None:
            where.append("lane = ?")
            params.append(lane)
        sql = "SELECT doc_id, path, lane, industry, area, level, title FROM documents"
        if where:
            sql += " WHERE " + " AND ".join(where)
        sql += " ORDER BY industry, area, level LIMIT ?"
        params.append(int(limit))
        rows = conn.execute(sql, params).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def query_fts(
    text: str,
    industry: Optional[str] = None,
    area: Optional[str] = None,
    lane: Optional[str] = "reference",
    limit: int = 20,
) -> List[Dict[str, Any]]:
    """K5-② FTS5 MATCH query, joined with documents metadata."""
    text = (text or "").strip()
    if not text:
        return []
    conn = _open_index_db()
    if conn is None:
        return []
    try:
        where, params = ["documents_fts MATCH ?"], [text]
        if industry is not None:
            where.append("d.industry = ?")
            params.append(industry)
        if area is not None:
            where.append("d.area = ?")
            params.append(area)
        if lane is not None:
            where.append("d.lane = ?")
            params.append(lane)
        sql = (
            "SELECT d.doc_id, d.path, d.lane, d.industry, d.area, d.level, d.title, "
            "bm25(documents_fts) AS rank "
            "FROM documents_fts JOIN documents d ON d.rowid = documents_fts.rowid "
            "WHERE " + " AND ".join(where) + " ORDER BY rank LIMIT ?"
        )
        params.append(int(limit))
        rows = conn.execute(sql, params).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()
