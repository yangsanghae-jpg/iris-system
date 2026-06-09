# Ch2.6 데이터·AI 도메인 — 데이터팩 작업표 (8 산업)

> 데이터 출처: `server/knowledge/step5/ch2/card6/10_card6_master.json` (V1.52-B-pilot)
> 작성일: 2026-06-05
> 목적: 8개 산업의 Ch2.6(데이터·AI 도메인) 현재 데이터팩을 한눈에 정리. 사용자가 직접 보완 가능한 작업표 형태.

---

## 0. 보강 상태 요약

| 산업 | role 수 | label_ko | data_sources_ko | key_kpis_top3_ko | 상태 |
|------|---------|----------|-----------------|------------------|------|
| **A** 프로젝트형 제조 | 5 | 0/5 | 0/5 | 0/5 | ⏳ 미보강 |
| **B** 반도체 제조 | 6 | 6/6 | 6/6 | 6/6 | ✅ 완료 |
| **C** 전자 조립 제조 | 5 | 0/5 | 0/5 | 0/5 | ⏳ 미보강 |
| **D** 디스플레이·신에너지 제조 | 5 | 0/5 | 0/5 | 0/5 | ⏳ 미보강 |
| **E** 프로세스·화학 제조 | 6 | 0/6 | 0/6 | 0/6 | ⏳ 미보강 |
| **F** 소비재·식품 제조 | 6 | 0/6 | 0/6 | 0/6 | ⏳ 미보강 |
| **G** 의약품·바이오 제조 | 6 | 0/6 | 0/6 | 0/6 | ⏳ 미보강 |
| **H** 자동차·장비 제조 | 6 | 0/6 | 0/6 | 0/6 | ⏳ 미보강 |

- ✅ B (반도체) 만 V1.52 보강 완료 (파일럿)
- ⏳ A·C·D·E·F·G·H 7개 산업은 zh + metrics 만 존재

---

## 1. 공통 카탈로그 (role_master 10종)

Ch2.6 에서 사용 가능한 role 코드 풀. 산업별 role_by_industry 에서 이 코드 중 5~6개를 선택.

| role_code | zh | ko | en | summary_ko |
|-----------|----|----|----|------------|
| `PROD_OPS` | 生产运营管理 | 생산 운영 관리 | Production Operations | 투입·재공·사이클 타임 등 일일 운영 페이스 지표를 통합 가시화 |
| `QUALITY` | 质量管控 | 품질 관리 | Quality | 수율·결함밀도·FPY·Hold 등 품질 신호 폐루프 |
| `LOGISTICS` | 仓储物流管理 | 물류·창고 관리 | Logistics & Warehouse | 라인사이드 키트·재고·보충·AGV/AMHS 가시화 |
| `PLAN_DELIVERY` | 计划与交付协同 | 계획·납기 협업 | Planning & Delivery | 스케줄링·디스패치·납기 이행률 통합 추적 |
| `EQUIPMENT` | 设备稼动与效能管理 | 설비 가동·효능 관리 | Equipment Effectiveness | OEE·가용성·다운타임·병목 설비 부하 분석 |
| `COST_EFF` | 成本与效率管理 | 원가·효율 관리 | Cost & Efficiency | 단위 원가·전력·소모재·인건비 효율 추적 |
| `TRACE` | 追溯与谱系管理 | 추적·계보 관리 | Traceability & Genealogy | Lot↔Wafer↔Die↔Recipe↔Tool 풀 체인 계보 추적 |
| `ENERGY` | 能耗与公辅管理 | 에너지·유틸리티 관리 | Energy & Utilities | 단위 전력·UPW·CDA·N2·CO2 등 유틸리티 모니터링 |
| `IMPROVEMENT` | 异常预警与持续改善 | 이상 경보·지속 개선 | Anomaly & Improvement | SPC·Excursion 경보, 폐루프 개선 액션 트래킹 |
| `GLOBAL` | 跨工厂运营对标 | 다공장 운영 벤치마킹 | Cross-Fab Benchmark | 팹 간 수율·CT·OEE 차이 분석과 베스트 프랙티스 공유 |

