# 세부 산업 공정 분석 — 원본 데이터 + 보완 작업표

> 데이터 출처 (자동 추출, 2026-06-05):
> - 라벨/공정 흐름 요약: `server/data/step3/industry_scale_model_v1.json`
> - 라우팅/MVP/모듈/KPI/방향성: `server/data/ch1/industry_packs/IND_*.json` (`sub_profiles[slug]`)
> - slug/desc 보조: `server/data/ch1/sub_industry_meta.json`

**목적**: 49개 세부 산업의 raw 데이터를 한눈에 보고, 사용자가 직접 보완(상세 공정 + 핵심 관리점)할 수 있게 작업표 제공.

**보완 가이드** (각 sub_industry 의 두 빈 섹션):
- **공정 상세 (보완 필요)**: 현재 흐름이 3~5단계로 너무 거침. 8~15단계로 풀고, 각 단계에 짧은 설명(노광/식각 공정명, 설비, 핵심 파라미터 등).
- **핵심 관리점 (보완 필요)**: 결과 KPI(수율·OEE)가 아니라 "현장에서 매일 봐야 하는 것". 5~8개 항목. 예: "포토 마스크 정렬 오차 ≤5nm", "챔버 가스 변경 이력 lot 단위 기록".

**진행 방식 예시**: 한 sub 의 두 섹션을 채워 주시면 동일 포맷으로 다음 sub 채우기. 1산업 전체 완성되면 데이터/UI 반영.

---

# A. 프로젝트형 제조 / 项目型制造

세부 산업 수: **8**


## A-1. 플랜트 EPC / 工厂 EPC / Plant EPC
`slug = plant_epc`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 기본 설계 → 상세 설계 → 자재 조달 → 현장 시공 → 시운전 |
| 공정 흐름 (zh) | 基本设计 → 详细设计 → 物料采购 → 现场施工 → 试运行 |
| 공정 흐름 (en) | Basic design → Detail design → Procurement → Construction → Commissioning |
| 라우팅 | `RT_PROJECT` — 프로젝트형 (Project) — 1건당 계획·자원·납기 관리. 사이트/EPC 성격. |
| MVP 기능 (raw) | `MVP_ORDER_TRACK`, `MVP_PROJECT_VIS`, `MVP_RESOURCE_PLAN`, `MVP_MATERIAL_SYNC`, `MVP_PROGRESS_MON` |
| 핵심 모듈 (raw) | `MOD_PROJECT_PLAN`, `MOD_RESOURCE`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_PROJECT_PROGRESS`, `KPI_DELIVERY`, `KPI_COST`, `KPI_RESOURCE_UTIL` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `DELIVERY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## A-2. 중공업 장비 / 重工业装备 / Heavy Industrial Equipment
`slug = heavy_equipment`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 단조·주조 → 정밀가공 → 조립 → 시험·시운전 |
| 공정 흐름 (zh) | 锻造·铸造 → 精密加工 → 装配 → 试验·试运行 |
| 공정 흐름 (en) | Forging/Casting → Precision machining → Assembly → Test & commissioning |
| 라우팅 | `RT_PROJECT` — 프로젝트형 (Project) — 1건당 계획·자원·납기 관리. 사이트/EPC 성격. |
| MVP 기능 (raw) | `MVP_ORDER_TRACK`, `MVP_PROJECT_VIS`, `MVP_RESOURCE_PLAN`, `MVP_MATERIAL_SYNC`, `MVP_PROGRESS_MON` |
| 핵심 모듈 (raw) | `MOD_PROJECT_PLAN`, `MOD_RESOURCE`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_PROJECT_PROGRESS`, `KPI_DELIVERY`, `KPI_COST`, `KPI_RESOURCE_UTIL` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `DELIVERY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## A-3. 반도체 장비 / 半导体装备 / Semiconductor Equipment
`slug = semi_equipment`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 장비 설계 → 정밀 부품 가공 → 모듈 조립 → 클린룸 시험·출하 |
| 공정 흐름 (zh) | 装备设计 → 精密零件加工 → 模组装配 → 洁净室测试·出货 |
| 공정 흐름 (en) | Design → Precision parts → Module assembly → Cleanroom test → Ship |
| 라우팅 | `RT_PROJECT` — 프로젝트형 (Project) — 1건당 계획·자원·납기 관리. 사이트/EPC 성격. |
| MVP 기능 (raw) | `MVP_ORDER_TRACK`, `MVP_PROJECT_VIS`, `MVP_RESOURCE_PLAN`, `MVP_MATERIAL_SYNC`, `MVP_PROGRESS_MON` |
| 핵심 모듈 (raw) | `MOD_PROJECT_PLAN`, `MOD_RESOURCE`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_PROJECT_PROGRESS`, `KPI_DELIVERY`, `KPI_COST`, `KPI_RESOURCE_UTIL` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `DELIVERY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## A-4. 디스플레이 장비 / 显示装备 / Display Equipment
`slug = display_equipment`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 프레임 가공 → 광학·전자 부품 조립 → 정합·캘리브레이션 |
| 공정 흐름 (zh) | 框架加工 → 光学·电子部件装配 → 校准 |
| 공정 흐름 (en) | Frame machining → Optical/electronic assembly → Calibration |
| 라우팅 | `RT_PROJECT` — 프로젝트형 (Project) — 1건당 계획·자원·납기 관리. 사이트/EPC 성격. |
| MVP 기능 (raw) | `MVP_ORDER_TRACK`, `MVP_PROJECT_VIS`, `MVP_RESOURCE_PLAN`, `MVP_MATERIAL_SYNC`, `MVP_PROGRESS_MON` |
| 핵심 모듈 (raw) | `MOD_PROJECT_PLAN`, `MOD_RESOURCE`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_PROJECT_PROGRESS`, `KPI_DELIVERY`, `KPI_COST`, `KPI_RESOURCE_UTIL` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `DELIVERY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## A-5. 배터리 장비 / 电池装备 / Battery Equipment
`slug = battery_equipment`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 정밀가공 → 클린룸 조립 → 안전 시험·인증 |
| 공정 흐름 (zh) | 精密加工 → 洁净室装配 → 安全测试·认证 |
| 공정 흐름 (en) | Precision machining → Cleanroom assembly → Safety test & cert |
| 라우팅 | `RT_PROJECT` — 프로젝트형 (Project) — 1건당 계획·자원·납기 관리. 사이트/EPC 성격. |
| MVP 기능 (raw) | `MVP_ORDER_TRACK`, `MVP_PROJECT_VIS`, `MVP_RESOURCE_PLAN`, `MVP_MATERIAL_SYNC`, `MVP_PROGRESS_MON`, `MVP_LINE_VIS` |
| 핵심 모듈 (raw) | `MOD_PROJECT_PLAN`, `MOD_RESOURCE`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL`, `MOD_BATCH_CTRL` |
| KPI 키워드 (raw) | `KPI_PROJECT_PROGRESS`, `KPI_DELIVERY`, `KPI_COST`, `KPI_RESOURCE_UTIL`, `KPI_YIELD` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `DELIVERY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## A-6. 항공·우주 장비 / 航空航天装备 / Aerospace Equipment
`slug = aerospace_equipment`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 정밀가공 → 조립 → 비파괴검사 → 인증 시험 |
| 공정 흐름 (zh) | 精密加工 → 装配 → 无损检测 → 认证试验 |
| 공정 흐름 (en) | Precision machining → Assembly → NDT → Cert test |
| 라우팅 | `RT_PROJECT` — 프로젝트형 (Project) — 1건당 계획·자원·납기 관리. 사이트/EPC 성격. |
| MVP 기능 (raw) | `MVP_ORDER_TRACK`, `MVP_PROJECT_VIS`, `MVP_RESOURCE_PLAN`, `MVP_MATERIAL_SYNC`, `MVP_PROGRESS_MON` |
| 핵심 모듈 (raw) | `MOD_PROJECT_PLAN`, `MOD_RESOURCE`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_PROJECT_PROGRESS`, `KPI_DELIVERY`, `KPI_COST`, `KPI_RESOURCE_UTIL` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `DELIVERY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## A-7. 조선 / 船舶制造 / Shipbuilding
`slug = shipbuilding`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 강재 절단 → 블록 조립 → 도장 → 진수·시운전 |
| 공정 흐름 (zh) | 钢材切割 → 分段装配 → 涂装 → 下水·试运行 |
| 공정 흐름 (en) | Steel cut → Block assembly → Painting → Launch & commissioning |
| 라우팅 | `RT_PROJECT` — 프로젝트형 (Project) — 1건당 계획·자원·납기 관리. 사이트/EPC 성격. |
| MVP 기능 (raw) | `MVP_ORDER_TRACK`, `MVP_PROJECT_VIS`, `MVP_RESOURCE_PLAN`, `MVP_MATERIAL_SYNC`, `MVP_PROGRESS_MON` |
| 핵심 모듈 (raw) | `MOD_PROJECT_PLAN`, `MOD_RESOURCE`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_PROJECT_PROGRESS`, `KPI_DELIVERY`, `KPI_COST`, `KPI_RESOURCE_UTIL` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `DELIVERY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## A-8. 특수 구조물 제조 / 特殊结构制造 / Special Structural Mfg.
`slug = special_structural`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 철근·강재 가공 → 용접·조립 → 시공 시험 |
| 공정 흐름 (zh) | 钢筋·钢材加工 → 焊接·装配 → 施工试验 |
| 공정 흐름 (en) | Rebar/steel cut → Welding & assembly → Construction test |
| 라우팅 | `RT_PROJECT` — 프로젝트형 (Project) — 1건당 계획·자원·납기 관리. 사이트/EPC 성격. |
| MVP 기능 (raw) | `MVP_ORDER_TRACK`, `MVP_PROJECT_VIS`, `MVP_RESOURCE_PLAN`, `MVP_MATERIAL_SYNC`, `MVP_PROGRESS_MON` |
| 핵심 모듈 (raw) | `MOD_PROJECT_PLAN`, `MOD_RESOURCE`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_PROJECT_PROGRESS`, `KPI_DELIVERY`, `KPI_COST`, `KPI_RESOURCE_UTIL` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `DELIVERY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

