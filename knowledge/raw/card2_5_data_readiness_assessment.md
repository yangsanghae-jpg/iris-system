# Step5 CH2 Card2.5 사전 점검

목적: 기존 데이터 자산 위치/수준 확인 후, 엔진 수정 여부 판단

## 0) 점검 범위와 원칙

- 이번 점검은 **코드/엔진 수정 없이** 데이터 자산 실사만 수행했다.
- 점검 축은 3가지다.
  1. Step1 산업 데이터 (A~H)
  2. Step2 서브산업/라우팅 데이터
  3. Step4 품질 자동화 수준 데이터
- 추가로 현재 Card2 입력 실태(`keywords` 의존)를 재확인했다.

---

## 1) 현재 사용 가능한 데이터 파일 목록

- `client/src/ui/step1.js`
- `client/src/ui/step2.js`
- `client/src/ui/step4.js`
- `client/src/ui/step4_ui_v15/index.js`
- `client/src/app.js`
- `client/src/state.js`
- `client/src/data.js`
- `client/data/industry_routing_guide.json`
- `client/data/routing_industry_context_v1.json`
- `client/i18n/ko/ui.json`
- `client/i18n/ko/labels.json`
- `server/normalize.py`
- `server/diagnose_legacy.py`
- `server/assemble/compose_step5.py`
- `server/assemble/ch2_system/engine_bridge.py`
- `server/assemble/ch2_system/compose.py`
- `server/data/master/industry_master_v2.json`
- `server/data/ch1/catalogs/industry_codes.json`
- `server/data/ch1/catalogs/sub_industry_codes.json`
- `server/data/ch1/catalogs/routing_codes.json`
- `server/data/ch1/catalogs/flow_style_codes.json`
- `server/data/ch1/catalogs/control_unit_codes.json`
- `server/data/ch1/routing_profile.json`
- `server/data/ch1/industry_packs/IND_B_semiconductor.json`
- `server/data/ch1/industry_packs/IND_C_electronics_jobshop.json`
- `server/assemble/ch1_mgmt/engine.py`
- `server/data/automation_interpretation.json`
- `server/data/ch2/catalog/system_automation_scale_scores.json`
- `server/data/ch2/catalog/systems_catalog.json`
- `server/data/ch2/catalog/keywords_map.json`
- `server/data/ch2/catalog/keywords_map_merged.json`
- `server/data/ch2/README.md`

---

## 2) 축별 점검 결과

### [산업 데이터]

- 파일:
  - `client/src/ui/step1.js`
  - `client/src/data.js`
  - `server/data/ch1/catalogs/industry_codes.json`
  - `server/data/master/industry_master_v2.json`
  - `server/data/ch1/industry_packs/*.json`
- 현재 포함 정보:
  - A~H 산업 코드/라벨은 프론트와 서버 모두에 구조화되어 존재
  - `industry_master_v2`에는 산업별 `subIndustryCodes`까지 연결됨
  - Ch1 산업팩에는 산업별 priority axis, characteristic, default profile, sub profile 존재
- Card2.5 활용 가능 수준:
  - **높음 (구조화 데이터 충분)**
  - 산업코드 자체는 바로 재사용 가능
- 부족한 점:
  - Card2 현재 엔진 경로에서는 산업코드가 추천 계산 핵심축으로 쓰이지 않음(특히 non-exec)

### [서브산업 데이터]

- 파일:
  - `client/data/industry_routing_guide.json`
  - `client/src/ui/step2.js`
  - `server/data/master/industry_master_v2.json`
  - `server/data/ch1/catalogs/sub_industry_codes.json`
  - `server/data/ch1/industry_packs/*.json`
  - `server/data/ch1/routing_profile.json`
  - `server/data/ch1/catalogs/routing_codes.json`
  - `server/data/ch1/catalogs/flow_style_codes.json`
  - `server/data/ch1/catalogs/control_unit_codes.json`
- 현재 포함 정보:
  - Step2 UI에는 산업별 `recommendedRouting`, `routingDetails`, `subIndustries` 텍스트가 존재
  - 서버 쪽에는 `sub_industry_codes`, 산업팩 `sub_profiles`, routing->flow_style/control_unit 매핑 존재
  - "반도체 전공정/후공정", "전자 SMT", "배치/연속" 등 분류 힌트가 데이터로 이미 존재
- Card2.5 활용 가능 수준:
  - **중간~높음 (데이터는 풍부)**
- 부족한 점:
  - 현재 UI 상태/요청 payload에 `subIndustry`가 실리지 않음
  - `routingDetails`는 주로 설명 텍스트이며, Card2 입력용 코드형 키와 직접 연결이 약함
  - 서버 `normalize`에서 `routing/sub_industry`를 보존하지 않아 Ch2까지 전달되지 않음