---

## 2. 규모별 능력 단계 (capabilities S1~S4)

산업 무관, **규모 S1~S4** 만으로 결정되는 카드. 보강 완료.

### S1 — S1 단일 공장 / S1 单工厂

- **권장 시스템**: ERP, MES, Basic Report
- **시스템 디테일**:
  - ERP — 출하/원가/회계 결산
  - MES — Lot·Recipe·Tool 실행 트랜잭션
  - Basic Report — 일/주/월 정형 보고서
- **요약 (ko)**: ERP·MES·기본 보고서를 중심으로 운영 지표를 사후 집계·조회
- **데이터 아키텍처 (ko)**: MES/ERP 트랜잭션 → 야간 배치 ETL → 사내 RDB → 정형 보고서
- **주요 특징**: 일/주/월 실적 집계, 기본 KPI 조회, 단일 공장 운영 확인
- **관리 포커스**:
  - 사후 통계 기반 생산 결과 확인
  - KPI 달성·미달성 판단
  - 보고서 기반 사람 손 분석
  - 문제 발견이 운영자 경험에 의존

### S2 — S2 다라인·전문 운영 / S2 多产线 / 专业运营

- **권장 시스템**: Professional Report, Specialized Kanban, Historian
- **시스템 디테일**:
  - Professional Report — 라인·공정 단위 전문 보고서
  - Specialized Kanban — 역할별(품질·설비·계획) 칸반
  - Historian — 설비 시계열 데이터 1차 통합
- **요약 (ko)**: 라인·공정 단위로 지표를 시각화하고 근실시간 운영을 구현
- **데이터 아키텍처 (ko)**: MES + Historian → 근실시간 스트림 → 라인/공정 마트 → 전문 보고서·칸반
- **주요 특징**: 전문 보고서, 역할 칸반, 라인/공정 뷰
- **관리 포커스**:
  - 라인/공정 실시간 모니터링
  - 이상 즉시 발견·대응
  - 칸반 기반 운영 디스패치
  - 생산 편차 빠른 시정
- **포함 단계**: S1

### S3 — S3 다공장 통합 분석 / S3 多工厂综合分析

- **권장 시스템**: DataPlatform, BI, Digital Twin
- **시스템 디테일**:
  - DataPlatform — Lake/Lakehouse + Mart, ETL/CDC + 데이터 품질
  - BI — 셀프 분석, 드릴다운, KPI 정의 거버넌스
  - Digital Twin — 라인/팹 시뮬레이션과 시나리오 분석
- **요약 (ko)**: 다공장 데이터를 통합해 KPI를 비교 분석하고, BI·디지털 트윈으로 추세·연관·예측·시뮬레이션을 수행
- **데이터 아키텍처 (ko)**: 다공장 MES·EAP·Historian → DataPlatform Lakehouse → 표준 KPI Mart → BI/DT 분석·예측
- **주요 특징**: 통합 KPI 대시보드, 드릴다운 분석, 시뮬레이션·예측 뷰
- **관리 포커스**:
  - 다공장 KPI 비교 분석
  - 이상 근본원인 분석(Why)
  - 추세 예측과 캐파 평가
  - 팹 간 의사결정 지원
- **포함 단계**: S1, S2

### S4 — S4 글로벌 통합 운영 / S4 全球综合运营

- **권장 시스템**: Global IMC, AI Knowledge Warehouse, MLOps, Feature Store
- **시스템 디테일**:
  - Global IMC — 글로벌 통합 운영 센터, 표준 KPI/메타 거버넌스
  - AI Knowledge Warehouse — 사례·룰·모델·라이브러리의 자산화
  - MLOps — 모델 학습·배포·모니터링·재학습 파이프라인
  - Feature Store — 학습/추론 공통 피처 일관성 보장
