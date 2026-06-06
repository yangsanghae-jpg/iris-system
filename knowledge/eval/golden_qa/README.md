# Golden Q&A 평가 하네스 (V2.6 Phase 4)

## 무엇

V2.5 §10 완료 기준(정상호출 ≥ 95%, Gold ≥ 3 등)을 정량 측정하는 골든셋.
V2.5.1 §2.D "KPI가 표어가 됨" 차단 정책 구현.

## 양식

`golden_qa.jsonl` 한 줄당 1문항 (JSON Lines):

```json
{
  "id": "Q001",
  "question": "MES 관련 지표 무엇이 있나?",
  "expected_doc_ids": ["raw:nanoln-l0-l4:b7c825fe", "raw:mes:d7559bb6"],
  "expected_mode": "fts",
  "industry": null,
  "area": null,
  "notes": "본문 어디서나 'MES'와 '지표' 동시 출현 기대"
}
```

| 필드 | 의미 |
|---|---|
| `id` | `Q001` ~ `Q050` (사양 목표) — 본 사이클은 seed 8~12문항 |
| `question` | 자연어 질문 |
| `expected_doc_ids` | hit으로 기대되는 documents.doc_id 리스트 (순서 무관) |
| `expected_mode` | `matrix` / `fts` / `semantic` |
| `industry`, `area` | matrix 모드일 때 K3 키 |
| `notes` | 검증 의도 |

## 분포 목표 (사양 V2.5.1 §7 Phase 4.2)

| 모드 | 목표 | 본 사이클 |
|---|---|---|
| matrix | 20문항 | 0 (K3 분류 미부여) |
| fts | 20문항 | 8~12 (현 데이터 가능) |
| semantic | 10문항 | 0 (Phase 5.4 의존, 미가동) |

본 사이클은 fts 모드만 실측. matrix/semantic은 스키마 박고 placeholder 문항만.

## 측정 지표

- **Hit@5** — 상위 5개 결과에 expected_doc_ids 중 하나라도 포함된 비율
- **MRR** (Mean Reciprocal Rank) — 첫 expected hit의 rank 역수 평균
- **p50 / p95 응답시간** — Hit@5 계산 외 retrieval 호출 latency

## 실행

```bash
cd iris-system
make eval            # 전체 골든셋 실행, eval_runs/YYYY-MM-DD_HHmm/ 산출
make eval-baseline   # baseline 측정 (회귀 비교용)
```

## V2.5 §10 완료 기준과의 매핑

| §10 기준 | 본 평가 산출 |
|---|---|
| (a) L6-D1 K5 정상 호출 ≥ 95% | (Phase 5 K5 표준 API + Telemetry 의존) |
| (b) Gold 후보 ≥ 3건 | `apps/wiki/curate.py::trigger_a` (Phase 3에서 박힘) |
| (c) `X-IRIS-Caller` 누락률 < 1% | (Phase 5 의존) |
| (d) K5 가용성 ≥ 99% | (Phase 5 의존) |

본 평가는 *retrieval 품질 KPI* 자체를 측정 — §10의 (a)(c)(d) 의존성 제거 후 회귀 감지.