# B. 반도체 제조 / 半导体制造

세부 산업 수: **8**


## B-1. 로직/파운드리 / 逻辑/代工 / Logic / Foundry
`slug = logic_foundry`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 포토 → 식각 → 박막 증착 → CMP → 이온주입 (재진입) |
| 공정 흐름 (zh) | 光刻 → 刻蚀 → 薄膜沉积 → CMP → 离子注入 (再进入) |
| 공정 흐름 (en) | Photo → Etch → Deposition → CMP → Implant (re-entrant) |
| 라우팅 | `RT_REENTRANT` — 재진입형 (Reentrant) — 동일 공정/설비를 여러 번 다시 통과. 디스패칭 룰이 사이클 타임 결정. |
| MVP 기능 (raw) | `MVP_LOT_TRACK`, `MVP_WIP_VIS`, `MVP_RULE_DISPATCH`, `MVP_RECIPE_CTRL`, `MVP_YIELD_MON`, `MVP_ALARM_CLOSED_LOOP` |
| 핵심 모듈 (raw) | `MOD_PC`, `MOD_DISPATCH`, `MOD_APC_BASIC`, `MOD_VISUAL`, `MOD_RULE`, `MOD_YIELD` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_CYCLE_TIME`, `KPI_WIP_TURN`, `KPI_DISPATCH_STABILITY` |
| 시스템 방향성 (raw) | `DISPATCH`, `WIP`, `CT` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## B-2. 메모리 (DRAM/NAND) / 存储 (DRAM/NAND) / Memory (DRAM/NAND)
`slug = memory_dram_nand`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 셀 어레이 → 주변회로 → 다층 적층 (3D NAND) → KGD 어셈블리 |
| 공정 흐름 (zh) | 存储阵列 → 周边电路 → 多层堆叠 (3D NAND) → KGD 装配 |
| 공정 흐름 (en) | Cell array → Periphery → 3D stacking (NAND) → KGD assembly |
| 라우팅 | `RT_REENTRANT` — 재진입형 (Reentrant) — 동일 공정/설비를 여러 번 다시 통과. 디스패칭 룰이 사이클 타임 결정. |
| MVP 기능 (raw) | `MVP_LOT_TRACK`, `MVP_WIP_VIS`, `MVP_RULE_DISPATCH`, `MVP_RECIPE_CTRL`, `MVP_YIELD_MON`, `MVP_ALARM_CLOSED_LOOP` |
| 핵심 모듈 (raw) | `MOD_PC`, `MOD_DISPATCH`, `MOD_APC_BASIC`, `MOD_VISUAL`, `MOD_RULE`, `MOD_YIELD` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_CYCLE_TIME`, `KPI_WIP_TURN`, `KPI_DISPATCH_STABILITY` |
| 시스템 방향성 (raw) | `DISPATCH`, `WIP`, `CT` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## B-3. 아날로그/혼성신호 / 模拟/混合信号 / Analog / Mixed Signal
`slug = analog_mixed`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 웨이퍼 가공 → 트림·캘리브레이션 → 패키지 → 테스트 |
| 공정 흐름 (zh) | 晶圆加工 → 修调·校准 → 封装 → 测试 |
| 공정 흐름 (en) | Wafer fab → Trim/calibration → Package → Test |
| 라우팅 | `RT_REENTRANT` — 재진입형 (Reentrant) — 동일 공정/설비를 여러 번 다시 통과. 디스패칭 룰이 사이클 타임 결정. |
| MVP 기능 (raw) | `MVP_LOT_TRACK`, `MVP_WIP_VIS`, `MVP_RULE_DISPATCH`, `MVP_RECIPE_CTRL`, `MVP_YIELD_MON`, `MVP_ALARM_CLOSED_LOOP`, `MVP_PROCESS_MON` |
| 핵심 모듈 (raw) | `MOD_PC`, `MOD_DISPATCH`, `MOD_APC_BASIC`, `MOD_VISUAL`, `MOD_RULE`, `MOD_YIELD`, `MOD_PROCESS_MON` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_CYCLE_TIME`, `KPI_WIP_TURN`, `KPI_DISPATCH_STABILITY` |
| 시스템 방향성 (raw) | `DISPATCH`, `WIP`, `CT` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## B-4. 전력/디스크리트 / 功率/分立 / Power / Discrete
`slug = power_discrete`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 에피택시 → 단위 소자 가공 → 패키지 → 번인 |
| 공정 흐름 (zh) | 外延 → 单元器件加工 → 封装 → 老化 |
| 공정 흐름 (en) | Epi → Device fab → Package → Burn-in |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_LOT_TRACK`, `MVP_WIP_VIS`, `MVP_RULE_DISPATCH`, `MVP_RECIPE_CTRL`, `MVP_YIELD_MON`, `MVP_ALARM_CLOSED_LOOP`, `MVP_BATCH_TRACE` |
| 핵심 모듈 (raw) | `MOD_PC`, `MOD_DISPATCH`, `MOD_APC_BASIC`, `MOD_VISUAL`, `MOD_RULE`, `MOD_YIELD`, `MOD_BATCH_CTRL` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_CYCLE_TIME`, `KPI_WIP_TURN`, `KPI_DISPATCH_STABILITY` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## B-5. 광·센서 / 光学/传感 / Optical / Sensor
`slug = optical_sensor`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 박막 증착 → 광학 정렬 → 다이싱 → 패키지 |
| 공정 흐름 (zh) | 薄膜沉积 → 光学对位 → 划片 → 封装 |
| 공정 흐름 (en) | Thin film → Optical alignment → Dicing → Package |
| 라우팅 | `RT_REENTRANT` — 재진입형 (Reentrant) — 동일 공정/설비를 여러 번 다시 통과. 디스패칭 룰이 사이클 타임 결정. |
| MVP 기능 (raw) | `MVP_LOT_TRACK`, `MVP_WIP_VIS`, `MVP_RULE_DISPATCH`, `MVP_RECIPE_CTRL`, `MVP_YIELD_MON`, `MVP_ALARM_CLOSED_LOOP`, `MVP_PROCESS_MON` |
| 핵심 모듈 (raw) | `MOD_PC`, `MOD_DISPATCH`, `MOD_APC_BASIC`, `MOD_VISUAL`, `MOD_RULE`, `MOD_YIELD`, `MOD_PROCESS_MON` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_CYCLE_TIME`, `KPI_WIP_TURN`, `KPI_DISPATCH_STABILITY`, `KPI_FIRST_PASS_YIELD` |
| 시스템 방향성 (raw) | `DISPATCH`, `WIP`, `CT` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## B-6. 화합물 반도체 (SiC/GaN) / 化合物半导体 (SiC/GaN) / Compound Semi (SiC/GaN)
`slug = compound_semi`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 단결정 성장 → 슬라이싱 → 에피 → 디바이스 가공 |
| 공정 흐름 (zh) | 单晶生长 → 切片 → 外延 → 器件加工 |
| 공정 흐름 (en) | Crystal growth → Slicing → Epi → Device fab |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_LOT_TRACK`, `MVP_WIP_VIS`, `MVP_RULE_DISPATCH`, `MVP_RECIPE_CTRL`, `MVP_YIELD_MON`, `MVP_ALARM_CLOSED_LOOP`, `MVP_PROCESS_MON` |
| 핵심 모듈 (raw) | `MOD_PC`, `MOD_DISPATCH`, `MOD_APC_BASIC`, `MOD_VISUAL`, `MOD_RULE`, `MOD_YIELD`, `MOD_PROCESS_MON` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_CYCLE_TIME`, `KPI_WIP_TURN`, `KPI_DISPATCH_STABILITY`, `KPI_FIRST_PASS_YIELD` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## B-7. 조립·패키징 / 封装 / Assembly / Packaging
`slug = assembly_packaging`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 다이 어태치 → 와이어/플립칩 본딩 → 몰딩 → 마킹·테스트 |
| 공정 흐름 (zh) | 贴片 → 引线/倒装焊 → 模压 → 标记·测试 |
| 공정 흐름 (en) | Die attach → Wire/Flip-chip bond → Mold → Mark & test |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_LOT_TRACK`, `MVP_WIP_VIS`, `MVP_RULE_DISPATCH`, `MVP_RECIPE_CTRL`, `MVP_YIELD_MON`, `MVP_ALARM_CLOSED_LOOP`, `MVP_UNIT_TRACE` |
| 핵심 모듈 (raw) | `MOD_PC`, `MOD_DISPATCH`, `MOD_APC_BASIC`, `MOD_VISUAL`, `MOD_RULE`, `MOD_YIELD`, `MOD_ASSEMBLY_CTRL` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_CYCLE_TIME`, `KPI_WIP_TURN`, `KPI_DISPATCH_STABILITY`, `KPI_LINE_BALANCE` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## B-8. 테스트 / 测试 / Test
`slug = test`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 프로브 테스트 → 번인 → 최종 테스트·분류 |
| 공정 흐름 (zh) | 探针测试 → 老化 → 最终测试·分类 |
| 공정 흐름 (en) | Probe test → Burn-in → Final test & sort |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_LOT_TRACK`, `MVP_WIP_VIS`, `MVP_RULE_DISPATCH`, `MVP_RECIPE_CTRL`, `MVP_YIELD_MON`, `MVP_ALARM_CLOSED_LOOP`, `MVP_PROCESS_MON` |
| 핵심 모듈 (raw) | `MOD_PC`, `MOD_DISPATCH`, `MOD_APC_BASIC`, `MOD_VISUAL`, `MOD_RULE`, `MOD_YIELD`, `MOD_PROCESS_MON` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_CYCLE_TIME`, `KPI_WIP_TURN`, `KPI_DISPATCH_STABILITY`, `KPI_FIRST_PASS_YIELD` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