- **요약 (ko)**: 전 세계 공장의 KPI를 표준화하고 지역·팹·제품군을 통합 모니터링, 지표 이력과 개선 사례를 AI 지식으로 자산화하여 재사용
- **데이터 아키텍처 (ko)**: 전 팹 통합 Mesh → Global IMC + Feature Store/MLOps → AI 추론·자율 폐루프 → 표준 KPI 거버넌스
- **주요 특징**: 글로벌 KPI 표준, 통합 운영 허브, AI 지식 추천
- **관리 포커스**:
  - 글로벌 KPI 통일·벤치마킹
  - 이력·사례 재사용
  - AI 기반 이상 탐지·의사결정 권고
  - 운영 전략 자동 최적화
- **포함 단계**: S1, S2, S3

---

## 3. 데이터 성숙도 (maturity_levels L1~L4)

산업 무관 공통. 규모(S1~S4) 에 따라 권장 단계 매핑 — S1→L1, S2→L2, S3→L3, S4→L4.

### L1 — L1 보고형 (Reporting)

- **요약 (ko)**: 정형 보고서로 사후 집계. 단일 공장·일/주/월 단위.
- **요약 (zh)**: 固定报表事后汇总。单工厂·日/周/月口径。
- **현재 단계의 신호 (evidence_ko)**:
  - 정형 일/주/월 보고서 자동 발행
  - 사후 분석 비중이 90% 이상
  - 이상 탐지는 사람 경험 의존

### L2 — L2 제조 BI (Manufacturing BI)

- **요약 (ko)**: 셀프 BI·역할 칸반·근실시간 모니터링. 라인·공정 단위 폐루프 시정.
- **요약 (zh)**: 自助 BI·角色看板·近实时监控。产线/工序级闭环纠正。
- **현재 단계의 신호 (evidence_ko)**:
  - 역할별 칸반 운영 (Quality·Equipment·Plan)
  - 이상 알람 → 운영자 조치까지 < 30분
  - 전문 보고서를 사용자가 직접 빌드

### L3 — L3 데이터 플랫폼 (Data Platform)

- **요약 (ko)**: Lakehouse 통합·표준 KPI Mart·디지털 트윈. 다공장 비교·예측·시뮬레이션.
- **요약 (zh)**: Lakehouse 集成·标准 KPI Mart·数字孪生。多工厂对比·预测·仿真。
- **현재 단계의 신호 (evidence_ko)**:
  - KPI 정의 마스터로 팹 간 동일 정의 사용
  - 디지털 트윈으로 시나리오 분석
  - 데이터 품질 SLA 운영(완전성/적시성/정확성)

### L4 — L4 산업 AI·자율 폐루프 (Industrial AI / Autonomous)

- **요약 (ko)**: Feature Store + MLOps 기반 모델 운영, 글로벌 IMC 표준화, AI 지식 추천과 자율 폐루프.
- **요약 (zh)**: Feature Store + MLOps 模型运维，全球 IMC 标准化，AI 知识推荐与自治闭环。
- **현재 단계의 신호 (evidence_ko)**:
  - 모델 모니터링·드리프트 감지·자동 재학습
  - Excursion 자동 분류·권고 액션 제시
  - AI 지식 창고로 사례·룰 자산화

---

## 4. 산업별 role_by_industry (8개)

각 산업 row 에 (a) 라벨 ko/en (b) data_sources_ko/zh/en (c) key_kpis_top3_ko/zh/en 를 보강.
**아래 표 자체가 작업표** — ⏳ 표시된 칸을 사용자가 직접 채우는 형식.

### A. 프로젝트형 제조 / 项目型制造

- 산업명 ko: ⏳
- 산업명 en: ⏳
- 정의된 role 수: **5** 개

#### PROD_OPS (priority=1)

| 항목 | 값 |
|------|----|
| label_zh | 制程生产运营 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 产量, 产出达成率, 在制品, Cycle Time, 换线时间 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### QUALITY (priority=2)

| 항목 | 값 |
|------|----|
| label_zh | 质量管控 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 一次通过率, 不良率, 直通率, AOI合格率, ICT/FCT合格率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### LOGISTICS (priority=3)