### [품질 자동화 수준 데이터]

- 파일:
  - `client/src/ui/step4_ui_v15/index.js`
  - `client/i18n/ko/labels.json`
  - `client/src/app.js`
  - `server/data/automation_interpretation.json`
  - `server/data/ch2/catalog/system_automation_scale_scores.json`
  - `server/data/ch2/catalog/systems_catalog.json`
- 현재 포함 정보:
  - UI 레벨: planning/quality/equipment/logistics 4대 영역 `L0~L4` 선택 구조 존재
  - 품질 영역 라벨(`수동 검사 -> 데이터 기록 -> 온라인 모니터링 -> 예측 최적화 -> 자율 학습`)이 명시됨
  - 서버/카탈로그 레벨: `AUTO1~AIPLUS` 기반 시스템 적합도(`automation_fit`) 데이터 존재
- Card2.5 활용 가능 수준:
  - **중간 (구조는 있으나 스케일 불일치)**
- 부족한 점:
  - Step4 UI는 도메인별 `L0~L4`, Ch2 데이터는 `AUTO1~AIPLUS` 축이라 직접 매핑 규칙이 필요
  - 현재 `app.js` payload는 `STATE.automation_level`만 전송하며, v15 도메인 벡터는 `decisionStaging`에만 저장됨
  - `normalize` 결과에서 `step4_ui_v15.vector`/`quality level`은 소실됨
  - 현재 Card2 추천 경로는 품질 도메인 레벨을 실제로 쓰지 않음

---

## 3) 현재 Card2 입력 실태

### [현재 Card2 입력 실태]

- 실제 핵심 입력:
  - `keywords` (절대적)
- industry 반영 정도:
  - **낮음 (Card2 non-exec에는 사실상 미반영)**
  - `compose`에서 `industry+scale`은 exec(Card1) 후보 결정에만 직접 사용
- subIndustry 반영 정도:
  - **없음**
- quality level 반영 정도:
  - **없음(현재 Card2 추천 경로 기준)**
  - `automation_level` 단일 값은 normalize되지만 Card2 kw_map 추천에 직접 쓰이지 않음
- keywords 의존 정도:
  - **매우 높음**
  - `engine_bridge`는 kw_map hit 기반 엔진이며 hit 0이면 `NO_KW_HIT`

핵심 확인:

- 현재 Card2 추천은 `keywords -> kw_map -> by_domain` 중심이며, 산업/서브산업/품질레벨 3축은 추천 핵심축으로 연결되어 있지 않다.

---

## 4) 기존 데이터만으로 Card2.5 재구성 가능 여부

판정 기준 적용:

- 산업: 구조화 데이터 **있음**
- 서브산업: 구조화 데이터 **부분 있음** (데이터는 풍부하나 입력 파이프 미연결)
- 품질 수준: 구조화 데이터 **부분 있음** (L0~L4 vs AUTO1~AIPLUS 간 브리지 필요)

결론:

- 새 데이터팩을 처음부터 설계할 단계는 아님
- 다만 기존 데이터 "그대로"만으로는 바로 엔진 재설계가 어렵고, 최소 보강(매핑/브리지)이 선행돼야 함

---

## 5) 엔진 수정 전 선행 필요사항

1. Step2 `subIndustry`를 상태 및 payload에 코드형으로 탑재
2. Step4 domain vector(`planning/quality/equipment/logistics L0~L4`)를 서버 입력으로 전달
3. `normalize`에서 `routing/sub_industry/step4 vector`를 보존하는 context 확장
4. `L0~L4` <-> `AUTO1~AIPLUS` 매핑 테이블 정의(특히 quality 축)
5. Card2 추천 로직에서 `keywords` 단일축 외에 `industry + subIndustry + quality level` 가중 결합 규칙 정의

---

## 6) 최종 판정

### B. 일부 보강 후 엔진 수정 가능

근거:

- 산업/서브산업/품질 관련 데이터 자산은 이미 상당수 존재
- 그러나 현재 Card2 입력 경로에 3축이 직접 연결되어 있지 않음
- 최소 보강(입력 contract + 매핑 테이블) 후에는 신규 대규모 데이터팩 없이 Card2.5 진행 가능

---

## [최적 적용 판단]

1. 기존 데이터 재사용 비율: **약 70%**
2. 추가 데이터 설계 필요 범위: **입력 브리지/매핑 테이블 중심(약 30%)**
3. 엔진 수정 난이도: **중**
4. UI/출력 구조 영향 여부: **있음(입력 전달 구조는 영향, Step5 출력 스키마는 최소 영향 가능)**
5. 권장 다음 단계: **보강 데이터 정의 후 엔진 수정 진행**

