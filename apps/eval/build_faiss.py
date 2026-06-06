"""V2.6 Phase 5.4 — FAISS 인덱스 빌드.

chunks 테이블의 모든 텍스트를 Ollama nomic-embed-text로 임베딩 →
FAISS IndexFlatIP (정규화된 내적 = cosine 유사도) + meta(chunk_id) 저장.

저장 위치 (V2.5.1 §11.2 iCloud 회피):
  knowledge/.nosync/_faiss/index.faiss
  knowledge/.nosync/_faiss/meta.npy

  secure lane 문서는 chunks 비등록이라 자동 격리.
"""
from __future__ import annotations

import sqlite3
import sys
import time
from pathlib import Path

import faiss
import numpy as np

REPO_ROOT = Path("/Users/iris/Documents/0Dev")
IRIS_ROOT = REPO_ROOT / "iris-system"
DB_PATH = IRIS_ROOT / "knowledge" / "_index.db"
FAISS_DIR = IRIS_ROOT / "knowledge" / ".nosync" / "_faiss"

sys.path.insert(0, str(IRIS_ROOT))

from apps.wiki.embed import EMBED_DIM, embed_batch


def build() -> dict:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            "SELECT chunk_id, text FROM chunks ORDER BY chunk_id"
        ).fetchall()
    finally:
        conn.close()

    if not rows:
        print("[WARN] chunks 0건. ingest 먼저 실행.")
        return {"chunks": 0}

    chunk_ids = [r["chunk_id"] for r in rows]
    texts = [r["text"] for r in rows]

    print(f"[Phase 5.4] chunks {len(rows)}건 임베딩 시작 (nomic-embed-text 768-dim)…")
    t0 = time.perf_counter()
    vectors = embed_batch(texts)
    elapsed = time.perf_counter() - t0
    print(f"  embedded in {elapsed:.1f}s ({len(rows)/elapsed:.1f} chunks/s)")

    arr = np.array(vectors, dtype="float32")
    # 정규화 → IndexFlatIP가 cosine 유사도와 동치
    faiss.normalize_L2(arr)

    index = faiss.IndexFlatIP(EMBED_DIM)
    index.add(arr)

    FAISS_DIR.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(FAISS_DIR / "index.faiss"))
    np.save(FAISS_DIR / "meta.npy", np.array(chunk_ids))

    print(f"[DONE] FAISS index → {FAISS_DIR}/index.faiss ({index.ntotal} vectors)")
    return {"chunks": len(rows), "elapsed_s": elapsed, "ntotal": index.ntotal}


if __name__ == "__main__":
    build()