| 항목 | 값 |
|------|----|
| label_zh | 线边物料与仓储物流 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 线边齐套率, 缺料次数, 补料响应时间, 库存准确率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### PLAN_DELIVERY (priority=4)

| 항목 | 값 |
|------|----|
| label_zh | 生产计划与交付协同 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 排产达成率, 工单准时完工率, 按时交付率, 急单响应率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### EQUIPMENT (priority=5)

| 항목 | 값 |
|------|----|
| label_zh | 设备稼动与瓶颈工位管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 稼动率, 停机时长, OEE, 瓶颈工位负荷 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

### B. 반도체 제조 / 半导体制造

- 산업명 ko: 반도체 제조
- 산업명 en: Semiconductor
- 정의된 role 수: **6** 개

#### PROD_OPS (priority=1)

| 항목 | 값 |
|------|----|
| label_zh | 晶圆流转与生产运营 |
| label_ko | 웨이퍼 흐름·생산 운영 |
| label_en | Wafer Flow & Production Ops |
| metrics (zh) | 投片量, Move, 在制品, Turn Ratio, Cycle Time |
| metrics_ko | 투입량(Wafer Start), Move 수, 재공(WIP), Turn Ratio, Cycle Time |
| metrics_en | Wafer Starts, Moves, WIP, Turn Ratio, Cycle Time |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko:
  - MES(Lot 이벤트)
  - EAP(설비 Move)
  - Dispatcher 결정 로그
  - FOUP/캐리어 ID
- zh:
  - MES(Lot 事件)
  - EAP(设备 Move)
  - Dispatcher 决策日志
  - FOUP/Carrier ID
- en:
  - MES (lot events)
  - EAP (tool moves)
  - Dispatcher decision log
  - FOUP/carrier ID

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko:
  - Cycle Time x-factor (계획 대비 비)
  - WIP 분포의 병목 단계 비중
  - Turn Ratio (= Moves / WIP)
- zh:
  - Cycle Time x-factor
  - WIP 瓶颈步骤占比
  - Turn Ratio
- en:
  - Cycle Time x-factor
  - WIP share at bottleneck step
  - Turn Ratio (Moves/WIP)

---

#### QUALITY (priority=2)

| 항목 | 값 |
|------|----|
| label_zh | 良率与缺陷管理 |
| label_ko | 수율·결함 관리 |
| label_en | Yield & Defect |
| metrics (zh) | Yield, 一次通过率, 缺陷密度, 返工率, Hold率 |
| metrics_ko | Yield(수율), 1차 합격률 FPY, 결함 밀도 D0, 재작업률, Hold율 |
| metrics_en | Yield, First Pass Yield, Defect Density (D0), Rework rate, Hold rate |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko:
  - 계측(CD/Overlay/Film/Particle)
  - 검사(Defect map, KLA)
  - EDS/Sort 결과
  - MES Hold/Disposition
- zh:
  - 计量(CD/Overlay/Film/Particle)
  - 检测(Defect map, KLA)
  - EDS/Sort
  - MES Hold/Disposition
- en:
  - Metrology (CD/Overlay/Film/Particle)
  - Inspection (defect map, KLA)
  - EDS/Sort results
  - MES hold/disposition

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko:
  - Line Yield / Final Yield 격차
  - Top 결함 카테고리 Pareto 변화율
  - Hold 클리어 평균 시간(MTTR-Hold)
- zh:
  - Line/Final Yield Gap
  - Top Defect Pareto Δ
  - Hold MTTR
- en:
  - Line vs Final Yield gap
  - Top defect Pareto delta
  - Hold clearance MTTR

---

#### EQUIPMENT (priority=3)

| 항목 | 값 |
|------|----|
| label_zh | 设备稼动与机台效能 |
| label_ko | 설비 가동·효율 |
| label_en | Tool Effectiveness |
| metrics (zh) | OEE, Availability, Downtime, MTTR, 瓶颈机台负荷 |
| metrics_ko | OEE, 가용성(A), 다운타임, MTTR, 병목 설비 부하 |
| metrics_en | OEE, Availability, Downtime, MTTR, Bottleneck loading |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko:
  - EAP/FDC 센서
  - SECS/GEM 이벤트
  - Historian(Trace data)
  - PM/WO 시스템
