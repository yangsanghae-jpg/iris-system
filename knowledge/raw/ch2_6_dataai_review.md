# Ch2.6 Data/AI 도메인 리뷰 — 현재 상태와 개선 방향

> 작성: 2026-06-05
> 대상: Step5 Ch2 / 6번째 도메인(dataai), 화면 표시 + 데이터 마스터 + 빌더 로직 전반

---

## 1. 결론 요약

지금 화면이 **단편적으로 느껴지는 이유는 두 갈래**입니다.

1. **마스터 데이터 자체의 깊이가 부족** — `10_card6_master.json` 의 role/capability 모두 zh 텍스트만 있고, 산업·규모별 차이가 metric 키워드 몇 개로 표현됨. AI/데이터 도메인의 핵심인 **데이터 흐름·자산·성숙도 모델·실제 시스템 토폴로지**가 들어있지 않음.
2. **다른 5개 도메인 대비 카드 종류가 줄어듦** — Ch2.6 빌더가 의도적으로 `iface` 카드를 제거(role + cap 2장)하고, role 카드는 metric 리스트만 보여줌. 나머지 도메인은 `role / cap / iface` 3장 + 각 카드 안의 capabilities·objects·interfaces·maturity 필드가 채워져 있어 정보 밀도 차이가 크게 보임.

→ 개선은 ① **마스터 보강** ② **카드 구조 통일(또는 dataai 만의 고유 구조 정식화)** 두 축으로 갑니다.

---

## 2. 현재 상태 진단

### 2.1 데이터 위치

| 파일 | 역할 | 현재 깊이 |
|------|------|-----------|
| [server/data/ch2/catalog/domain_cards_catalog.json](../../server/data/ch2/catalog/domain_cards_catalog.json) `domains.dataai` | 6 도메인 공통 카드 카탈로그의 dataai 기본값 (variants.default) | role/cap/iface 3장, 각 5필드(role/purpose/capabilities/objects/interfaces/maturity) — 다른 5개 도메인과 거의 동일 분량 (≈1,000자) |
| [server/knowledge/step5/ch2/card6/10_card6_master.json](../../server/knowledge/step5/ch2/card6/10_card6_master.json) | dataai 전용 마스터 (산업×규모 매트릭스) | role_master 10개, role_by_industry 8 산업×5~6 role(metric 리스트만), capabilities 4 scale(systems 1~2개+display_traits 3개+management_focus 4개) — 모두 zh 만 |
| [server/assemble/ch2_system/compose.py](../../server/assemble/ch2_system/compose.py) `_apply_card6_dataai_overrides` | 위 마스터를 industry+scale 로 룩업해서 카드 구조 재구성 | role 카드: card6_role 타입(items[].role_code/label_zh/priority/metrics) / cap 카드: card6_capability 타입 / **iface 카드 강제 제거** |
| [client/src/ui/step5/step5_ch2_card6_renderer.js](../../client/src/ui/step5/step5_ch2_card6_renderer.js) | card6_role/card6_capability 타입 전용 렌더러 | role 항목 = label + metric chip 행 / cap = label + summary + traits chip + focus bullet + 포함 scale chip |

### 2.2 화면 비교 (B/L 규모 케이스)

다른 도메인은 1 카드당 다음을 표시:
- **role**: 한 단락 책임 설명 + capabilities(5~6개) + objects(4~5개) + interfaces(1~2문장) + maturity(1~2문장)
- **cap**: 산업·규모 맥락 한 줄 + capabilities + objects + interfaces + maturity
- **iface**: interfaces 문장

dataai는:
- **role(card6_role)**: 산업별 5~6개 metric 카테고리 + 각 카테고리에 metric 키워드 3~5개. 한 줄 설명·접속 시스템·성숙도 단계가 없음.
- **cap(card6_capability)**: 규모(S1~S4)별 1줄 summary + display_traits 3개 + management_focus 4개 + 포함 scale 칩. 산업 차이 미반영.
- **iface**: 없음(제거됨).

→ **눈에 보이는 정보량**: 다른 도메인 ≈ 30~40 항목, dataai ≈ 15~20 항목 (즉 절반).

### 2.3 본질적 약점 4가지

1. **데이터 흐름·아키텍처 부재**  
   AI/데이터 도메인의 본질인 "어디서(OT/IT) → 어디로(Lake/DWH/Mart) → 어떻게(Pipeline/Quality/Lineage) → 무엇이 나오는가(Mart/Feature Store/Model)" 가 표시되지 않음. 다른 도메인은 interfaces 필드에 인풋·아웃풋이 한 줄로라도 적혀 있는데, dataai 만 iface 가 제거되어 더 부족하게 느껴짐.

2. **성숙도 모델(L1~L4)이 표지판만 있고 본문이 없음**  
   role 카드 purpose 줄에 "Data Maturity L1~L4" 라는 표현만 있고, 각 단계가 무엇을 의미하는지(L1 정형 보고서 → L2 셀프 BI → L3 데이터 플랫폼/시계열 → L4 산업 AI/자율 폐루프) 가 어디에도 정의되지 않음. 그래서 사용자가 "지금 우리는 어디 있고 다음은 어디인가" 를 판단할 수 없음.

3. **role_code 의 산업 매핑이 표면적**  
   - `PROD_OPS / QUALITY / EQUIPMENT / TRACE / PLAN_DELIVERY / COST_EFF / ENERGY / IMPROVEMENT / GLOBAL` 10가지 코드 자체는 좋은 분류이지만, 산업별로는 **이름과 metric 키워드만 살짝 갈아 끼움**. 예: B/QUALITY = "양품률·결함·재작업" / C/QUALITY = "광학 양품률·외관 결함" / D/QUALITY = (정의 없음). 산업 고유 "데이터 모델/지표 정의/소스 시스템"이 빠짐.
   - D, G 등은 일부 산업에서 QUALITY role 자체가 누락 (D=5 role 모두 운영·이력·설비·물류·에너지로 구성, QUALITY 없음). 이건 의도된 누락인지 빠진 건지 불명.

