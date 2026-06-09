# Card1 Exec 구조 분석 (Step A)

범위 제한:
- `server/data/ch2/catalog/execution_candidate_master_v1_52.json`
- `server/data/ch2/catalog/execution_industry_features.json`
- `server/data/ch2/catalog/systems_catalog.json`
- `server/assemble/ch2_system/engine_bridge.py`

금지 준수:
- API 호출 없음
- 코드 수정 없음
- 전체 repo 탐색 없음

## 1) Candidate 구조 요약

- `execution_candidate_master_v1_52.json`에 `industry_scale_master`가 존재하며, `A~H × S1~S4` 조합별 후보가 별도로 정의되어 있음.
- `engine_bridge.py`의 `get_execution_candidates_for_card1_with_meta()`는 우선 `industry_scale_master[industry][scale]`를 조회하고, 미스 시 `industry_master[industry].core`로 fallback함.
- 즉 구조는 **scale 중심만이 아니라 industry+scale 결합 구조**다.
- 다만 패턴상 공통 경향이 강함:
  - S1/S2: MES 계열 + 현장 실행 시스템
  - S3: `EXEC_MGMT` 중심 강화
  - S4: `GLOBAL_MES` 중심 강화
- 결론: 후보 테이블 자체는 산업 분화가 존재하나, 상위 스케일(S3/S4)에서는 산업 간 수렴 경향이 큼.

## 2) Overlay 분석

- `execution_industry_features.json`에 A~H별 `execution_features`가 명확히 분리되어 있음.
- 샘플 확인:
  - B(반도체): `lot_tracking`, `recipe_control`, `equipment_integration`, `wip_dispatch`
  - C(전자/SMT): `line_execution`, `feeder_setup`, `component_traceability`
  - D(디스플레이/배터리): `panel_tracking`, `equipment_integration`, `yield_management`
- `engine_bridge.py`는 overlay를 직접 사용하지 않고, 후보 선택만 담당.
- Overlay는 compose 레벨에서 활용되는 구조(후보 선정 로직과는 분리).
- 결론: 산업 특화 정의는 존재하나, 후보 선택의 1차 결정은 candidate master가 담당하고 overlay는 2차 보강 성격.

## 3) Systems Catalog 분석

- `systems_catalog.json`의 `systems`에 실행 카드 핵심 시스템 다수 존재:
  - `BATCH_EXEC` 존재
  - `LINE_EXEC` 존재
  - `EBR` 존재
  - `GLOBAL_MES`는 **해당 파일에 미정의** (실행 후보에는 있으나 catalog 상세는 누락 가능성)
  - `EXEC_MGMT`도 본 catalog에서는 직접 정의 확인 어려움(동일 리스크)
- `MES`, `TRACEABILITY`, `EAP`, `QMS`, `WMS` 등은 상세 정의가 풍부함.
- 결론: 산업 표현 잠재력은 있으나, Card1 상위 스케일 핵심 코드(`GLOBAL_MES`, `EXEC_MGMT`)의 catalog 상세 부재 시 카드 표현이 generic fallback으로 수렴할 여지가 큼.

## 4) 핵심 결론 (5줄)

- Candidate는 industry+scale 분화 구조이며, 단순 scale-only 구조는 아니다.
- 상위 스케일(S3/S4)로 갈수록 후보 패턴은 산업 간 유사해지는 경향이 있다.
- Overlay 데이터는 산업별로 존재하며(B/C/D 포함) 산업 특화 단서도 충분하다.
- 다만 overlay는 후보 선정 1차 로직이 아니라 후속 보강 경로라 영향력이 제한될 수 있다.
- systems catalog에서 일부 상위 코드 상세 누락 시 결과가 generic MES 중심으로 보일 구조적 가능성이 있다.
