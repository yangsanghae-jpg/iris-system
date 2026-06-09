# Card1 생산실행 카드 산업별 평가 (Step C)

## 1) 목적

본 평가는 Card1이 Chapter2의 6개 카드 중 **생산실행 전용 카드**라는 전제를 명시적으로 채택한다.  
따라서 평가지점은 "왜 품질/물류/설비/지표가 적게 보이느냐"가 아니라, **생산실행 범위 안에서 산업별 실행 구조가 얼마나 정확하게 표현되는가**에 둔다.

참고 입력:
- [Card1 Exec 구조 분석 (Step A)](docs/card1_exec_structure_analysis.md)
- [Card1 Exec Industry Snapshots (Step B)](docs/card1_exec_industry_snapshots.md)

## 2) 평가 기준 (4축)

- **A. 카드 범위 적합성**: Card1이 생산실행 범위를 벗어나지 않는가
- **B. 산업 실행 특성 반영**: 산업별 실행 방식(LOT, Batch, 라인/시퀀스 등)이 role/cap/iface에 드러나는가
- **C. 카드 내부 일관성**: role / cap / iface가 같은 실행 구조를 설명하는가
- **D. 표현력 수준**: candidate는 맞더라도 최종 설명이 과도하게 generic으로 수렴하지 않는가

판정 레벨:
- **OK**: 범위를 지키면서 산업 특성이 role/cap/iface 전반에 명확함
- **WEAK**: 범위는 맞지만 산업 특화가 iface 편중이거나 role/cap가 generic 경향
- **NG**: 산업 실행 구조 자체가 맞지 않거나 role/cap/iface가 상호 불일치

## 3) 8대 산업 평가 매트릭스

| 산업 | 생산실행 기대 구조 | 실제 후보 | 실제 표현 요약 | 판정 | 문제 유형 | 개선 포인트 |
|---|---|---|---|---|---|---|
| A 프로젝트·특수제조 | 주문/프로젝트 단위, BOM/변경 반영, 공정별 지시·진도 | MES, SFC, LINE_EXEC, DISPATCH | 생산실행 범위는 적합하나 프로젝트 단위/변경반영 표현이 약하고 MES 공통 서술 비중 큼 | WEAK | 생산실행 범위는 적절하나 산업 특화 약함 | role/cap에 프로젝트 오더, ECO 반영 실행, 공정 진도 통제 문구 보강 |
| B 반도체 | LOT, Route/Recipe, Hold/Rework, Genealogy, 재진입 | MES, DISPATCH, TRACE_EXEC, ROUTE_EXEC | 후보와 iface에 Recipe/Genealogy가 드러나며 추적/라우트 축도 존재, 다만 role/cap은 MES 중심 문구 강함 | WEAK | iface 편중형 산업 표현 | role/cap에 LOT 분기, hold/release, rework loop를 명시 |
| C 전자·정밀 | 라인+공정 혼합, SMT/AOI/SPI, SFC/Board/Panel 추적 | MES, SFC, LINE_EXEC, TRACE_EXEC | 라인/SFC 후보와 SMT/AOI/SPI 인터페이스가 맞물려 실행 맥락이 비교적 선명함 | OK | candidate는 적절하나 role/cap 표현 약함(경미) | role/cap에 공정전환(setup/changeover)과 Board/Panel 추적 단위를 추가 |
| D 면판·신에너지 | 라인 흐름, 구간 연속성/병목, 설비연동, throughput | MES, TRACE_EXEC, ROUTE_EXEC, DISPATCH | 후보는 실행형이나 라인 흐름/병목 제어 서술이 약하고 generic MES에 수렴 | WEAK | catalog/detail 부족으로 generic 수렴 | throughput, bottleneck 구간 제어, 연속공정 동기화 표현을 role/cap에 반영 |
| E 화학 | Batch/Recipe 단계 실행, 투입/혼합/반응/배출 단계관리 | MES, SFC, TRACE_EXEC, LINE_EXEC | iface에 Recipe/Batch record가 있으나 후보와 role/cap이 배치 단계 제어를 충분히 반영하지 못함 | WEAK | 산업 실행 구조와 부분 불일치 | BATCH_EXEC 계열 후보/표현을 강화하고 공정단계 제어(cap)를 명시 |
| F 소비재·식품 | SKU/LOT, 포장/배치/유통기한, 배치+라인 혼합 | MES, BATCH_EXEC, ROUTE_EXEC | BATCH_EXEC가 포함되어 방향성은 맞고 배치 실행 맥락 존재, 다만 SKU/유통기한/포장 실행 통제가 약함 | WEAK | candidate는 적절하나 role/cap 표현 약함 | role/cap에 SKU 전환, 포장라인 동기, shelf-life 제약 실행 로직 보강 |
| G 제약·바이오 | Batch 실행, EBR/전자기록/전자서명, 규제준수 실행 | MES, BATCH_EXEC, EBR, TRACE_EXEC | 배치+EBR+추적 조합이 명확하고 iface에도 QMS/LIMS/EBR 연계가 반영되어 일관성 높음 | OK | 없음(강점형) | role/cap에 예외처리(Deviation/CAPA 트리거)와 릴리즈 게이트를 추가하면 완성도 상승 |
| H 자동차 | 라인/시퀀스 조립, 모델/옵션별 지시, JIT/JIS 연계 | MES, SFC, LINE_EXEC, WO_EXEC | 라인 실행 후보는 있으나 실제 표현이 전자형(SMT/AOI/SPI) iface로 기울어 자동차 시퀀스/JIT 맥락이 약함 | WEAK | 산업 실행 구조와 부분 불일치 | iface와 cap을 모델/옵션 시퀀스, JIT/JIS 연동, VIN/sequence 기준으로 재정렬 |