- zh:
  - EAP/FDC 传感
  - SECS/GEM Events
  - Historian(Trace)
  - PM/WO 系统
- en:
  - EAP/FDC sensors
  - SECS/GEM events
  - Historian (trace)
  - PM/WO system

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko:
  - 병목 설비 OEE
  - Unscheduled Down 비중
  - Reticle/Chamber 평균 큐타임
- zh:
  - 瓶颈设备 OEE
  - Unscheduled Down 占比
  - Reticle/Chamber 平均 Queue Time
- en:
  - Bottleneck OEE
  - Unscheduled down share
  - Reticle/chamber avg queue time

---

#### TRACE (priority=4)

| 항목 | 값 |
|------|----|
| label_zh | 批次追溯与Genealogy管理 |
| label_ko | Lot 추적·계보 관리 |
| label_en | Lot Trace & Genealogy |
| metrics (zh) | Lot追溯完整率, Genealogy完整率, 追溯查询时间, 记录缺失率 |
| metrics_ko | Lot 추적 완전율, Genealogy 완전율, 추적 조회 시간, 기록 누락률 |
| metrics_en | Lot trace completeness, Genealogy completeness, Trace query time, Record missing rate |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko:
  - MES (Step×Tool×Recipe 이력)
  - RTD/Dispatch 결정 로그
  - Recipe Management(레시피 ID)
  - Maskshop/Reticle 추적
- zh:
  - MES (Step×Tool×Recipe 履历)
  - RTD/Dispatch 日志
  - Recipe Management
  - Maskshop/Reticle 追溯
- en:
  - MES (Step × Tool × Recipe history)
  - RTD/dispatch decision log
  - Recipe Management
  - Maskshop/reticle trace

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko:
  - 전 공정 Lot 추적 가능 비율
  - 이상 발생 Lot의 평균 추적 시간
  - Recipe-Tool 미스매치 발생 건수
- zh:
  - 全工序 Lot 可追溯比率
  - 异常 Lot 平均追溯时间
  - Recipe-Tool 不匹配次数
- en:
  - End-to-end lot traceability ratio
  - Avg trace time for excursion lots
  - Recipe-tool mismatch incidents

---

#### PLAN_DELIVERY (priority=5)

| 항목 | 값 |
|------|----|
| label_zh | 派工调度与交期兑现 |
| label_ko | 디스패치·납기 이행 |
| label_en | Dispatch & Delivery |
| metrics (zh) | Dispatch规则执行率, Hot Lot响应率, 出货达成率, 按时交付率 |
| metrics_ko | Dispatch 룰 준수율, Hot Lot 응답률, 출하 달성률, 납기 이행률 |
| metrics_en | Dispatch rule compliance, Hot Lot response, Ship-out attainment, On-time delivery |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko:
  - APS/Scheduler
  - Dispatcher 실행 로그
  - ERP 출하/주문
  - SCM 약속 납기
- zh:
  - APS/Scheduler
  - Dispatcher 执行日志
  - ERP 出货/订单
  - SCM 承诺交期
- en:
  - APS / scheduler
  - Dispatcher execution log
  - ERP shipment / order
  - SCM commit dates

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko:
  - Dispatch 룰 위반 비율
  - Hot Lot 평균 Lead Time 단축
  - On-Time Delivery
- zh:
  - Dispatch 规则违反率
  - Hot Lot Lead Time 缩短
  - OTD
- en:
  - Dispatch rule violation %
  - Hot lot lead-time reduction
  - OTD

---

#### GLOBAL (priority=6)

| 항목 | 값 |
|------|----|
| label_zh | Fab间运营对标 |
| label_ko | 팹 간 운영 벤치마킹 |
| label_en | Cross-Fab Benchmark |
| metrics (zh) | Fab间良率差异, 产能利用率差异, 周转差异 |
| metrics_ko | 팹 간 수율 차이, 팹 간 가동률 차이, 팹 간 회전 차이 |
| metrics_en | Cross-fab yield gap, Cross-fab utilization gap, Cross-fab turn gap |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko:
  - 다공장 DataPlatform 통합 마트
  - 팹별 BI 데이터셋
  - 표준 KPI 정의 마스터