# C. 전자 조립 제조 / 电子装配制造

세부 산업 수: **7**


## C-1. EMS (전자 수탁 제조) / EMS (电子代工) / EMS
`slug = ems`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 수주 → BOM 등록 → SMT/PCBA → 조립·테스트 → 출하 (다고객) |
| 공정 흐름 (zh) | 接单 → BOM 登记 → SMT/PCBA → 装配·测试 → 出货 (多客户) |
| 공정 흐름 (en) | Order → BOM → SMT/PCBA → Assembly & test → Ship (multi-customer) |
| 라우팅 | `RT_JOBSHOP` — (라우팅 정의 없음) |
| MVP 기능 (raw) | `MVP_BOARD_TRACK`, `MVP_WIP_VIS`, `MVP_MATERIAL_SYNC`, `MVP_LINE_BALANCE`, `MVP_ORDER_TRACK` |
| 핵심 모듈 (raw) | `MOD_LINE_CTRL`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL`, `MOD_WO` |
| KPI 키워드 (raw) | `KPI_OEE`, `KPI_FIRST_PASS_YIELD`, `KPI_LINE_BALANCE`, `KPI_THROUGHPUT`, `KPI_DELIVERY` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `SCHEDULING` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## C-2. SMT 조립 / SMT 贴装 / SMT Assembly
`slug = smt_assembly`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 스텐실 인쇄 → 마운팅 → 리플로우 → AOI/X-ray 검사 |
| 공정 흐름 (zh) | 钢网印刷 → 贴装 → 回流焊 → AOI/X-ray 检测 |
| 공정 흐름 (en) | Stencil print → Mount → Reflow → AOI/X-ray |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_BOARD_TRACK`, `MVP_WIP_VIS`, `MVP_MATERIAL_SYNC`, `MVP_LINE_BALANCE`, `MVP_LINE_VIS` |
| 핵심 모듈 (raw) | `MOD_LINE_CTRL`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_OEE`, `KPI_FIRST_PASS_YIELD`, `KPI_LINE_BALANCE`, `KPI_THROUGHPUT` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## C-3. PCB / PCBA / PCB / PCBA / PCB / PCBA
`slug = pcb_pcba`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 회로 설계 → 동박 적층 → 식각·도금 → 부품 실장 |
| 공정 흐름 (zh) | 电路设计 → 铜箔层压 → 刻蚀·电镀 → 元件贴装 |
| 공정 흐름 (en) | Circuit design → Cu lamination → Etch/plate → Component mount |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_BOARD_TRACK`, `MVP_WIP_VIS`, `MVP_MATERIAL_SYNC`, `MVP_LINE_BALANCE`, `MVP_PROCESS_MON` |
| 핵심 모듈 (raw) | `MOD_LINE_CTRL`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL`, `MOD_PROCESS_MON` |
| KPI 키워드 (raw) | `KPI_OEE`, `KPI_FIRST_PASS_YIELD`, `KPI_LINE_BALANCE`, `KPI_THROUGHPUT`, `KPI_YIELD` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## C-4. 산업용 전자 / 工业电子 / Industrial Electronics
`slug = industrial_electronics`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 회로 설계 → SMT → 함체 조립 → 환경 시험 (고신뢰) |
| 공정 흐름 (zh) | 电路设计 → SMT → 机壳装配 → 环境试验 (高可靠) |
| 공정 흐름 (en) | Circuit design → SMT → Enclosure → Env test (high-rel) |
| 라우팅 | `RT_JOBSHOP` — (라우팅 정의 없음) |
| MVP 기능 (raw) | `MVP_BOARD_TRACK`, `MVP_WIP_VIS`, `MVP_MATERIAL_SYNC`, `MVP_LINE_BALANCE`, `MVP_PROCESS_MON` |
| 핵심 모듈 (raw) | `MOD_LINE_CTRL`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL`, `MOD_QM` |
| KPI 키워드 (raw) | `KPI_OEE`, `KPI_FIRST_PASS_YIELD`, `KPI_LINE_BALANCE`, `KPI_THROUGHPUT` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `SCHEDULING` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## C-5. 통신 장비 / 通信设备 / Telecom Equipment
`slug = telecom_equipment`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 회로 설계 → SMT → RF/광 모듈 조립 → 망 적합성 시험 |
| 공정 흐름 (zh) | 电路设计 → SMT → RF/光模组装配 → 网络兼容性测试 |
| 공정 흐름 (en) | Circuit design → SMT → RF/optical module → Network compliance |
| 라우팅 | `RT_JOBSHOP` — (라우팅 정의 없음) |
| MVP 기능 (raw) | `MVP_BOARD_TRACK`, `MVP_WIP_VIS`, `MVP_MATERIAL_SYNC`, `MVP_LINE_BALANCE`, `MVP_PROCESS_MON` |
| 핵심 모듈 (raw) | `MOD_LINE_CTRL`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL`, `MOD_QM` |
| KPI 키워드 (raw) | `KPI_OEE`, `KPI_FIRST_PASS_YIELD`, `KPI_LINE_BALANCE`, `KPI_THROUGHPUT` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `SCHEDULING` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## C-6. 소비자 전자 / 消费电子 / Consumer Electronics
`slug = consumer_electronics`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | SMT → 케이스 조립 → 캘리브레이션 → 포장·라벨링 (다 SKU) |
| 공정 흐름 (zh) | SMT → 外壳装配 → 校准 → 包装·标签 (多 SKU) |
| 공정 흐름 (en) | SMT → Case assembly → Calibration → Pack/label (multi-SKU) |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_BOARD_TRACK`, `MVP_WIP_VIS`, `MVP_MATERIAL_SYNC`, `MVP_LINE_BALANCE`, `MVP_LINE_VIS` |
| 핵심 모듈 (raw) | `MOD_LINE_CTRL`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_OEE`, `KPI_FIRST_PASS_YIELD`, `KPI_LINE_BALANCE`, `KPI_THROUGHPUT` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## C-7. 정밀 모듈 / 精密模组 / Precision Modules
`slug = precision_modules`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 정밀 부품 가공 → 광학·전자 모듈 조립 → 정합·캘리브레이션 |
| 공정 흐름 (zh) | 精密零件加工 → 光学·电子模组装配 → 校准 |
| 공정 흐름 (en) | Precision parts → Optical/electronic module → Calibration |
| 라우팅 | `RT_JOBSHOP` — (라우팅 정의 없음) |
| MVP 기능 (raw) | `MVP_BOARD_TRACK`, `MVP_WIP_VIS`, `MVP_MATERIAL_SYNC`, `MVP_LINE_BALANCE`, `MVP_UNIT_TRACE`, `MVP_PROCESS_MON` |
| 핵심 모듈 (raw) | `MOD_LINE_CTRL`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL`, `MOD_ASSEMBLY_CTRL`, `MOD_PROCESS_MON` |
| KPI 키워드 (raw) | `KPI_OEE`, `KPI_FIRST_PASS_YIELD`, `KPI_LINE_BALANCE`, `KPI_THROUGHPUT` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `SCHEDULING` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

