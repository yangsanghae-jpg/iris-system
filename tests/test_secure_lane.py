"""V2.6 Phase 2.6 — Secure Lane 차단 게이트 회귀 테스트.

사양 V2.5.1 §7 Phase 2.6: 6 시나리오 (K1~K6 각 진입점에서 secure 거부).
본 사이클 구현 범위에 따라 변형:
  - K1 (raw_intake): assert_not_secure → RuntimeError
  - K1 (reference_diagnosis): 동일
  - K3 (engine merge): 본 사이클 외 (K6 ingest 미구현) → secure_intake 백도어 우회 검증
  - K4 (chunks): assert_chunk_lane → RuntimeError
  - K5 (retrieval): filter_secure_rows + X-IRIS-Secure-Excluded
  - K6 (Curate): 이미 curate.py에 박힘 (test_echo_filter.py::test_secure_lane_excluded)
"""
from __future__ import annotations

import os
import sqlite3
from pathlib import Path

import pytest

from apps.wiki.secure_gate import (
    SECURE_LANE,
    assert_not_secure,
    assert_chunk_lane,
    filter_secure_rows,
    is_gate_active,
)
from apps.ingest.secure_intake import register_secure_document


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
CREATE TABLE chunks (
    chunk_id TEXT PRIMARY KEY,
    doc_id TEXT NOT NULL REFERENCES documents(doc_id) ON DELETE CASCADE,
    ord INTEGER NOT NULL,
    text TEXT NOT NULL
);
"""


@pytest.fixture
def db(tmp_path: Path) -> sqlite3.Connection:
    p = tmp_path / "secure.db"
    conn = sqlite3.connect(p)
    conn.executescript(SCHEMA_SQL)
    return conn


@pytest.fixture(autouse=True)
def gate_on(monkeypatch):
    """기본 ON 보장 (다른 테스트가 OFF로 둔 채 끝났을 경우 대비)."""
    monkeypatch.delenv("IRIS_SECURE_GATE", raising=False)
    assert is_gate_active()


# ─── 1. K1 raw_intake 가드 ────────────────────────────────────────────────


def test_k1_assert_not_secure_blocks_secure_lane():
    with pytest.raises(RuntimeError, match="SECURE GATE/K1"):
        assert_not_secure("secure", "K1", doc_id="x")


def test_k1_assert_not_secure_allows_other_lanes():
    # bronze/silver/gold/reference → 통과
    for lane in ("bronze", "silver", "gold", "reference"):
        assert_not_secure(lane, "K1", doc_id="x")  # no raise


# ─── 2. K1 게이트 OFF 시 우회 (V2.5.1 §10 롤백 정책) ──────────────────────


def test_gate_off_disables_block(monkeypatch):
    monkeypatch.setenv("IRIS_SECURE_GATE", "off")
    assert not is_gate_active()
    # 게이트 비활성: secure 허용
    assert_not_secure("secure", "K1", doc_id="x")  # no raise


# ─── 3. secure_intake 백도어 — 명시적 secure 등록 ─────────────────────────


def test_secure_intake_registers_document(db):
    register_secure_document(db, "sec_001", "/x/sec_001", "확인 금지 보고서")
    row = db.execute("SELECT lane, title FROM documents WHERE doc_id='sec_001'").fetchone()
    assert row[0] == "secure"
    assert row[1] == "확인 금지 보고서"


def test_secure_intake_does_not_create_chunks(db):
    """secure는 chunks 비등록 (검색·임베딩 차단)."""
    register_secure_document(db, "sec_002", "/x/sec_002", "또 다른 비밀")
    n = db.execute("SELECT COUNT(*) FROM chunks WHERE doc_id='sec_002'").fetchone()[0]
    assert n == 0


# ─── 4. K4 chunk lane 가드 ────────────────────────────────────────────────


def test_k4_assert_chunk_lane_blocks_secure(db):
    register_secure_document(db, "sec_003", "/x/sec_003", "비밀")
    with pytest.raises(RuntimeError, match="SECURE GATE/K4"):
        assert_chunk_lane(db, "sec_003", stage="K4")


def test_k4_assert_chunk_lane_allows_bronze(db):
    db.execute(
        "INSERT INTO documents (doc_id, path, lane) VALUES ('b001', '/x/b001', 'bronze')"
    )
    assert_chunk_lane(db, "b001", stage="K4")  # no raise


def test_k4_assert_chunk_lane_missing_doc_noop(db):
    # 존재하지 않는 doc_id → 조용히 통과 (등록 전 호출 가능성)
    assert_chunk_lane(db, "missing", stage="K4")


# ─── 5. K5 retrieval 필터 + 카운트 ────────────────────────────────────────


def test_k5_filter_excludes_secure_rows():
    rows = [
        {"doc_id": "1", "lane": "bronze", "title": "a"},
        {"doc_id": "2", "lane": "secure", "title": "b"},
        {"doc_id": "3", "lane": "reference", "title": "c"},
        {"doc_id": "4", "lane": "secure", "title": "d"},
    ]
    kept, excluded = filter_secure_rows(rows)
    assert excluded == 2
    assert {r["doc_id"] for r in kept} == {"1", "3"}


def test_k5_filter_no_secure_returns_zero():
    rows = [{"doc_id": "1", "lane": "bronze"}, {"doc_id": "2", "lane": "gold"}]
    kept, excluded = filter_secure_rows(rows)
    assert excluded == 0
    assert kept == rows


def test_k5_filter_gate_off_passes_all(monkeypatch):
    monkeypatch.setenv("IRIS_SECURE_GATE", "off")
    rows = [{"doc_id": "1", "lane": "secure"}]
    kept, excluded = filter_secure_rows(rows)
    assert excluded == 0
    assert kept == rows


# ─── 6. K6 Curate 입력 제외 — 이미 test_echo_filter 에서 검증 ────────────
# 본 모듈에서는 중복 안 함. test_echo_filter.py::test_secure_lane_excluded 참조.
