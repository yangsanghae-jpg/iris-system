"""V2.6 Phase 5.4 — mode=semantic (FAISS + Ollama nomic-embed-text).

활성:
  IRIS_SEMANTIC=on AND knowledge/.nosync/_faiss/index.faiss 존재

인덱스 구조:
  knowledge/.nosync/_faiss/index.faiss  — FAISS IndexFlatIP (내적 = cosine 유사도, 정규화 가정)
  knowledge/.nosync/_faiss/meta.npy     — chunk_id 배열 (FAISS rowid 순서 동일)

V2.5.1 §11.2 iCloud 회피 — .nosync/ 디렉터리 사용.
"""
from __future__ import annotations

import os
from pathlib import Path

import numpy as np

FAISS_DIR = Path(
    os.environ.get(
        "IRIS_FAISS_DIR",
        "/Users/iris/Documents/0Dev/iris-system/knowledge/.nosync/_faiss",
    )
)
INDEX_PATH = FAISS_DIR / "index.faiss"
META_PATH = FAISS_DIR / "meta.npy"


def is_active() -> bool:
    if os.environ.get("IRIS_SEMANTIC", "off").lower() != "on":
        return False
    return INDEX_PATH.is_file() and META_PATH.is_file()


def _load_index_and_meta():
    import faiss
    index = faiss.read_index(str(INDEX_PATH))
    meta = np.load(META_PATH, allow_pickle=True)
    return index, meta


def query_semantic(
    text: str,
    *,
    industry: str | None = None,
    area: str | None = None,
    lane: str | None = None,
    limit: int = 20,
) -> list[dict]:
    """V2.6 Phase 5.4: FAISS 검색 → chunk_id → documents 메타 조인.

    secure는 chunks 비등록이라 FAISS 인덱스에 *애초에 없음* (자동 격리).
    추가 lane='secure' 필터는 secure_gate.filter_secure_rows에서 안전망.
    """
    if not is_active() or not (text or "").strip():
        return []
    import faiss  # noqa: F401
    import sqlite3
    from .embed import embed

    index, meta = _load_index_and_meta()
    q = np.array([embed(text)], dtype="float32")
    # cosine = L2-normalized inner product. 임베딩이 정규화되지 않았을 수 있으니 normalize_L2 강제.
    faiss.normalize_L2(q)

    k = min(limit * 4, len(meta))  # 동일 doc_id 중복 제거 위해 over-fetch
    if k <= 0:
        return []
    scores, ids = index.search(q, k)
    chunk_ids = [str(meta[int(i)]) for i in ids[0] if 0 <= i < len(meta)]
    score_by_chunk = {str(meta[int(i)]): float(scores[0][j]) for j, i in enumerate(ids[0]) if 0 <= i < len(meta)}

    if not chunk_ids:
        return []

    # chunk_id → doc_id → documents 메타
    db_path = Path("/Users/iris/Documents/0Dev/iris-system/knowledge/_index.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        placeholders = ",".join("?" * len(chunk_ids))
        rows = conn.execute(
            f"""
            SELECT c.chunk_id, c.doc_id, d.path, d.lane, d.industry, d.area, d.level, d.title
              FROM chunks c
              JOIN documents d ON d.doc_id = c.doc_id
             WHERE c.chunk_id IN ({placeholders})
            """,
            chunk_ids,
        ).fetchall()
    finally:
        conn.close()

    # 후처리: 메타 필터 + lane='secure' 자동 제외 + doc_id 중복 제거 + 점수순
    by_doc: dict[str, dict] = {}
    for r in rows:
        d = dict(r)
        d["rank"] = -score_by_chunk.get(d["chunk_id"], 0.0)  # FTS와 부호 통일 (낮을수록 좋음)
        if industry and d["industry"] != industry:
            continue
        if area and d["area"] != area:
            continue
        if lane and d["lane"] != lane:
            continue
        if d["lane"] == "secure":
            continue
        did = d["doc_id"]
        if did not in by_doc or d["rank"] < by_doc[did]["rank"]:
            by_doc[did] = d
    out = sorted(by_doc.values(), key=lambda x: x["rank"])[:limit]
    # chunk_id는 응답에서 제거 (caller는 doc_id 단위)
    for d in out:
        d.pop("chunk_id", None)
    return out