# D. 디스플레이·신에너지 제조 / 面板与新能源制造

세부 산업 수: **5**


## D-1. LCD / LCD / LCD
`slug = lcd`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 기판 세정 → TFT 박막 → 컬러필터 → 셀 합착 → 모듈 조립 |
| 공정 흐름 (zh) | 基板清洗 → TFT 薄膜 → 彩色滤光片 → 贴合 → 模组装配 |
| 공정 흐름 (en) | Substrate clean → TFT thin film → Color filter → Cell bond → Module |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_BATCH_TRACK`, `MVP_WIP_VIS`, `MVP_PROCESS_MON`, `MVP_YIELD_MON`, `MVP_LINE_VIS` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_PROCESS_MON`, `MOD_YIELD`, `MOD_LINE_CTRL` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_OEE`, `KPI_THROUGHPUT`, `KPI_PROCESS_STABILITY`, `KPI_LINE_BALANCE` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## D-2. OLED / OLED / OLED
`slug = oled`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 기판 세정 → LTPS/LTPO TFT → OLED 증착 → 인캡슐레이션 → 모듈 |
| 공정 흐름 (zh) | 基板清洗 → LTPS/LTPO TFT → OLED 蒸镀 → 封装 → 模组 |
| 공정 흐름 (en) | Substrate clean → LTPS/LTPO TFT → OLED deposition → Encap → Module |
| 라우팅 | `RT_REENTRANT` — 재진입형 (Reentrant) — 동일 공정/설비를 여러 번 다시 통과. 디스패칭 룰이 사이클 타임 결정. |
| MVP 기능 (raw) | `MVP_BATCH_TRACK`, `MVP_WIP_VIS`, `MVP_PROCESS_MON`, `MVP_YIELD_MON` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_PROCESS_MON`, `MOD_YIELD` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_OEE`, `KPI_THROUGHPUT`, `KPI_PROCESS_STABILITY` |
| 시스템 방향성 (raw) | `DISPATCH`, `WIP`, `CT` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## D-3. 태양광 (Solar PV) / 太阳能光伏 / Solar PV
`slug = solar_pv`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 잉곳 → 웨이퍼 → 셀 텍스처/도핑 → 모듈 라미네이션 |
| 공정 흐름 (zh) | 硅锭 → 晶圆 → 电池绒面/掺杂 → 组件层压 |
| 공정 흐름 (en) | Ingot → Wafer → Cell texture/doping → Module lamination |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_BATCH_TRACK`, `MVP_WIP_VIS`, `MVP_PROCESS_MON`, `MVP_YIELD_MON`, `MVP_LINE_VIS` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_PROCESS_MON`, `MOD_YIELD`, `MOD_LINE_CTRL` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_OEE`, `KPI_THROUGHPUT`, `KPI_PROCESS_STABILITY` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## D-4. 2차전지 / 二次电池 / Battery
`slug = battery`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 전극 코팅 → 압연·노칭 → 권취/적층 → 활성화·포메이션 |
| 공정 흐름 (zh) | 极片涂布 → 辊压·分切 → 卷绕/叠片 → 化成 |
| 공정 흐름 (en) | Electrode coat → Calendering/slit → Wind/stack → Formation |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_BATCH_TRACK`, `MVP_WIP_VIS`, `MVP_PROCESS_MON`, `MVP_YIELD_MON`, `MVP_LINE_VIS` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_PROCESS_MON`, `MOD_YIELD` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_OEE`, `KPI_THROUGHPUT`, `KPI_PROCESS_STABILITY` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## D-5. ESS 에너지 저장 시스템 / ESS 储能系统 / Energy Storage (ESS)
`slug = energy_storage`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 셀 → 모듈 → PCS/EMS 통합 → 사이트 설치·시운전 |
| 공정 흐름 (zh) | 电芯 → 模组 → PCS/EMS 集成 → 现场安装·试运行 |
| 공정 흐름 (en) | Cells → Modules → PCS/EMS integration → Site install & commission |
| 라우팅 | `RT_PROJECT` — 프로젝트형 (Project) — 1건당 계획·자원·납기 관리. 사이트/EPC 성격. |
| MVP 기능 (raw) | `MVP_BATCH_TRACK`, `MVP_WIP_VIS`, `MVP_PROCESS_MON`, `MVP_YIELD_MON`, `MVP_PROGRESS_MON` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_PROCESS_MON`, `MOD_YIELD`, `MOD_PROJECT_PLAN` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_OEE`, `KPI_THROUGHPUT`, `KPI_PROCESS_STABILITY`, `KPI_PROJECT_PROGRESS` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `DELIVERY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

