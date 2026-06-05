import hashlib
import os
import sqlite3
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, "..", ".."))
# Phase 0.5: storage 경로 환경변수화 (~/iris-local/storage 또는 /app/storage)
DEFAULT_STORAGE_PATH = os.path.join(PROJECT_ROOT, "storage")
STORAGE_PATH = os.environ.get("STORAGE_PATH", DEFAULT_STORAGE_PATH)
DB_DIR = os.path.join(STORAGE_PATH, "sqlite")
DB_PATH = os.path.join(DB_DIR, "wiki_history.db")

CREATE_SQL = """
CREATE TABLE IF NOT EXISTS ingest_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    raw_file TEXT NOT NULL,
    wiki_file TEXT,
    status TEXT NOT NULL,
    processed_at TEXT NOT NULL,
    checksum TEXT,
    mtime REAL,
    error_message TEXT,
    skip_reason TEXT,
    operation TEXT DEFAULT 'ingest'
);
"""


def file_checksum(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _ensure_columns(conn: sqlite3.Connection) -> None:
    cur = conn.execute("PRAGMA table_info(ingest_history)")
    cols = {row[1] for row in cur.fetchall()}
    if "skip_reason" not in cols:
        conn.execute("ALTER TABLE ingest_history ADD COLUMN skip_reason TEXT")
    if "operation" not in cols:
        conn.execute("ALTER TABLE ingest_history ADD COLUMN operation TEXT DEFAULT 'ingest'")


def init_db() -> None:
    os.makedirs(DB_DIR, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(CREATE_SQL)
        _ensure_columns(conn)
        conn.commit()


def record_ingest(
    raw_file: str,
    wiki_file: Optional[str],
    status: str,
    checksum: Optional[str],
    mtime: Optional[float],
    error_message: Optional[str] = None,
    skip_reason: Optional[str] = None,
    operation: str = "ingest",
) -> None:
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT INTO ingest_history
            (raw_file, wiki_file, status, processed_at, checksum, mtime, error_message, skip_reason, operation)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                raw_file,
                wiki_file,
                status,
                _now_iso(),
                checksum,
                mtime,
                error_message,
                skip_reason,
                operation,
            ),
        )
        conn.commit()


def get_last_record(raw_file: str) -> Optional[Dict[str, Any]]:
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.execute(
            """
            SELECT id, raw_file, wiki_file, status, processed_at, checksum, mtime, error_message, skip_reason, operation
            FROM ingest_history
            WHERE raw_file = ?
            ORDER BY id DESC
            LIMIT 1
            """,
            (raw_file,),
        )
        row = cur.fetchone()
        if row is None:
            return None
        return dict(row)


def get_last_successful_record(raw_file: str) -> Optional[Dict[str, Any]]:
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.execute(
            """
            SELECT id, raw_file, wiki_file, status, processed_at, checksum, mtime, error_message, skip_reason, operation
            FROM ingest_history
            WHERE raw_file = ? AND status = 'ok'
            ORDER BY id DESC
            LIMIT 1
            """,
            (raw_file,),
        )
        row = cur.fetchone()
        if row is None:
            return None
        return dict(row)


def unchanged_since_last_success(
    last_ok: Optional[Dict[str, Any]], checksum: str
) -> bool:
    if not last_ok or not last_ok.get("checksum"):
        return False
    return last_ok["checksum"] == checksum


def list_recent_history(limit: int = 20) -> List[Dict[str, Any]]:
    init_db()
    limit = max(1, min(limit, 500))
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.execute(
            """
            SELECT raw_file, wiki_file, status, processed_at, checksum, mtime, error_message, skip_reason, operation
            FROM ingest_history
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        )
        return [dict(row) for row in cur.fetchall()]
