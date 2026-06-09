# Step5 CH2 Card2 산업별 스냅샷 (Step B)

## 1) 목적

Card2를 Card1과 동일 프레임으로 검증하기 위해, A~H 산업에서 실제 추천 출력을 동일 조건으로 수집한다.  
이번 문서의 범위는 Card2이므로 `exec`(Execution)는 제외하고 본다.

## 2) 고정 테스트 조건

- `industry`: `A~H` 전수
- `scale`: `S3` (입력은 `L/L/L`로 동일, 내부 정규화 `S3`)
- `automation_level`: `L3`
- `keywords`:
  - `[EAP, FDC, SPC, APS, WMS, BI]`

이유:

- Card2는 `keywords`가 없으면 `NO_KW_HIT`로 비어 버리는 특성이 있어, 키워드 고정이 필수다.

## 3) 산업별 요약 (Execution 제외)

### Industry A

- equip: `[Analytics, EAP, FDC]`
- quality: `[Analytics, FDC, QMS]`
- planning: `[APS]`
- logistics: `[WMS]`
- dataai: `[Analytics, FDC, QMS]`
- 빈 도메인: 없음
- 이상 매핑:
  - `Analytics`가 `equip/quality`에 동시에 등장
  - `FDC`가 `dataai`와 `quality`에 동시 노출

### Industry B (Semiconductor)

- equip: `[Analytics, EAP, FDC]`
- quality: `[Analytics, FDC, QMS]`
- planning: `[APS]`
- logistics: `[WMS]`
- dataai: `[Analytics, FDC, QMS]`
- 빈 도메인: 없음
- 이상 매핑:
  - 반도체 산업임에도 A와 동일한 도메인 분포/코드 집합
  - `Analytics` 다중 도메인 반복 노출

### Industry C

- equip: `[Analytics, EAP, FDC]`
- quality: `[Analytics, FDC, QMS]`
- planning: `[APS]`
- logistics: `[WMS]`
- dataai: `[Analytics, FDC, QMS]`
- 빈 도메인: 없음
- 이상 매핑:
  - C 산업 고유 특징 없이 A/B와 동일 결과

### Industry D

- equip: `[Analytics, EAP, FDC]`
- quality: `[Analytics, FDC, QMS]`
- planning: `[APS]`
- logistics: `[WMS]`
- dataai: `[Analytics, FDC, QMS]`
- 빈 도메인: 없음
- 이상 매핑:
  - 도메인 편차가 거의 없고 산업별 차등 신호 부재

### Industry E

- equip: `[Analytics, EAP, FDC]`
- quality: `[Analytics, FDC, QMS]`
- planning: `[APS]`
- logistics: `[WMS]`
- dataai: `[Analytics, FDC, QMS]`
- 빈 도메인: 없음
- 이상 매핑:
  - 화학/공정형 특화 후보보다 공통 키워드 계열이 우세

### Industry F

- equip: `[Analytics, EAP, FDC]`
- quality: `[Analytics, FDC, QMS]`
- planning: `[APS]`
- logistics: `[WMS]`
- dataai: `[Analytics, FDC, QMS]`
- 빈 도메인: 없음
- 이상 매핑:
  - 소비재/식품 맥락보다 공통 추천셋이 고정적으로 유지

### Industry G

- equip: `[Analytics, EAP, FDC]`
- quality: `[Analytics, FDC, QMS]`
- planning: `[APS]`
- logistics: `[WMS]`
- dataai: `[Analytics, FDC, QMS]`
- 빈 도메인: 없음
- 이상 매핑:
  - 제약/바이오 특화 차별 없이 동일 템플릿 출력

### Industry H

- equip: `[Analytics, EAP, FDC]`
- quality: `[Analytics, FDC, QMS]`
- planning: `[APS]`
- logistics: `[WMS]`
- dataai: `[Analytics, FDC, QMS]`
- 빈 도메인: 없음
- 이상 매핑:
  - 자동차 산업에서도 A~G와 동일한 결과 유지

## 4) 스냅샷 총평

- A~H 전 산업에서 Card2 추천 시스템 구성이 사실상 동일했다.
- 산업별 분화 신호보다 키워드 기반 공통 셋(`EAP/FDC/SPC/APS/WMS/BI`)의 영향이 지배적이었다.
- 빈 도메인은 없었지만, 이는 산업 특화가 좋아서가 아니라 입력 키워드를 강하게 고정했기 때문이다.
- `Analytics`의 다중 도메인 중복 노출, `FDC`의 데이터/품질 동시 노출 등 "도메인 경계가 흐린 매핑"이 반복 관찰됐다.