# E. 프로세스·화학 제조 / 流程化工制造

세부 산업 수: **5**


## E-1. 석유화학 / 石油化工 / Petrochemical
`slug = petrochemical`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 원유 → 분별증류 → 크래킹 → 정제 → 폴리머 (연속공정) |
| 공정 흐름 (zh) | 原油 → 分馏 → 裂解 → 精制 → 聚合物 (连续工艺) |
| 공정 흐름 (en) | Crude → Distill → Crack → Refine → Polymer (continuous) |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_RECIPE_CTRL`, `MVP_PROCESS_MON`, `MVP_BATCH_TRACK` |
| 핵심 모듈 (raw) | `MOD_RECIPE`, `MOD_PROCESS_MON` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_PROCESS_STABILITY`, `KPI_ENERGY_EFFICIENCY` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## E-2. 정밀화학 / 精细化工 / Fine Chemical
`slug = fine_chemical`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 합성 → 정제 → 정밀 측정 → 고순도 패키징 (다품종 소량) |
| 공정 흐름 (zh) | 合成 → 精制 → 精密测量 → 高纯包装 (多品种小量) |
| 공정 흐름 (en) | Synthesis → Purify → Precision metrology → High-purity pack |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_RECIPE_CTRL`, `MVP_PROCESS_MON`, `MVP_BATCH_TRACK` |
| 핵심 모듈 (raw) | `MOD_RECIPE`, `MOD_PROCESS_MON` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_PROCESS_STABILITY`, `KPI_ENERGY_EFFICIENCY`, `KPI_FIRST_PASS_YIELD` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## E-3. 고분자 소재 / 高分子材料 / Polymer Materials
`slug = polymer_materials`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 중합 → 압출 → 펠릿화 → 가공·블렌딩 |
| 공정 흐름 (zh) | 聚合 → 挤出 → 造粒 → 加工·混合 |
| 공정 흐름 (en) | Polymerize → Extrude → Pelletize → Compound/blend |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_RECIPE_CTRL`, `MVP_PROCESS_MON`, `MVP_BATCH_TRACK` |
| 핵심 모듈 (raw) | `MOD_RECIPE`, `MOD_PROCESS_MON` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_PROCESS_STABILITY`, `KPI_ENERGY_EFFICIENCY` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## E-4. 특수가스 / 特种气体 / Specialty Gas
`slug = specialty_gas`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 원료 정제 → 액화 → 정밀 충전 → 출하 (고순도) |
| 공정 흐름 (zh) | 原料精制 → 液化 → 精密充装 → 出货 (高纯) |
| 공정 흐름 (en) | Feedstock refine → Liquefy → Precision fill → Ship (high purity) |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_RECIPE_CTRL`, `MVP_PROCESS_MON`, `MVP_BATCH_TRACK`, `MVP_BATCH_TRACE` |
| 핵심 모듈 (raw) | `MOD_RECIPE`, `MOD_PROCESS_MON`, `MOD_BATCH_CTRL` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_PROCESS_STABILITY`, `KPI_ENERGY_EFFICIENCY`, `KPI_DEVIATION_RATE` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## E-5. 무기 소재 / 无机材料 / Inorganic Materials
`slug = inorganic_materials`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 원료 분쇄 → 합성·소성 → 분급 → 패키징 |
| 공정 흐름 (zh) | 原料粉碎 → 合成·烧结 → 分级 → 包装 |
| 공정 흐름 (en) | Raw grind → Synth/sinter → Classify → Pack |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_RECIPE_CTRL`, `MVP_PROCESS_MON`, `MVP_BATCH_TRACK`, `MVP_BATCH_TRACE` |
| 핵심 모듈 (raw) | `MOD_RECIPE`, `MOD_PROCESS_MON`, `MOD_BATCH_CTRL` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_PROCESS_STABILITY`, `KPI_ENERGY_EFFICIENCY` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

