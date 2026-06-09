# Step5 CH2 Card2.5 매핑 테이블 설계 스펙

목적: Card2.5 엔진 수정 전에 필요한 최소 보강 데이터(브리지 JSON)의 설계 원칙과 범위를 확정한다.

관련 브리지 파일:

- [subindustry_bridge_v1_7.json](server/data/ch2/card2/subindustry_bridge_v1_7.json)
- [quality_level_mapping_v1_7.json](server/data/ch2/card2/quality_level_mapping_v1_7.json)

## 1) subIndustry 브리지 정의 원칙

- 코드형 키 사용:
  - 예: `semiconductor_frontend`, `electronics_smt_highmix`
  - UI 텍스트가 아닌 엔진 입력용 stable key로 관리
- 산업별 네임스페이스 분리:
  - 상위 키를 산업코드(`B`, `C`)로 분리해 중복/충돌 방지
- 최소 속성 세트만 유지:
  - `label`
  - `quality_profile`
  - `equip_profile`
  - `traceability`
  - 필요 시 `routing_hint`/`source_codes` 추가
- 확장 가능하지만 과설계 금지:
  - v1.7은 B/C 우선
  - A~H 일괄 완성보다 contract 안정성을 우선

## 2) quality level 매핑 원칙

- 단일 축:
  - `L0~L4 -> automation_stage(AUTO1~AIPLUS) -> recommended_quality_systems`
- quality 시스템만 포함:
  - `QMS`, `SPC`, `FDC`, `APC` 중심
  - planning/equipment/logistics 시스템은 제외
- 점진적 누적 원칙:
  - 낮은 레벨은 기본 품질 시스템
  - 높은 레벨은 분석/고도화 시스템을 누적
- 기존 카탈로그 코드와 충돌 금지:
  - `systems_catalog` 기준 코드를 우선 사용
  - 코드 별칭은 추후 별도 alias 테이블로 관리

## 3) 재사용 원칙

- 우선 재사용 대상:
  - `industry_master_v2` (산업/서브산업 코드 체계)
  - `sub_industry_codes` (서브산업 레이블)
  - `automation_interpretation` (자동화 단계 의미)
  - `systems_catalog` (시스템 코드/설명)
- 신규 파일 역할 제한:
  - 신규 브리지 파일은 "연결 계층"만 담당
  - 기존 카탈로그를 대체하지 않음

## 4) 브리지 테이블 계약 요약

### 4-1. subindustry_bridge_v1_7

- 상위:
  - `version`, `owner`, `scope`, `industries`
- 산업별:
  - `sub_industries` 객체
- subIndustry 항목:
  - `label`
  - `source_codes`
  - `routing_hint`
  - `quality_profile`
  - `equip_profile`
  - `traceability`

### 4-2. quality_level_mapping_v1_7

- 상위:
  - `version`, `owner`, `scope`, `levels`
- 레벨별(`L0~L4`) 항목:
  - `automation_stage`
  - `recommended_quality_systems`
  - `selection_intent`

## 5) 적용 경계

- 이번 단계는 데이터 정의까지만 수행
- 엔진/compose/UI 기능 코드는 변경하지 않음
- 다음 단계(Card2.5 엔진 수정)에서만 브리지 연결 및 가중 로직 반영
