"""V2.6 Phase 3.5 — K6 Echo Chamber 필터 회귀 테스트.

사양 V2.5.1 §7 Phase 3.5:
  Trigger A에 ai 문서 10개 vs human 문서 4개 → human만 Gold 후보
  즉 ai 10개가 카운트에서 제외되어 4개로 Trigger A 임계치(5) 미달
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from apps.wiki.curate import trigger_a


SCHEMA_SQL = """
CREATE TABLE documents (
    doc_id TEXT PRIMARY KEY,
    path TEXT NOT NULL,
    lane TEXT NOT NULL,
    trust TEXT NOT NULL DEFAULT 'verified',
    industry TEXT,
    area TEXT,
    level TEXT,
    title TEXT,
    source_url TEXT,
    fetched_at TEXT,
    promoted_to TEXT,
    kind TEXT,
    origin TEXT NOT NULL DEFAULT 'human'
);
"""


def _make_db(tmp_path: Path) -> sqlite3.Connection:
    db = tmp_path / "echo.db"
    conn = sqlite3.connect(db)
    conn.executescript(SCHEMA_SQL)
    return conn


def _insert(conn, doc_id: str, industry: str, area: str, origin: str, lane: str = "bronze") -> None:
    conn.execute(
        "INSERT INTO documents (doc_id, path, lane, industry, area, kind, origin) "
        "VALUES (?, ?, ?, ?, ?, 'source', ?)",
        (doc_id, f"/x/{doc_id}", lane, industry, area, origin),
    )


def test_echo_filter_blocks_ai_only_cluster(tmp_path):
    """ai 10개만 있는 군집은 Gold 후보가 되면 안 됨."""
    conn = _make_db(tmp_path)
    for i in range(10):
        _insert(conn, f"ai_{i}", industry="B", area="planning", origin="ai")
    conn.commit()

    candidates = trigger_a(conn, distinct_threshold=5)
    assert candidates == [], "ai-only 군집이 Gold 후보로 올라옴 (Echo Chamber)"


def test_echo_filter_keeps_human_cluster(tmp_path):
    """human 7개는 Gold 후보가 되어야 함."""
    conn = _make_db(tmp_path)
    for i in range(7):
        _insert(conn, f"h_{i}", industry="B", area="planning", origin="human")
    conn.commit()

    candidates = trigger_a(conn, distinct_threshold=5)
    assert len(candidates) == 1
    assert candidates[0].matrix_key == "B/planning"
    assert candidates[0].distinct_docs == 7


def test_echo_filter_mixed_ai_dominates_human_under_threshold(tmp_path):
    """사양 §7 Phase 3.5: ai 10 + human 4 → human 4만 카운트, 임계치 5 미달.

    Echo 필터가 작동하지 않으면 (ai+human=14) → Gold 후보로 올라가는 게 보임.
    """
    conn = _make_db(tmp_path)
    for i in range(10):
        _insert(conn, f"ai_{i}", industry="B", area="planning", origin="ai")
    for i in range(4):
        _insert(conn, f"h_{i}", industry="B", area="planning", origin="human")
    conn.commit()

    candidates = trigger_a(conn, distinct_threshold=5)
    assert candidates == [], "ai+human 혼합 군집에서 ai가 카운트에 포함됨 (필터 실패)"


def test_echo_filter_hybrid_counts(tmp_path):
    """origin='hybrid' (사람 Reviewer 통과)는 Gold 카운트에 포함되어야 함."""
    conn = _make_db(tmp_path)
    for i in range(3):
        _insert(conn, f"hu_{i}", industry="B", area="planning", origin="human")
    for i in range(2):
        _insert(conn, f"hy_{i}", industry="B", area="planning", origin="hybrid")
    conn.commit()

    candidates = trigger_a(conn, distinct_threshold=5)
    assert len(candidates) == 1
    assert candidates[0].distinct_docs == 5
    # hybrid + human 합쳐서 5개 → 통과


def test_secure_lane_excluded(tmp_path):
    """V2.6 Phase 2 의존: lane='secure'는 Trigger 입력에서 제외 (사양 §2.A).

    Phase 2 미가동 상태에서도 curate.py가 lane!='secure' 조건을 박아두는지 확인.
    """
    conn = _make_db(tmp_path)
    for i in range(7):
        _insert(conn, f"s_{i}", industry="B", area="planning", origin="human", lane="secure")
    conn.commit()

    candidates = trigger_a(conn, distinct_threshold=5)
    assert candidates == [], "secure lane 문서가 Trigger 입력에 들어옴 (Phase 2 대비 누락)"


def test_null_industry_excluded(tmp_path):
    """industry/area가 NULL인 행은 Trigger A 그룹화에서 제외."""
    conn = _make_db(tmp_path)
    for i in range(7):
        _insert(conn, f"n_{i}", industry=None, area=None, origin="human")
    conn.commit()

    candidates = trigger_a(conn, distinct_threshold=5)
    assert candidates == [], "NULL industry 행이 Trigger A 후보로 올라옴"