# F. 소비재·식품 제조 / 消费品与食品制造

세부 산업 수: **5**


## F-1. 식품 가공 / 食品加工 / Food Processing
`slug = food_processing`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 원료 입고 → 가공·살균 → 충전·포장 → 보관 (HACCP) |
| 공정 흐름 (zh) | 原料入库 → 加工·杀菌 → 灌装·包装 → 储存 (HACCP) |
| 공정 흐름 (en) | Raw intake → Process/pasteurize → Fill/pack → Store (HACCP) |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_BATCH_TRACE`, `MVP_LINE_VIS`, `MVP_QUALITY_MON`, `MVP_MATERIAL_SYNC`, `MVP_ORDER_TRACK` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_LINE_CTRL`, `MOD_QUALITY`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_OEE`, `KPI_THROUGHPUT`, `KPI_DELIVERY`, `KPI_LINE_BALANCE`, `KPI_RECALL_SCOPE` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## F-2. 음료·주류 / 饮料·酒类 / Beverage
`slug = beverage`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 원료 혼합 → 충전·캡핑 → 살균 → 라벨링 |
| 공정 흐름 (zh) | 原料混合 → 灌装·封盖 → 杀菌 → 标签 |
| 공정 흐름 (en) | Mix → Fill/cap → Pasteurize → Label |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_BATCH_TRACE`, `MVP_LINE_VIS`, `MVP_QUALITY_MON`, `MVP_MATERIAL_SYNC`, `MVP_ORDER_TRACK` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_LINE_CTRL`, `MOD_QUALITY`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_OEE`, `KPI_THROUGHPUT`, `KPI_DELIVERY`, `KPI_LINE_BALANCE` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## F-3. 퍼스널 케어 (화장품·헬스) / 个人护理 (化妆品·健康) / Personal Care
`slug = personal_care`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 원료 혼합 → 충진 → 포장 (다 SKU, GMP 준용) |
| 공정 흐름 (zh) | 原料混合 → 灌装 → 包装 (多 SKU, 准 GMP) |
| 공정 흐름 (en) | Mix → Fill → Pack (multi-SKU, GMP-aligned) |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_BATCH_TRACE`, `MVP_LINE_VIS`, `MVP_QUALITY_MON`, `MVP_MATERIAL_SYNC`, `MVP_ORDER_TRACK` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_LINE_CTRL`, `MOD_QUALITY`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_OEE`, `KPI_THROUGHPUT`, `KPI_DELIVERY`, `KPI_LINE_BALANCE`, `KPI_BATCH_RELEASE` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## F-4. 홈 케어 (세제·위생) / 家庭清洁 (洗涤·卫生) / Home Care
`slug = home_care`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 원료 혼합 → 충진 → 포장 (대량 양산) |
| 공정 흐름 (zh) | 原料混合 → 灌装 → 包装 (大批量) |
| 공정 흐름 (en) | Mix → Fill → Pack (mass production) |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_BATCH_TRACE`, `MVP_LINE_VIS`, `MVP_QUALITY_MON`, `MVP_MATERIAL_SYNC`, `MVP_ORDER_TRACK` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_LINE_CTRL`, `MOD_QUALITY`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_OEE`, `KPI_THROUGHPUT`, `KPI_DELIVERY`, `KPI_LINE_BALANCE` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## F-5. 일반 소비재 / 一般消费品 / Consumer Goods
`slug = consumer_goods`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 조립·포장 (다 SKU 양산) |
| 공정 흐름 (zh) | 装配·包装 (多 SKU 量产) |
| 공정 흐름 (en) | Assembly & pack (multi-SKU) |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_BATCH_TRACE`, `MVP_LINE_VIS`, `MVP_QUALITY_MON`, `MVP_MATERIAL_SYNC`, `MVP_ORDER_TRACK` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_LINE_CTRL`, `MOD_QUALITY`, `MOD_MATERIAL_CTRL`, `MOD_VISUAL` |
| KPI 키워드 (raw) | `KPI_YIELD`, `KPI_OEE`, `KPI_THROUGHPUT`, `KPI_DELIVERY`, `KPI_LINE_BALANCE` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

# G. 의약품·바이오 제조 / 制药与生物制造

세부 산업 수: **5**