- zh:
  - 多工厂 DataPlatform 集成 Mart
  - 各 Fab BI 数据集
  - KPI 标准定义主数据
- en:
  - Multi-fab DataPlatform integrated mart
  - Per-fab BI datasets
  - Standard KPI definition master

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko:
  - Top/Bottom 팹 수율 Δ
  - Top/Bottom 팹 OEE Δ
  - 표준 KPI 정의 일치율
- zh:
  - Top/Bottom Fab Yield Δ
  - Top/Bottom Fab OEE Δ
  - KPI 定义一致率
- en:
  - Top/bottom fab yield Δ
  - Top/bottom fab OEE Δ
  - KPI definition alignment %

---

### C. 전자 조립 제조 / 电子装配制造

- 산업명 ko: ⏳
- 산업명 en: ⏳
- 정의된 role 수: **5** 개

#### PROD_OPS (priority=1)

| 항목 | 값 |
|------|----|
| label_zh | 制程达成与产线节拍 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 产量, 节拍达成率, 在制品, 工序Cycle Time |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### QUALITY (priority=2)

| 항목 | 값 |
|------|----|
| label_zh | 光学品质与外观缺陷管控 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | Yield, 光学不良率, 外观缺陷率, 直通率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### EQUIPMENT (priority=3)

| 항목 | 값 |
|------|----|
| label_zh | 设备稳定性与关键参数控制 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 设备稼动率, 停机时长, 参数偏差率, 关键工位负荷 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### ENERGY (priority=4)

| 항목 | 값 |
|------|----|
| label_zh | 能耗与公用工程监控 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 单位电耗, 峰值负载, 公辅异常次数 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### TRACE (priority=5)

| 항목 | 값 |
|------|----|
| label_zh | Panel/Lot追溯管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | Panel追溯完整率, Lot追溯完整率, 追溯查询时间 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

### D. 디스플레이·신에너지 제조 / 面板与新能源制造

- 산업명 ko: ⏳
- 산업명 en: ⏳
- 정의된 role 수: **5** 개

#### PROD_OPS (priority=1)

| 항목 | 값 |
|------|----|
| label_zh | 工艺分析与生产节拍管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 产量, 节拍达成率, 在制品, 工序Cycle Time |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### TRACE (priority=2)

| 항목 | 값 |
|------|----|
| label_zh | 全链条质量追溯 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 批次追溯完整率, 全链路追溯闭环率, 售后追溯闭环率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### EQUIPMENT (priority=3)

| 항목 | 값 |
|------|----|
| label_zh | 温控与关键设备状态管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 温控偏差, 设备稼动率, 故障预警次数, 预测性维护达成率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### LOGISTICS (priority=4)

| 항목 | 값 |
|------|----|
| label_zh | 智能仓储物流 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 库存准确率, 物流响应时间, 送料及时率, 周转天数 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### ENERGY (priority=5)

| 항목 | 값 |
|------|----|
| label_zh | 能耗与资源效率管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 单位能耗, 用电量, 用水量, 良率损失成本 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

### E. 프로세스·화학 제조 / 流程化工制造

- 산업명 ko: ⏳
- 산업명 en: ⏳
- 정의된 role 수: **6** 개

#### PROD_OPS (priority=1)

| 항목 | 값 |
|------|----|
| label_zh | 装配运营与节拍达成 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 产量, 节拍达成率, 线体Throughput, 在制品 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### QUALITY (priority=2)

| 항목 | 값 |
|------|----|
| label_zh | 全流程质量控制 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 一次通过率, 客户PPM, 不良率, 返工率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### TRACE (priority=3)

| 항목 | 값 |
|------|----|
| label_zh | 序列号追溯与全生命周期质量追溯 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 序列号追溯完整率, 全生命周期追溯完整率, 召回查询时间 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### PLAN_DELIVERY (priority=4)