4. **system 추천이 너무 적음**  
   S1 = ERP/MES/Basic Report (3), S2 = Professional Report + Specialized Kanban (2), S3 = BI + DT (2), S4 = Global IMC + AI Knowledge Warehouse (2). 다른 도메인의 `top_overall` 시스템 추천은 보통 8~12개. dataai 도메인이 추천하는 시스템도 카탈로그(systems_catalog.json) 에는 **DataPlatform, Historian, BI, MES↔DataPlatform 인터페이스** 등 풍부하지만 card6_capability.systems 는 짧은 라벨 2~3개만 노출.

---

## 3. 개선 방안 (3 옵션)

### 옵션 A — 마스터 데이터만 보강 (작업량 ★)

`10_card6_master.json` 의 기존 스키마를 유지하면서 채움.

추가/보강:
- `role_master` 각 role 에 `summary_ko/zh/en` 1~2문장 (코드만 있고 의미 설명 없음 해소)
- `role_by_industry` 각 row 에 `data_sources_ko/zh/en`(주요 데이터 출처: ERP/MES/EAP/Historian/Vision 등), `key_kpis_ko/zh/en`(현장에서 매일 보는 KPI)
- `capabilities` 각 scale 에 `systems_detail_ko/zh/en`(시스템별 짧은 설명), `architecture_ko/zh/en`(데이터 흐름 한 문장: "EAP/MES → Historian → Data Lake → BI/Mart")
- 신규 `maturity_levels` 절: L1~L4 각 단계 정의 (각 ~3문장 ko/zh/en)

장점: 빌더/렌더러 변경 최소, 화면 정보량 ~2배.  
단점: 카드 구조(role/cap 2장)는 그대로라 다른 도메인과 모양 불일치 남음.

### 옵션 B — A + 카드 추가 (작업량 ★★)

A 위에 카드를 한두 장 추가:
- **maturity 카드** — L1~L4 정의 + 현재 산업·규모 추천 단계 표기
- **architecture 카드** — 데이터 흐름 텍스트 다이어그램 (예: OT/IT 소스 → 통합 → 저장 → 분석/서비스)
- 또는 다른 5개 도메인처럼 **iface 카드 복원** (입·출 시스템 표)

장점: 다른 도메인과 외형 통일, 정보 더 구조화.  
단점: 빌더의 `_apply_card6_dataai_overrides` 손봐야 함 (iface.pop 제거 + 신규 카드 빌더 추가), 렌더러도 신규 카드 타입 지원.

### 옵션 C — Step5/Ch2.6 의 정체성 재정의 (작업량 ★★★, 권장 검토)

지금 dataai 가 "기타 시스템 카탈로그를 한 줌 뿌리는 자리" 처럼 보입니다. 사실 **데이터/AI 도메인은 다른 5개 도메인을 **횡단**하는 인프라**라서, 같은 형태로 5개를 옆에 늘어놓는 게 잘 안 맞습니다.

대안 구조 (3 카드):
1. **데이터 자산** — 무엇을 (사실/지표/시계열/특징/모델/규칙), 어디서 (소스 시스템 5~7), 어떻게 (수집 주기·이력)
2. **분석/AI 능력** — 4단계 maturity (보고 → BI → 플랫폼 → AI), 산업·규모별 권장 단계, 권장 시스템 셋
3. **거버넌스·운영** — 마스터데이터, 권한·감사, 데이터 품질 KPI, 모델 라이프사이클

이 정체성이 잡히면 마스터 JSON 스키마를 재설계하고, 빌더와 렌더러도 같이 갱신.

장점: dataai 가 "데이터·AI 도메인" 으로 자기 자리를 가짐. 다른 도메인 사용자가 봐도 "여기서 뭘 봐야 하는지" 명확.  
단점: 작업이 가장 큼. 기존 운영 데이터 호환 필요.

---

## 4. 추천 진행 순서

1. **결정**: A / B / C 중 어느 정도까지 갈지 선택 — 권장은 **B (정식 통일) + A 마스터 보강 동시**.
2. **마스터 보강** (`10_card6_master.json` ko/zh/en 평행화 + 산업×규모 매트릭스에 데이터소스·KPI·시스템 디테일 + maturity_levels 절 신설)
3. **빌더**: `_apply_card6_dataai_overrides` 에 iface 카드 복원 + maturity 카드 신규 빌더 추가
4. **렌더러**: `step5_ch2_card6_renderer.js` 에 새 카드 타입 핸들러
5. **i18n**: ko/zh/en 키 (현재 zh 만)
6. **문서**: 03_ui_structure.md / 05_data_structure.md 의 Ch2.6 섹션 갱신
7. **버전**: V2.3 → V2.4

---

## 5. 결정해주실 것

- **A / B / C 중 어느 옵션** 으로 갈지
- **마스터 보강 범위**: (a) zh+ko+en 평행화까지, (b) 데이터소스·KPI 보강까지, (c) maturity 모델 신설까지, 어디까지 진행할지
- **카드 구조 변경 허용** 여부 (B/C 선택 시 빌더·렌더러 손대야 함)
- (선택) **샘플 산업** 1~2개로 시범 적용 후 점진 확장할지, 한 번에 전체 8 산업 보강할지

이 4개에 답 주시면 작업 들어가겠습니다.