## G-1. 원료의약품 (API) / 原料药 (API) / API
`slug = api`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 합성 → 정제 → 결정화 → 분쇄·블렌딩 |
| 공정 흐름 (zh) | 合成 → 精制 → 结晶 → 粉碎·混合 |
| 공정 흐름 (en) | Synthesis → Purify → Crystallize → Mill/blend |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_BATCH_TRACE`, `MVP_RECIPE_CTRL`, `MVP_QUALITY_CTRL` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_QUALITY` |
| KPI 키워드 (raw) | `KPI_BATCH_RELEASE`, `KPI_YIELD`, `KPI_DEVIATION_RATE` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## G-2. 완제의약품 / 制剂 / Drug Product
`slug = drug_product`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 원료 칭량 → 과립·타정/충전 → 코팅 → 포장 (GMP) |
| 공정 흐름 (zh) | 原料称量 → 制粒·压片/灌装 → 包衣 → 包装 (GMP) |
| 공정 흐름 (en) | Weigh → Granulate/Tablet/Fill → Coat → Pack (GMP) |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_BATCH_TRACE`, `MVP_RECIPE_CTRL`, `MVP_QUALITY_CTRL`, `MVP_APPROVAL_CONTROL` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_QUALITY`, `MOD_COMPLIANCE` |
| KPI 키워드 (raw) | `KPI_BATCH_RELEASE`, `KPI_YIELD`, `KPI_DEVIATION_RATE` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## G-3. 바이오의약품 / 生物药 / Biologics
`slug = biologics`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 세포 배양 → 정제(downstream) → 제제화 → 무균 충전 (Annex 1) |
| 공정 흐름 (zh) | 细胞培养 → 纯化 (downstream) → 制剂 → 无菌灌装 (Annex 1) |
| 공정 흐름 (en) | Cell culture → Downstream purify → Formulate → Aseptic fill (Annex 1) |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_BATCH_TRACE`, `MVP_RECIPE_CTRL`, `MVP_QUALITY_CTRL`, `MVP_LOT_TRACK` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_QUALITY`, `MOD_DISPATCH`, `MOD_COMPLIANCE` |
| KPI 키워드 (raw) | `KPI_BATCH_RELEASE`, `KPI_YIELD`, `KPI_DEVIATION_RATE` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## G-4. 백신 / 疫苗 / Vaccine
`slug = vaccine`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 균주 배양 → 정제 → 백신 원액 → 충전 (cold chain) |
| 공정 흐름 (zh) | 菌株培养 → 纯化 → 疫苗原液 → 灌装 (冷链) |
| 공정 흐름 (en) | Strain culture → Purify → Vaccine drug substance → Fill (cold chain) |
| 라우팅 | `RT_BATCH` — 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행. |
| MVP 기능 (raw) | `MVP_BATCH_TRACE`, `MVP_RECIPE_CTRL`, `MVP_QUALITY_CTRL` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_QUALITY`, `MOD_COMPLIANCE` |
| KPI 키워드 (raw) | `KPI_BATCH_RELEASE`, `KPI_YIELD`, `KPI_DEVIATION_RATE` |
| 시스템 방향성 (raw) | `TRACEABILITY`, `RECIPE`, `QUALITY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## G-5. CDMO (위탁개발생산) / CDMO (合同开发生产) / CDMO
`slug = cdmo`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 고객 사양 인계 → 양산 적합화 → GMP 배치 양산 → 인도 |
| 공정 흐름 (zh) | 客户规格交接 → 量产适配 → GMP 批次量产 → 交付 |
| 공정 흐름 (en) | Spec transfer → Scale-up → GMP batch → Deliver |
| 라우팅 | `RT_JOBSHOP` — (라우팅 정의 없음) |
| MVP 기능 (raw) | `MVP_BATCH_TRACE`, `MVP_RECIPE_CTRL`, `MVP_QUALITY_CTRL` |
| 핵심 모듈 (raw) | `MOD_BATCH_CTRL`, `MOD_QUALITY` |
| KPI 키워드 (raw) | `KPI_BATCH_RELEASE`, `KPI_YIELD`, `KPI_DEVIATION_RATE` |
| 시스템 방향성 (raw) | `ORDER`, `RESOURCE`, `SCHEDULING` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

# H. 자동차·장비 제조 / 汽车与装备制造

세부 산업 수: **6**