| 항목 | 값 |
|------|----|
| label_zh | 交付兑现与供应协同 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 交付达成率, JIT/JIS达成率, 急单响应率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### EQUIPMENT (priority=5)

| 항목 | 값 |
|------|----|
| label_zh | 预测性维护与关键设备保障 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 设备稼动率, 故障预警率, 停机时长, MTTR |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### COST_EFF (priority=6)

| 항목 | 값 |
|------|----|
| label_zh | 成本与工位效率管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 单位成本, 工位效率, 返工损失成本, 人工效率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

### F. 소비재·식품 제조 / 消费品与食品制造

- 산업명 ko: ⏳
- 산업명 en: ⏳
- 정의된 role 수: **6** 개

#### PROD_OPS (priority=1)

| 항목 | 값 |
|------|----|
| label_zh | 元器件制程运营 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 产量, 在制品, Cycle Time, 达成率, 线体Throughput |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### QUALITY (priority=2)

| 항목 | 값 |
|------|----|
| label_zh | 批次质量与直通率管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 一次通过率, 批次不良率, 直通率, 检验合格率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### LOGISTICS (priority=3)

| 항목 | 값 |
|------|----|
| label_zh | 自动物流与线边补料管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 线边补料及时率, AGV响应时间, 库存准确率, 缺料次数 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### EQUIPMENT (priority=4)

| 항목 | 값 |
|------|----|
| label_zh | 设备稼动效率管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 设备稼动率, 停机时长, OEE, 瓶颈工位负荷 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### PLAN_DELIVERY (priority=5)

| 항목 | 값 |
|------|----|
| label_zh | 计划达成与订单响应 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 排产达成率, 工单准时完工率, 订单响应时间 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### COST_EFF (priority=6)

| 항목 | 값 |
|------|----|
| label_zh | 成本损耗与效率改善 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 单位成本, 损耗率, 人效, 改善收益率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

### G. 의약품·바이오 제조 / 制药与生物制造

- 산업명 ko: ⏳
- 산업명 en: ⏳
- 정의된 role 수: **6** 개

#### PLAN_DELIVERY (priority=1)

| 항목 | 값 |
|------|----|
| label_zh | 项目计划与交付管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 项目节点达成率, 交付准时率, 计划偏差率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### PROD_OPS (priority=2)

| 항목 | 값 |
|------|----|
| label_zh | 模块装配与工单进度管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 模块完工率, 工单进度达成率, 在制工单数 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### LOGISTICS (priority=3)

| 항목 | 값 |
|------|----|
| label_zh | 齐套与配套物流管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 齐套率, 缺件次数, 补料响应时间 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### QUALITY (priority=4)

| 항목 | 값 |
|------|----|
| label_zh | 装配质量与调试闭环 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 调试一次通过率, 不良率, 返修率, 闭环完成率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### COST_EFF (priority=5)

| 항목 | 값 |
|------|----|
| label_zh | 项目成本与人效管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 项目成本偏差, 人工效率, 返工成本 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### TRACE (priority=6)

| 항목 | 값 |
|------|----|
| label_zh | 配置追溯与BOM一致性管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | BOM一致率, 配置追溯完整率, 记录缺失率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

### H. 자동차·장비 제조 / 汽车与装备制造

- 산업명 ko: ⏳
- 산업명 en: ⏳
- 정의된 role 수: **6** 개

#### PROD_OPS (priority=1)

| 항목 | 값 |
|------|----|
| label_zh | 批次工艺与生产运行管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 批次产量, 工艺Cycle Time, 在制批次, 达成率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### QUALITY (priority=2)

| 항목 | 값 |
|------|----|
| label_zh | 质量一致性与批次追溯 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 批次合格率, 成材率, 追溯完整率, 不良率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### EQUIPMENT (priority=3)

| 항목 | 값 |
|------|----|
| label_zh | 关键设备实时监测与智能检维修 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 设备稼动率, 故障预警次数, 停机时长, 检维修达成率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### ENERGY (priority=4)

