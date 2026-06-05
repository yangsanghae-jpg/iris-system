import os
import re
from collections import defaultdict
from typing import Any, Dict, List, Set, Tuple

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")

APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, "..", ".."))
DEFAULT_KNOWLEDGE_PATH = os.path.join(PROJECT_ROOT, "knowledge")
BASE_PATH = os.environ.get("KNOWLEDGE_BASE_PATH", DEFAULT_KNOWLEDGE_PATH)
WIKI_PATH = os.path.join(BASE_PATH, "wiki")

ORPHAN_MAX_OUTGOING = 1
MIN_BODY_CHARS = 320
MIN_CONTENT_LINES = 4


def _slugify(title: str) -> str:
    title = title.strip().lower()
    title = re.sub(r"[^\w가-힣\s\-]", "", title)
    title = re.sub(r"\s+", "_", title)
    return title[:80] if title else "untitled"


def _extract_title(markdown: str, fallback: str = "untitled") -> str:
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("#"):
            t = line.lstrip("#").strip()
            if t:
                return t
    return fallback


def _read_wiki_map() -> Dict[str, str]:
    out: Dict[str, str] = {}
    if not os.path.isdir(WIKI_PATH):
        return out
    for name in os.listdir(WIKI_PATH):
        if not name.endswith(".md"):
            continue
        path = os.path.join(WIKI_PATH, name)
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                out[name] = f.read()
    return out


def _resolve_link_target(
    target: str,
    fname_to_title: Dict[str, str],
) -> str | None:
    raw = target.strip()
    if not raw:
        return None
    tl = raw.lower().rstrip(".md")
    if "/" in raw or "\\" in raw:
        base = os.path.basename(raw.replace("\\", "/"))
        if base.lower().endswith(".md") and base in fname_to_title:
            return base
        tl = base.lower().rstrip(".md")

    for fname in fname_to_title:
        stem = fname.replace(".md", "").lower()
        if tl == stem or tl.replace(" ", "_") == stem:
            return fname

    for fname, h1 in fname_to_title.items():
        if not h1:
            continue
        if raw.lower() == h1.lower():
            return fname
        if _slugify(raw) == _slugify(h1):
            return fname
    return None


def _outgoing_link_count(content: str) -> int:
    return len(WIKILINK_RE.findall(content))


def _weak_reasons(content: str, title: str) -> List[str]:
    reasons: List[str] = []
    body = content
    if "## Summary" not in content and "## 요약" not in content:
        reasons.append("missing_summary")
    if "[[" not in content:
        reasons.append("no_links")
    stripped = re.sub(r"^#.*$", "", body, flags=re.MULTILINE)
    stripped = stripped.strip()
    if len(stripped) < MIN_BODY_CHARS:
        reasons.append("too_short")
    non_empty = [ln for ln in stripped.splitlines() if ln.strip()]
    if len(non_empty) < MIN_CONTENT_LINES:
        reasons.append("thin_body")
    if not title or title == "untitled":
        reasons.append("missing_title")
    return reasons


def run_lint() -> Dict[str, Any]:
    contents = _read_wiki_map()
    wiki_count = len(contents)
    fname_to_title = {
        fn: _extract_title(text, fallback=fn.replace(".md", ""))
        for fn, text in contents.items()
    }

    broken_links: List[Dict[str, str]] = []
    incoming: Dict[str, int] = defaultdict(int)
    outgoing: Dict[str, int] = {}

    seen_broken: Set[Tuple[str, str]] = set()
    for fname, text in contents.items():
        outgoing[fname] = _outgoing_link_count(text)
        for m in WIKILINK_RE.finditer(text):
            tgt = m.group(1)
            resolved = _resolve_link_target(tgt, fname_to_title)
            if resolved is None:
                key = (fname, tgt.strip())
                if key not in seen_broken:
                    seen_broken.add(key)
                    broken_links.append({"file": fname, "link": tgt.strip()})
            else:
                incoming[resolved] += 1

    orphan_pages: List[Dict[str, str]] = []
    for fname in contents:
        inc = incoming.get(fname, 0)
        outc = outgoing.get(fname, 0)
        if inc == 0 and outc <= ORPHAN_MAX_OUTGOING:
            orphan_pages.append({"file": fname})

    title_lower: Dict[str, List[str]] = defaultdict(list)
    slug_groups: Dict[str, List[str]] = defaultdict(list)

    for fname, text in contents.items():
        t = fname_to_title[fname].strip().lower()
        title_lower[t].append(fname)
        slug_groups[_slugify(fname_to_title[fname])].append(fname)

    duplicate_candidates: List[Dict[str, Any]] = []
    seen_sets: Set[Tuple[str, ...]] = set()

    def add_dup(files: List[str], reason: str) -> None:
        key = tuple(sorted(files))
        if len(key) < 2 or key in seen_sets:
            return
        seen_sets.add(key)
        duplicate_candidates.append({"files": list(key), "reason": reason})

    for t, files in title_lower.items():
        if len(files) > 1:
            add_dup(files, "duplicate_title")

    for _slug, files in slug_groups.items():
        if len(files) > 1 and _slug and _slug != "untitled":
            add_dup(files, "similar_slug")

    weak_pages: List[Dict[str, str]] = []
    for fname, text in contents.items():
        h1 = fname_to_title[fname]
        wr = _weak_reasons(text, h1)
        if wr:
            weak_pages.append({"file": fname, "reason": ",".join(wr)})

    issue_count = (
        len(orphan_pages)
        + len(broken_links)
        + len(duplicate_candidates)
        + len(weak_pages)
    )

    n_broken = len(broken_links)
    n_dup = len(duplicate_candidates)
    n_orphan = len(orphan_pages)
    n_weak = len(weak_pages)

    if n_broken > 0:
        quality_gate = "block"
    elif issue_count > 0:
        quality_gate = "warning"
    else:
        quality_gate = "pass"

    merge_allowed = quality_gate != "block"

    policy_checks = {
        "broken_links_priority": n_broken > 0,
        "duplicate_review_needed": n_dup > 0,
        "orphan_review_needed": n_orphan > 0,
        "weak_pages_review_needed": n_weak > 0,
        "merge_allowed": merge_allowed,
    }

    return {
        "status": "ok",
        "summary": {
            "wiki_count": wiki_count,
            "issue_count": issue_count,
            "quality_gate": quality_gate,
        },
        "policy_checks": policy_checks,
        "issues": {
            "orphan_pages": orphan_pages,
            "broken_links": broken_links,
            "duplicate_candidates": duplicate_candidates,
            "weak_pages": weak_pages,
        },
    }