## H-1. 완성차 OEM / 整车 OEM / Vehicle OEM
`slug = vehicle_oem`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 프레스 → 차체 용접 → 도장 → 의장 조립 → 시험 (라인 양산) |
| 공정 흐름 (zh) | 冲压 → 车身焊接 → 涂装 → 内饰装配 → 测试 (流水线) |
| 공정 흐름 (en) | Stamp → Body weld → Paint → Trim assembly → Test (line) |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_UNIT_TRACE`, `MVP_LINE_BALANCE`, `MVP_SUPPLY_SYNC`, `MVP_LINE_VIS` |
| 핵심 모듈 (raw) | `MOD_ASSEMBLY_CTRL`, `MOD_SUPPLY_CHAIN` |
| KPI 키워드 (raw) | `KPI_OEE`, `KPI_DELIVERY`, `KPI_LINE_BALANCE` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## H-2. 파워트레인 / 动力总成 / Powertrain
`slug = powertrain`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 주조·단조·가공 → 조립 → 시험 (모듈 JIT) |
| 공정 흐름 (zh) | 铸造·锻造·加工 → 装配 → 测试 (模块 JIT) |
| 공정 흐름 (en) | Cast/forge/machine → Assembly → Test (JIT module) |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_UNIT_TRACE`, `MVP_LINE_BALANCE`, `MVP_SUPPLY_SYNC`, `MVP_BATCH_TRACE`, `MVP_LINE_VIS` |
| 핵심 모듈 (raw) | `MOD_ASSEMBLY_CTRL`, `MOD_SUPPLY_CHAIN`, `MOD_BATCH_CTRL` |
| KPI 키워드 (raw) | `KPI_OEE`, `KPI_DELIVERY`, `KPI_LINE_BALANCE`, `KPI_YIELD` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## H-3. EV 구동 시스템 / EV 驱动系统 / EV Drive System
`slug = ev_drive_system`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 셀·모듈 → 인버터·DCDC → 시스템 조립 → 차량 통합 |
| 공정 흐름 (zh) | 电芯·模组 → 逆变器·DCDC → 系统装配 → 整车集成 |
| 공정 흐름 (en) | Cells/modules → Inverter/DCDC → System assembly → Vehicle integration |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_UNIT_TRACE`, `MVP_LINE_BALANCE`, `MVP_SUPPLY_SYNC` |
| 핵심 모듈 (raw) | `MOD_ASSEMBLY_CTRL`, `MOD_SUPPLY_CHAIN` |
| KPI 키워드 (raw) | `KPI_OEE`, `KPI_DELIVERY`, `KPI_LINE_BALANCE` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## H-4. 섀시 부품 / 底盘部件 / Chassis Components
`slug = chassis_components`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 프레스·가공 → 용접 → 도장 (모듈 JIT) |
| 공정 흐름 (zh) | 冲压·加工 → 焊接 → 涂装 (模块 JIT) |
| 공정 흐름 (en) | Stamp/machine → Weld → Paint (JIT module) |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_UNIT_TRACE`, `MVP_LINE_BALANCE`, `MVP_SUPPLY_SYNC`, `MVP_LINE_VIS` |
| 핵심 모듈 (raw) | `MOD_ASSEMBLY_CTRL`, `MOD_SUPPLY_CHAIN`, `MOD_LINE_CTRL` |
| KPI 키워드 (raw) | `KPI_OEE`, `KPI_DELIVERY`, `KPI_LINE_BALANCE` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## H-5. 자동차 전자·전장 / 汽车电子 / Automotive Electronics
`slug = automotive_electronics`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 회로 설계 → SMT/PCBA → ECU 조립 → 차량 적합 시험 |
| 공정 흐름 (zh) | 电路设计 → SMT/PCBA → ECU 装配 → 车规试验 |
| 공정 흐름 (en) | Circuit design → SMT/PCBA → ECU assembly → Vehicle test |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_UNIT_TRACE`, `MVP_LINE_BALANCE`, `MVP_SUPPLY_SYNC`, `MVP_PROCESS_MON` |
| 핵심 모듈 (raw) | `MOD_ASSEMBLY_CTRL`, `MOD_SUPPLY_CHAIN`, `MOD_QM` |
| KPI 키워드 (raw) | `KPI_OEE`, `KPI_DELIVERY`, `KPI_LINE_BALANCE`, `KPI_FIRST_PASS_YIELD` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## H-6. Tier1 / Tier2 부품 공급사 / Tier1 / Tier2 零部件 / Tier1 / Tier2 Suppliers
`slug = tier1_tier2_suppliers`

### 현재 raw 데이터

| 항목 | 내용 |
|------|------|
| 공정 흐름 (ko) | 부품 가공 → 모듈 조립 → 검사 (JIT 납품) |
| 공정 흐름 (zh) | 零件加工 → 模组装配 → 检测 (JIT 供货) |
| 공정 흐름 (en) | Parts machining → Module assembly → Inspect (JIT) |
| 라우팅 | `RT_LINE` — 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률. |
| MVP 기능 (raw) | `MVP_UNIT_TRACE`, `MVP_LINE_BALANCE`, `MVP_SUPPLY_SYNC` |
| 핵심 모듈 (raw) | `MOD_ASSEMBLY_CTRL`, `MOD_SUPPLY_CHAIN` |
| KPI 키워드 (raw) | `KPI_OEE`, `KPI_DELIVERY`, `KPI_LINE_BALANCE` |
| 시스템 방향성 (raw) | `VISIBILITY`, `EFFICIENCY` |

### ▶ 공정 상세 (보완 필요)

8~15단계, 각 단계에 짧은 설명. 예시 포맷:

```
1. (공정명) — (설비/공정 핵심 설명)
2. ...
```

**ko**:

```
(여기 채워주세요)
```

**zh**:

```
(여기 채워주세요)
```

**en**:

```
(여기 채워주세요)
```

### ▶ 핵심 관리점 (보완 필요)

5~8개. 현장에서 매일 봐야 하는 것. 결과 KPI(수율/OEE)가 아니라 "이 값/기록을 놓치면 안 됨".

**ko**:

- (예) 포토 마스크 정렬 오차 ≤ 5nm — 로트별 측정·기록
- (예) 챔버 가스 변경 이력 — lot 단위 추적
- ...

**zh**:

- ...

**en**:

- ...

---

## 부록 A — 라우팅 4종 설명 (Step5 1.1 카드 표시용, 보완 필요)

아래 4종은 현재 사용 중. 각 항목에 ko/zh/en 1~2문장 설명을 채워주세요 (앞부분에 "라우팅" 칸의 자동 메모는 임시 초안일 뿐).

### `RT_LINE`
- 자동 초안 (ko): 라인형 (Linear) — 고정 순서 직선 흐름. 반복 없음. 산출 = 라인 속도 × 가동률.
- ko: 
- zh: 
- en: 

### `RT_BATCH`
- 자동 초안 (ko): 배치형 (Batch) — 로트/배치 단위 가공. 열처리·반응·시험이 묶음 단위로 진행.
- ko: 
- zh: 
- en: 

### `RT_REENTRANT`
- 자동 초안 (ko): 재진입형 (Reentrant) — 동일 공정/설비를 여러 번 다시 통과. 디스패칭 룰이 사이클 타임 결정.
- ko: 
- zh: 
- en: 

### `RT_PROJECT`
- 자동 초안 (ko): 프로젝트형 (Project) — 1건당 계획·자원·납기 관리. 사이트/EPC 성격.
- ko: 
- zh: 
- en: 

### `RT_JOB_SHOP`
- 자동 초안 (ko): 잡샵형 (Job Shop) — 다품종·다양한 라우팅, 설비 공유, 우선순위 변동 큼.
- ko: 
- zh: 
- en: 

### `RT_ASSEMBLY`
- 자동 초안 (ko): 조립형 (Assembly) — 다수 부품을 결합해 최종 제품화. BOM·서브어셈블리 핵심.
- ko: 
- zh: 
- en: 

### `RT_CONTINUOUS`
- 자동 초안 (ko): 연속형 (Continuous) — 시작/끝 없이 연속 운전. 공정 파라미터 안정성이 본질.
- ko: 
- zh: 
- en: 

---

## 부록 B — 작업 우선순위 제안

1. **B 반도체 (8 sub)** — 라우팅 다양성 가장 큼, 문서 [process_analysis_B_D_sample.md] 에 이미 분석 있음
2. **D 디스플레이/신에너지 (5 sub)** — 라인형 vs 프로젝트형 분기, 위 문서에 분석 있음
3. **C 전자 조립 (7 sub)** — 잡샵 성격, 다품종
4. **H 자동차/장비 (6 sub)** — 조립형 + 공급망 계층
5. **G 의약/바이오 (5 sub)** — 규제·배치
6. **E 프로세스/화학 (5 sub)** — 연속·배치
7. **F 소비재/식품 (5 sub)** — SKU 양산
8. **A 프로젝트형 (8 sub)** — EPC 성격, 모두 동일 raw 데이터 (RT_PROJECT)