| 항목 | 값 |
|------|----|
| label_zh | 能耗实时监控 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 单位能耗, 电耗, 气耗, 峰值负载 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### IMPROVEMENT (priority=5)

| 항목 | 값 |
|------|----|
| label_zh | 异常预警与持续改善 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 异常预警次数, 响应时长, 闭环完成率, 复发率 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---

#### COST_EFF (priority=6)

| 항목 | 값 |
|------|----|
| label_zh | 成本与成材率管理 |
| label_ko | ⏳ **보완 필요** |
| label_en | ⏳ **보완 필요** |
| metrics (zh) | 单位成本, 成材率, 损耗成本, 效率改善收益 |
| metrics_ko | ⏳ **보완 필요** (zh를 한국어로 풀기) |
| metrics_en | ⏳ **보완 필요** |

**▶ data_sources (현장 데이터 소스 4~6개)**
- ko: ⏳ **보완 필요** — 어디서 데이터를 가져오는지 (예: MES, EAP, Historian, ERP 등)
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

**▶ key_kpis_top3 (현장에서 매일 봐야 하는 핵심 KPI 3개)**
- ko: ⏳ **보완 필요** — 결과 KPI(Yield/OEE)보다 "이 값이 흔들리면 큰일" 수준
- zh: ⏳ **보완 필요**
- en: ⏳ **보완 필요**

---


## 5. 작업 진행 가이드

### 5.1 보완 우선순위 제안

1. **role 라벨 ko/en** — 가장 가벼움, 화면에 즉시 노출됨 (zh → ko/en 번역)
2. **metrics ko/en** — zh → ko/en 번역
3. **data_sources_ko/zh/en** — 산업별 실제 시스템 식별 (MES/EAP/Historian/Lab Info 등)
4. **key_kpis_top3_ko/zh/en** — 도메인 전문가 협업 필요. 가장 가치 높지만 가장 무거움

### 5.2 단일 산업 채우는 데 걸리는 분량

- role 5~6개 × (label 3개 + metrics 3개 + data_sources 3개 + key_kpis_top3 3개) = **약 60~70 셀**
- B 산업(보강 완료)이 그 분량 참조 가능

### 5.3 한 산업 보강 후 반영 절차

1. `server/knowledge/step5/ch2/card6/10_card6_master.json` 의 `role_by_industry` 해당 산업 row 갱신
2. `docker compose -p diagnosis-tool -f docker-compose.yml build api && up -d` 재빌드
3. 브라우저 `Cmd+Shift+R` 강제 새로고침
4. Step1 → 해당 산업 → Step1.5 → 적당한 sub_industry → Step5 → 2.6 도메인 카드 확인

---

## 6. 부록 — role_master 코드별 의도와 활용 산업

어떤 코드를 어느 산업이 활용 중인지 매트릭스:

| role_code | A | B | C | D | E | F | G | H |
|-----------|---|---|---|---|---|---|---|---|
| `PROD_OPS` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `QUALITY` | ✓ | ✓ | ✓ | · | ✓ | ✓ | ✓ | ✓ |
| `LOGISTICS` | ✓ | · | · | ✓ | · | ✓ | ✓ | · |
| `PLAN_DELIVERY` | ✓ | ✓ | · | · | ✓ | ✓ | ✓ | · |
| `EQUIPMENT` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | ✓ |
| `COST_EFF` | · | · | · | · | ✓ | ✓ | ✓ | ✓ |
| `TRACE` | · | ✓ | ✓ | ✓ | ✓ | · | ✓ | · |
| `ENERGY` | · | · | ✓ | ✓ | · | · | · | ✓ |
| `IMPROVEMENT` | · | · | · | · | · | · | · | ✓ |
| `GLOBAL` | · | ✓ | · | · | · | · | · | · |

- ✓ = 해당 산업에서 활용 / · = 미사용

> 참고: D(디스플레이) 는 QUALITY role 미정의, A(프로젝트) 는 TRACE 미정의. 의도된 것인지 누락인지 사용자 확인 필요.