## 4) 산업별 상세 평가

### A 프로젝트·특수제조
- 기대 생산실행 구조: 프로젝트/주문 단위 실행, BOM/설계변경 반영, 공정진도 관리
- 실제 스냅샷 핵심: `MES + SFC + LINE_EXEC + DISPATCH`로 실행 범위는 적절하나 설명은 공통 MES 실행에 가깝다.
- 판정 근거: **WEAK**. 범위 적합성은 높지만 프로젝트형 실행 특성이 role/cap에서 희석됨.
- 문제 유형: 생산실행 범위는 적절하나 산업 특화 약함
- 개선 포인트: role/cap에 프로젝트 WBS 단위 지시, ECO 반영 타이밍, 공정진도 마일스톤 제어를 추가

### B 반도체
- 기대 생산실행 구조: LOT, Route/Recipe, Hold/Rework, Genealogy, 재진입 실행
- 실제 스냅샷 핵심: `TRACE_EXEC + ROUTE_EXEC`와 Recipe/Genealogy iface는 적절하나 role/cap은 MES 범용 문구가 중심.
- 판정 근거: **WEAK**. 산업 신호는 존재하지만 iface에 비해 role/cap 구체도가 낮다.
- 문제 유형: iface 편중형 산업 표현
- 개선 포인트: role/cap에 lot split/merge, hold/release, rework re-entry를 명시

### C 전자·정밀
- 기대 생산실행 구조: 라인/공정 혼합, SMT/AOI/SPI 연계, SFC/Board/Panel 추적
- 실제 스냅샷 핵심: `SFC + LINE_EXEC + TRACE_EXEC`, iface의 SMT/AOI/SPI가 실행 구조와 정합.
- 판정 근거: **OK**. 범위와 산업성, 내부 일관성이 상대적으로 가장 안정적이다.
- 문제 유형: candidate는 적절하나 role/cap 표현 약함(경미)
- 개선 포인트: 공정전환시간, feeder/setup change, board-panel 계층 추적을 cap에 명문화

