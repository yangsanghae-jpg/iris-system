"""V2.6 Phase 5.3 — mode=auto 디스패처.

V2.5 §5.3 휴리스틱:
  1. industry & area & level 셋 다 지정 → matrix (메타데이터 정확 일치)
  2. industry 또는 area 1개만 지정 → fts + 메타 필터
  3. 자유 텍스트 (matrix 키 없음) → fts
  4. semantic 활성 시: 본문이 길거나 'why/how' 의미적 질문 → semantic
     (현 사이클 semantic 비활성, 항상 fts 폴백)

폴백 정책:
  - matrix 0건 → fts
  - semantic 비활성 → fts
  - 모든 모드 0건 → 빈 결과 + telemetry fallback=true 마킹
"""
from __future__ import annotations

from typing import Any

from .retrieval import query_fts, query_matrix
from .semantic import is_active as semantic_active, query_semantic


SEMANTIC_HINTS = ("왜", "어떻게", "why", "how", "비교")
SEMANTIC_MIN_LEN = 24   # 한국어 ~24자 = 의미적 질문 가능성


def _heuristic_mode(query: str, industry: str | None, area: str | None, level: str | None) -> str:
    if industry and area and level:
        return "matrix"
    q = (query or "").strip()
    if semantic_active() and (len(q) >= SEMANTIC_MIN_LEN or any(h in q for h in SEMANTIC_HINTS)):
        return "semantic"
    return "fts"


def dispatch(
    mode: str,
    query: str,
    *,
    industry: str | None = None,
    area: str | None = None,
    level: str | None = None,
    lane: str | None = None,
    limit: int = 20,
) -> tuple[list[dict], str, bool, str | None]:
    """Returns (rows, effective_mode, fallback, fallback_to)."""
    if mode == "auto":
        chosen = _heuristic_mode(query, industry, area, level)
    else:
        chosen = mode

    fallback = False
    fallback_to: str | None = None

    if chosen == "matrix":
        rows = query_matrix(industry=industry, area=area, level=level, lane=lane, limit=limit)
        if not rows:
            # matrix 0건 → fts 자동 폴백 (effective_mode='fts', fallback_to='matrix')
            rows = query_fts(query, industry=industry, area=area, lane=lane, limit=limit)
            return rows, "fts", True, "matrix"
        return rows, "matrix", False, None

    if chosen == "semantic":
        if not semantic_active():
            rows = query_fts(query, industry=industry, area=area, lane=lane, limit=limit)
            return rows, "fts", True, "semantic_inactive"
        rows = query_semantic(query, industry=industry, area=area, lane=lane, limit=limit)
        if not rows:
            rows = query_fts(query, industry=industry, area=area, lane=lane, limit=limit)
            return rows, "fts", True, "semantic"
        return rows, "semantic", False, None

    # default fts
    rows = query_fts(query, industry=industry, area=area, lane=lane, limit=limit)
    return rows, "fts", False, None
