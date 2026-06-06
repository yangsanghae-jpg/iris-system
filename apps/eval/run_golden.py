"""V2.6 Phase 4.3 — Golden Q&A 평가 러너.

골든셋 JSONL → retrieval 직접 호출 → Hit@5 / MRR / latency 측정.

본 사이클 범위:
  - fts 모드만 실측 (matrix/semantic은 placeholder, 0 hit이 기대값)
  - retrieval.query_fts(lane=None) 호출로 lane 무관 검색
  - Phase 5 K5 표준 엔드포인트 가동 시 HTTP 호출 모드로 전환 예정
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

REPO_ROOT = Path("/Users/iris/Documents/0Dev")
IRIS_ROOT = REPO_ROOT / "iris-system"
DEFAULT_GOLDEN = IRIS_ROOT / "knowledge" / "eval" / "golden_qa" / "golden_qa.jsonl"

# retrieval 모듈은 iris-system/apps/wiki/ 안
sys.path.insert(0, str(IRIS_ROOT))


@dataclass
class GoldenItem:
    id: str
    question: str
    expected_doc_ids: list[str]
    expected_mode: str          # fts | matrix | semantic
    industry: str | None = None
    area: str | None = None
    level: str | None = None
    notes: str = ""


@dataclass
class ItemResult:
    id: str
    mode: str
    question: str
    expected: list[str]
    returned: list[str]
    hit_at_5: bool
    reciprocal_rank: float       # 0.0 if no hit
    latency_ms: float
    error: str | None = None


@dataclass
class RunSummary:
    started_at: str
    finished_at: str
    item_count: int
    by_mode: dict[str, dict[str, float]] = field(default_factory=dict)
    items: list[ItemResult] = field(default_factory=list)


def now_iso() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_golden(path: Path) -> list[GoldenItem]:
    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        d = json.loads(line)
        items.append(GoldenItem(**d))
    return items


def run_item(item: GoldenItem, top_k: int = 5) -> ItemResult:
    from apps.wiki.retrieval import query_fts, query_matrix

    t0 = time.perf_counter()
    err = None
    returned: list[str] = []

    try:
        if item.expected_mode == "fts":
            rows = query_fts(item.question, lane=None, limit=top_k)
            returned = [r["doc_id"] for r in rows]
        elif item.expected_mode == "matrix":
            rows = query_matrix(
                industry=item.industry,
                area=item.area,
                level=item.level,
                lane=None,
                limit=top_k,
            )
            returned = [r["doc_id"] for r in rows]
        elif item.expected_mode == "semantic":
            # V2.6 Phase 5.4 의존 — placeholder
            returned = []
        else:
            err = f"unknown mode: {item.expected_mode}"
    except Exception as e:
        err = f"{type(e).__name__}: {e}"

    latency_ms = (time.perf_counter() - t0) * 1000.0

    expected_set = set(item.expected_doc_ids)
    hit_at_5 = bool(expected_set.intersection(returned[:top_k]))
    rr = 0.0
    for i, did in enumerate(returned[:top_k], start=1):
        if did in expected_set:
            rr = 1.0 / i
            break

    return ItemResult(
        id=item.id,
        mode=item.expected_mode,
        question=item.question,
        expected=item.expected_doc_ids,
        returned=returned,
        hit_at_5=hit_at_5,
        reciprocal_rank=rr,
        latency_ms=latency_ms,
        error=err,
    )


def _percentile(values: list[float], p: float) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    idx = int(round((len(s) - 1) * p))
    return s[idx]


def aggregate(items: list[ItemResult]) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    by_mode: dict[str, list[ItemResult]] = {}
    for it in items:
        by_mode.setdefault(it.mode, []).append(it)

    for mode, lst in by_mode.items():
        evaluable = [r for r in lst if r.expected]   # expected=[] (placeholder) 제외
        n = len(lst)
        n_eval = len(evaluable)
        n_hit = sum(1 for r in evaluable if r.hit_at_5)
        mrr = sum(r.reciprocal_rank for r in evaluable) / n_eval if n_eval else 0.0
        latencies = [r.latency_ms for r in lst if r.error is None]
        out[mode] = {
            "count": n,
            "evaluable": n_eval,
            "hit_at_5": n_hit,
            "hit_at_5_rate": (n_hit / n_eval) if n_eval else 0.0,
            "mrr": mrr,
            "latency_p50_ms": _percentile(latencies, 0.50),
            "latency_p95_ms": _percentile(latencies, 0.95),
        }
    return out


def run(golden_path: Path, top_k: int = 5) -> RunSummary:
    items = load_golden(golden_path)
    started = now_iso()
    results = [run_item(it, top_k=top_k) for it in items]
    finished = now_iso()
    return RunSummary(
        started_at=started,
        finished_at=finished,
        item_count=len(items),
        by_mode=aggregate(results),
        items=results,
    )


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--golden", default=str(DEFAULT_GOLDEN))
    p.add_argument("--top-k", type=int, default=5)
    p.add_argument("--out", default=None, help="결과 JSON 저장 경로")
    p.add_argument("--quiet", action="store_true")
    args = p.parse_args()

    summary = run(Path(args.golden), top_k=args.top_k)

    if not args.quiet:
        print(f"[Golden Q&A baseline] {summary.item_count} items")
        for mode, stats in summary.by_mode.items():
            print(f"  {mode:9s}  hit@5={stats['hit_at_5']}/{stats['evaluable']} "
                  f"({stats['hit_at_5_rate']*100:.0f}%)  MRR={stats['mrr']:.3f}  "
                  f"p50={stats['latency_p50_ms']:.1f}ms p95={stats['latency_p95_ms']:.1f}ms")
        miss = [it for it in summary.items if it.expected and not it.hit_at_5]
        if miss:
            print(f"\n[MISS] {len(miss)}건:")
            for it in miss:
                print(f"  {it.id} ({it.mode}) q='{it.question[:30]}' returned={it.returned[:3]}")

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        # asdict는 ItemResult list까지 변환
        Path(args.out).write_text(
            json.dumps(asdict(summary), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        if not args.quiet:
            print(f"\n[saved] {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