### D 면판·신에너지
- 기대 생산실행 구조: 연속 라인 흐름, 병목 구간 제어, 설비 연동, throughput 중심
- 실제 스냅샷 핵심: `TRACE_EXEC + ROUTE_EXEC + DISPATCH`는 있으나 라인 흐름 제어의 명시성이 낮다.
- 판정 근거: **WEAK**. 생산실행 카드 범위는 지키지만 산업의 핵심 실행 메커니즘(흐름/병목)이 약하다.
- 문제 유형: catalog/detail 부족으로 generic 수렴
- 개선 포인트: 구간별 takt, bottleneck alert, 연속공정 handoff 상태를 role/cap에 반영

### E 화학
- 기대 생산실행 구조: Batch/Recipe 단계 제어, 투입/혼합/반응/배출 실행관리
- 실제 스냅샷 핵심: iface는 Recipe/Batch record를 언급하나 후보는 `SFC/LINE_EXEC` 중심으로 배치 단계성이 약함.
- 판정 근거: **WEAK**. 산업 실행 구조와 부분 불일치가 존재한다.
- 문제 유형: 산업 실행 구조와 부분 불일치
- 개선 포인트: BATCH_EXEC 또는 단계 실행 엔진 축을 후보/role/cap에 명확히 반영

### F 소비재·식품
- 기대 생산실행 구조: SKU/LOT 기반, 포장/배치/유통기한 제약, 배치+라인 혼합
- 실제 스냅샷 핵심: `BATCH_EXEC` 포함으로 방향은 맞지만 SKU/유통기한/포장 동기화 실행 표현은 약함.
- 판정 근거: **WEAK**. 후보 적합성은 높으나 role/cap 설명력이 부족하다.
- 문제 유형: candidate는 적절하나 role/cap 표현 약함
- 개선 포인트: SKU changeover, shelf-life gate, packaging line sync를 cap/iface에 구체화

### G 제약·바이오
- 기대 생산실행 구조: Batch 실행, EBR/전자서명/감사추적 연계, 규제준수 통제
- 실제 스냅샷 핵심: `BATCH_EXEC + EBR + TRACE_EXEC` 조합과 QMS/LIMS/EBR iface가 함께 나타남.
- 판정 근거: **OK**. Card1 범위 안에서 산업 특화와 내부 일관성이 모두 높다.
- 문제 유형: 생산실행 범위 적합 + 산업성 표현 양호
- 개선 포인트: 예외처리 워크플로(Deviation/CAPA 연동)까지 표현되면 규제형 실행 완성도 상승

### H 자동차
- 기대 생산실행 구조: 라인/시퀀스 조립, 모델/옵션별 지시, JIT/JIS 연계
- 실제 스냅샷 핵심: `LINE_EXEC + WO_EXEC` 후보는 맞지만 iface가 SMT/AOI/SPI 중심으로 자동차 문맥과 어긋남.
- 판정 근거: **WEAK**. 후보는 적절하나 최종 표현이 산업 실행 구조를 충분히 설명하지 못한다.
- 문제 유형: 산업 실행 구조와 부분 불일치
- 개선 포인트: VIN/시퀀스, 모델-옵션 BOM, JIT/JIS 연계 이벤트를 role/cap/iface에 반영

## 5) 총평

- Card1은 전반적으로 **생산실행 카드 범위**를 잘 지키고 있으며, 범위 일탈 문제는 크지 않다.
- 산업 적합도가 비교적 높은 축은 **C(전자·정밀), G(제약·바이오)**다.
- **B, E, H**는 산업성이 주로 iface 또는 일부 후보에만 나타나며 role/cap의 산업별 실행 문맥이 약하다.
- **A, D, F**는 candidate 방향은 맞지만 detail 부족으로 generic MES 서술로 수렴하는 경향이 크다.
- 결론적으로 Step C의 핵심 이슈는 "Card1의 MES 중심성 자체"가 아니라, **생산실행 범위 내에서 role/cap의 산업별 실행 문법을 얼마나 구체화하느냐**다.
