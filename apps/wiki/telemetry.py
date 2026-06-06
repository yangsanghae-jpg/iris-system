"""V2.6 Phase 5.5 — L5 Telemetry append.

V2.5 §8.1 포맷. iris-stack의 Promtail `iris-k5-telemetry` job이 본 경로를
스크랩하므로 코드는 *append만*. 임계치 평가는 Grafana(§5.6 분리 정책).

포맷 (JSON Lines):
  {
    "ts":          ISO8601 UTC,
    "endpoint":    "/api/v1/retrieval",
    "caller":      "<X-IRIS-Caller>" or "FAULT:anonymous",
    "mode":        "matrix|fts|semantic|auto",
    "industry":    str | null,
    "area":        str | null,
    "lane":        str | null,
    "query_len":   int,
    "result_count": int,
    "secure_excluded": int,
    "latency_ms":  float,
    "fallback":    bool,    -- mode=auto가 다른 모드로 폴백했는지
    "fallback_to": str | null
  }
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# storage/ symlink → ~/iris-local/storage/ (V2.5.1 §11.2)
DEFAULT_TELEMETRY_ROOT = Path(
    os.environ.get(
        "IRIS_TELEMETRY_ROOT",
        "/Users/iris/Documents/0Dev/iris-system/storage/telemetry",
    )
)
ANONYMOUS_CALLER = "FAULT:anonymous"


def _today_log(root: Path | None = None) -> Path:
    r = root or DEFAULT_TELEMETRY_ROOT
    r.mkdir(parents=True, exist_ok=True)
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return r / f"iris_k5_telemetry.{day}.log"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def normalize_caller(raw: str | None) -> str:
    """X-IRIS-Caller 헤더 정규화. 빈 값/누락 → FAULT:anonymous."""
    if not raw or not raw.strip():
        return ANONYMOUS_CALLER
    return raw.strip()


def append(
    *,
    endpoint: str,
    caller: str | None,
    mode: str,
    query_len: int,
    result_count: int,
    latency_ms: float,
    industry: str | None = None,
    area: str | None = None,
    lane: str | None = None,
    secure_excluded: int = 0,
    fallback: bool = False,
    fallback_to: str | None = None,
    extra: dict[str, Any] | None = None,
    root: Path | None = None,
) -> None:
    record: dict[str, Any] = {
        "ts": now_iso(),
        "endpoint": endpoint,
        "caller": normalize_caller(caller),
        "mode": mode,
        "industry": industry,
        "area": area,
        "lane": lane,
        "query_len": query_len,
        "result_count": result_count,
        "secure_excluded": secure_excluded,
        "latency_ms": round(latency_ms, 3),
        "fallback": fallback,
        "fallback_to": fallback_to,
    }
    if extra:
        record.update(extra)
    log = _today_log(root)
    # JSON Lines append (한 줄당 1 레코드, Loki/Promtail 표준)
    with log.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
