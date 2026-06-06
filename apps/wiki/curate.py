"""K6 Curate — Trigger A/B/C로 Gold 후보 자동 식별.

V2.5 §4.6, V2.6 Phase 3 (Echo Chamber 필터).

Trigger A: 동일 (industry, area)에서 distinct doc_id ≥ 5
Trigger B: bronze 청크와 K1d 정본 텍스트 코사인 유사도 ≥ 0.80
           (Ollama nomic-embed-text 의존, V2.6 K1a 가동 후)
Trigger C: L6-D1 K5 실행 히트 (L5 Telemetry 의존, V2.6 K5 표준 API 후)

Echo Chamber 필터 (V2.6 Phase 3):
  - 모든 Trigger 입력에서 origin='ai' 제외 (자기 답변 재인용 차단)
  - origin='hybrid'는 포함 (사람 Reviewer 통과)
"""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path


@dataclass
class GoldCandidate:
    industry: str
    area: str
    distinct_docs: int
    doc_ids: list[str]    # 후보 doc_id 리스트
    source: str           # 'trigger_a' | 'trigger_b' | 'trigger_c'

    @property
    def matrix_key(self) -> str:
        return f"{self.industry}/{self.area}"


# ─── Echo Chamber 필터 (V2.6 Phase 3.2/3.3) ──────────────────────────────


def _echo_filter_clause() -> str:
    """모든 Trigger 입력의 documents WHERE 조건에 추가.
    V2.6 §2.D: 자기 답변 재인용 차단. origin='ai'만 제외, hybrid는 포함.
    """
    return "origin != 'ai'"


# ─── Trigger A — 교차 참조 임계치 ─────────────────────────────────────────


def trigger_a(
    conn: sqlite3.Connection,
    distinct_threshold: int = 5,
) -> list[GoldCandidate]:
    """동일 (industry, area)에서 distinct doc_id ≥ N → Gold 후보.

    V2.5 §4.6 Trigger A. origin='ai' 자동 제외 (V2.6 Phase 3.2).
    """
    sql = f"""
    SELECT industry, area, COUNT(DISTINCT doc_id) AS n,
           GROUP_CONCAT(DISTINCT doc_id) AS doc_ids
      FROM documents
     WHERE industry IS NOT NULL
       AND area IS NOT NULL
       AND lane != 'secure'
       AND {_echo_filter_clause()}
     GROUP BY industry, area
    HAVING n >= ?
     ORDER BY n DESC
    """
    rows = conn.execute(sql, (distinct_threshold,)).fetchall()
    out = []
    for r in rows:
        out.append(
            GoldCandidate(
                industry=r[0],
                area=r[1],
                distinct_docs=r[2],
                doc_ids=(r[3] or "").split(","),
                source="trigger_a",
            )
        )
    return out


# ─── Trigger B — 코사인 유사도 (V2.6 K1a 의존, 본 사이클 스텁) ────────────


def trigger_b(
    conn: sqlite3.Connection,
    similarity_threshold: float = 0.80,
) -> list[GoldCandidate]:
    """bronze 청크와 K1d 정본 텍스트 코사인 유사도 ≥ τ.

    V2.5 §4.6 Trigger B. Ollama nomic-embed-text 임베딩 의존.
    V2.6 K1a 비정형 파이프라인 가동 후 활성. 본 사이클은 placeholder.

    현재 카운트 = 0이 V2.5 §10에서 설계된 정상 상태.
    """
    # V2.6 K1a 가동 시 활성. 본 사이클에서는 항상 빈 리스트.
    # 임베딩 컬럼/테이블 부재 시 빈 결과 반환 (V2.5.1 §10 정상 상태).
    return []


# ─── Trigger C — L6 실행 히트 (V2.6 K5 표준 API 의존, 본 사이클 외) ──────


def trigger_c(
    conn: sqlite3.Connection,
    hit_threshold: int = 10,
) -> list[GoldCandidate]:
    """L6-D1 K5 실행 히트 ≥ N → Gold 후보.

    V2.5 §4.6 Trigger C. L5 Telemetry append + K5 표준 엔드포인트 의존.
    V2.6 Phase 5 가동 후 활성. origin 무관 (실행 히트는 사용 신호).

    본 사이클: placeholder.
    """
    return []


# ─── 통합 ───────────────────────────────────────────────────────────────


def all_gold_candidates(
    conn: sqlite3.Connection,
    *,
    a_threshold: int = 5,
    b_threshold: float = 0.80,
    c_threshold: int = 10,
) -> list[GoldCandidate]:
    """모든 Trigger 통합 + 중복 제거 (matrix_key 기준 가장 강한 신호 유지)."""
    found = trigger_a(conn, a_threshold) + trigger_b(conn, b_threshold) + trigger_c(conn, c_threshold)
    by_key: dict[str, GoldCandidate] = {}
    for c in found:
        key = c.matrix_key
        if key not in by_key or c.distinct_docs > by_key[key].distinct_docs:
            by_key[key] = c
    return list(by_key.values())


def open_db(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = None  # 위 쿼리는 인덱스 접근, dict 변환 비용 회피
    return conn
