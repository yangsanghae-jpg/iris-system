# Step5 CH2 Card2.5 입력 브리지 설계

목적: Card2.5 엔진 수정 전에 `industry + sub_industry + quality_level` 3축 입력이 Ch2 엔진 입력까지 전달되도록 최소 브리지 계약을 확정한다.

## 1) 현재 입력 끊김 지점

### 1-1. Step2 subIndustry

- 현황:
  - `client/data/industry_routing_guide.json`에는 산업별 `routingDetails`/`subIndustries`가 존재한다.
  - `client/src/ui/step2.js`에서 `subIndustries`는 추천 안내 텍스트로만 표시된다.
- 끊김:
  - `client/src/state.js`에 `sub_industry` 저장 필드가 없다.
  - `client/src/app.js` `buildPayload()`에 `sub_industry`가 없다.
  - `server/normalize.py`는 `sub_industry`를 normalize 결과에 보존하지 않는다.
  - 결과적으로 Ch2 입력(`ctx`)에 subIndustry가 전달되지 않는다.

### 1-2. Step4 품질 level

- 현황:
  - `client/src/ui/step4_ui_v15/index.js`에서 도메인별 `L0~L4` 벡터(`planning/quality/equipment/logistics`)를 관리한다.
  - `client/i18n/ko/labels.json`에 `step4.domain_level_labels.quality.L0~L4`가 정의되어 있다.
- 끊김:
  - `client/src/app.js`는 `STATE.automation_level`만 payload로 전송하고, `step4_ui_v15.vector`는 전송하지 않는다.
  - `server/normalize.py`는 `automation_level`만 normalize하고 quality 도메인 level은 보존하지 않는다.
  - 결과적으로 Ch2 입력에 `quality_level`이 없다.

---

## 2) 목표 입력 계약 (Card2.5)

Card2.5가 최종적으로 사용해야 하는 최소 계약:

```json
{
  "industry": "B",
  "sub_industry": "semiconductor_frontend",
  "quality_level": "L3"
}
```

세부 규칙:

- `industry`: `A~H`
- `sub_industry`: `subindustry_bridge_v1_7.json`에서 정의한 코드형 키
- `quality_level`: `L0~L4`

---

## 3) 단계별 전달 경로

### 3-1. UI state

- 소스:
  - Step2: routing 선택과 함께 subIndustry 코드 선택/확정
  - Step4: `step4_ui_v15.vector.quality`
- 목표 상태:
  - `STATE.sub_industry` (신규)
  - `STATE.quality_level` 또는 `STATE.step4_vector.quality`에서 추출

### 3-2. app payload

- 소스: `client/src/app.js` `buildPayload()`
- 목표 payload 확장:
  - `sub_industry`
  - `quality_level`

### 3-3. server normalize

- 소스: `server/normalize.py`
- 목표 normalize 확장:
  - `sub_industry`를 유효값 검증 후 `normalized`에 보존
  - `quality_level` (`L0~L4`) 보존
  - 기존 `automation_level`은 유지

### 3-4. ch2 engine input

- 소스: `server/assemble/compose_step5.py` -> `build_ch2_engine_from_kw_map(ctx, ...)`
- 목표:
  - `ctx`에 `sub_industry`, `quality_level` 포함
  - Card2.5 로직에서 `keywords`와 함께 가중 결합 입력으로 사용

---

## 4) 수정 필요 지점 목록 (이번 단계는 수정하지 않음)

- `client/src/state.js`
  - `sub_industry`, `quality_level`(또는 equivalent field) 저장 필드 추가 필요
- `client/src/ui/step2.js`
  - 추천 텍스트용 subIndustry를 코드형 선택값으로 확정/저장하는 지점 필요
- `client/src/app.js`
  - `buildPayload()`에 `sub_industry`, `quality_level` 전송 추가 필요
- `server/normalize.py`
  - `sub_industry`, `quality_level` 보존 및 기초 검증 추가 필요
- `server/assemble/compose_step5.py`
  - Ch2 입력 ctx 전달값에 신규 필드 포함 여부 점검 필요
- `server/assemble/ch2_system/engine_bridge.py`
  - Card2.5 단계에서 신규 브리지 입력을 가중치 계산에 반영하는 지점 필요

---

## 5) 적용 방향 요약

- 대형 신규 데이터팩 설계 없이 기존 데이터 재사용 우선
- 신규는 브리지 2종으로 제한:
  - [subindustry_bridge_v1_7.json](server/data/ch2/card2/subindustry_bridge_v1_7.json)
  - [quality_level_mapping_v1_7.json](server/data/ch2/card2/quality_level_mapping_v1_7.json)
- Ch2 출력 스키마(`domain_cards`, `recommended_systems`, `role/cap/iface`)는 변경하지 않는다.
