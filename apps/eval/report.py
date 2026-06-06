"""V2.6 Phase 4.4 — eval 결과를 사람 읽을 마크다운으로."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def render(run_json: Path) -> str:
    data = json.loads(run_json.read_text(encoding="utf-8"))

    lines = []
    lines.append(f"# Golden Q&A Eval Report")
    lines.append("")
    lines.append(f"- 시작: `{data['started_at']}`")
    lines.append(f"- 종료: `{data['finished_at']}`")
    lines.append(f"- 문항: **{data['item_count']}**")
    lines.append("")

    lines.append("## 모드별 요약")
    lines.append("")
    lines.append("| 모드 | 문항 | 평가 가능 | Hit@5 | Hit@5 율 | MRR | p50(ms) | p95(ms) |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for mode, s in data["by_mode"].items():
        lines.append(
            f"| {mode} | {s['count']} | {s['evaluable']} | "
            f"{s['hit_at_5']} | {s['hit_at_5_rate']*100:.0f}% | "
            f"{s['mrr']:.3f} | {s['latency_p50_ms']:.1f} | {s['latency_p95_ms']:.1f} |"
        )
    lines.append("")

    miss = [it for it in data["items"] if it["expected"] and not it["hit_at_5"]]
    if miss:
        lines.append("## MISS 분석")
        lines.append("")
        for it in miss:
            lines.append(f"### {it['id']} ({it['mode']})")
            lines.append(f"- 질문: `{it['question']}`")
            lines.append(f"- 기대: `{it['expected']}`")
            lines.append(f"- 반환: `{it['returned']}`")
            if it.get("error"):
                lines.append(f"- 오류: `{it['error']}`")
            lines.append("")

    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("run_json", help="run.json 경로 또는 디렉터리")
    p.add_argument("--out", default=None)
    args = p.parse_args()

    path = Path(args.run_json)
    if path.is_dir():
        path = path / "run.json"
    md = render(path)

    if args.out:
        Path(args.out).write_text(md, encoding="utf-8")
        print(f"[saved] {args.out}")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
