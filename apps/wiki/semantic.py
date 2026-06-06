"""V2.6 Phase 5.4 — mode=semantic (FAISS + Ollama nomic-embed-text).

본 사이클은 *경계 함수만 박고 비활성*. FAISS 인덱스 구축은 별도 사이클:
  - knowledge/.nosync/_faiss/ 디렉터리 (V2.5.1 §11.2 iCloud 회피)
  - chunks를 Ollama nomic-embed-text로 임베딩 → FAISS 외부 인덱스
  - is_active() = False 인 동안 mode=auto 디스패처는 자동으로 fts 폴백

V2.5.1 §10 "Trigger B 의존성 — V2.6 K1a 가동 후" 정책과 일치.
"""
from __future__ import annotations

import os
from pathlib import Path

FAISS_DIR = Path(
    os.environ.get(
        "IRIS_FAISS_DIR",
        "/Users/iris/Documents/0Dev/iris-system/knowledge/.nosync/_faiss",
    )
)


def is_active() -> bool:
    """FAISS 인덱스 존재 + 활성 토글 시 True. 본 사이클 기본 False."""
    if os.environ.get("IRIS_SEMANTIC", "off").lower() != "on":
        return False
    return (FAISS_DIR / "index.faiss").is_file()


def query_semantic(
    text: str,
    *,
    industry: str | None = None,
    area: str | None = None,
    lane: str | None = None,
    limit: int = 20,
) -> list[dict]:
    """V2.6 Phase 5.4 활성 시: FAISS top-K → documents 메타 조인.

    본 사이클은 항상 빈 리스트. mode=auto가 자동 폴백.
    """
    if not is_active():
        return []
    # TODO: V2.6 Phase 5.4 별도 사이클
    #   1. 쿼리 임베딩 (Ollama /api/embeddings, model='nomic-embed-text')
    #   2. FAISS 검색 (top-K chunk_id)
    #   3. _index.db에서 chunk_id → doc_id → documents 메타 조인
    #   4. lane='secure' 자동 제외 (V2.6 Phase 2 secure_gate.filter_secure_rows)
    return []
