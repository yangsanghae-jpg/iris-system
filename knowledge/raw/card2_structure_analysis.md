# Step5 CH2 Card2 구조 분석 (Step A)

## 1) Card2 본질 정의

- Card2는 **Execution(`exec`)을 제외한 나머지 시스템 추천 카드**다.
- Card2는 엔진의 `by_domain` 추천 결과를 렌더링한 결과물이다.
- 생성 경로는 `engine_bridge` -> `compose_ch2_v1` -> `domain_cards` 구조다.
- 즉 Card2는 "생산 실행 카드"가 아니라, 실행 이후/주변의 지원 시스템 묶음(품질/설비/계획/물류/데이터)을 보여준다.

## 2) 데이터 흐름

Card2의 추천 흐름은 아래 순서로 고정된다.

`keywords -> kw_map -> by_domain -> compose_ch2_v1 -> recommended_by_domain -> domain_cards (Card2 포함)`

- `keywords`는 입력 키워드 배열이다.
- `kw_map`은 키워드를 도메인/시스템으로 매핑하는 규칙이다.
- `by_domain`은 도메인별 상위 추천 시스템을 계산한 엔진 출력이다.
- `compose_ch2_v1`은 엔진 출력을 UI 계약 구조로 조합한다.
- `recommended_by_domain`은 도메인별 추천 코드 목록이다.
- 최종적으로 `domain_cards` 블록에서 Card2 도메인(`equip`, `quality`, `planning`, `logistics`, `dataai`)이 렌더링된다.

## 3) 입력 변수

Card2가 받는 핵심 입력:

- `industry`
- `scale` (`S1~S4`로 정규화)
- `automation_level`
- `keywords` (가장 중요)

핵심 관찰:

- Card2는 **`keywords` 의존도가 매우 높다**.
- `keywords=[]`일 때 엔진은 `NO_KW_HIT`로 `by_domain`을 비우고, Card2 추천도 사실상 붕괴한다.
- 반대로 단일 키워드(`BI`)만 넣으면 `dataai` 단일 도메인으로만 좁게 생성된다.

## 4) 출력 구조

Card2는 도메인별로 아래 구조를 가진다.

- `role`
- `capability`(실제 키는 `cap`)
- `interface`(실제 키는 `iface`)
- `recommended_systems`

도메인별 요약:

- `equip`: `recommended_systems` 기준으로 설비 계열 후보를 노출
- `quality`: 품질 계열 후보를 노출
- `planning`: 계획 계열 후보를 노출
- `logistics`: 물류 계열 후보를 노출
- `dataai`: 데이터/AI 후보를 노출 (현재는 Card6 override로 `iface` 비활성)

핵심:

- Card2는 **추천 시스템 리스트(`recommended_systems`) 중심**이다.
- Card1처럼 "대표 실행 시스템 role 중심"으로 서술되는 구조가 아니다.

## 5) Card1 vs Card2 차이

| 구분 | Card1 | Card2 |
|---|---|---|
| 성격 | 실행 | 지원 시스템 |
| 결정 방식 | `industry + scale` 중심 (execution candidate master) | `keywords` 중심 (`kw_map`) |
| 구조 | role 중심 실행 카드 | system 중심 추천 카드 |
| 안정성 | 높음 | 낮음 (키워드 품질 의존) |

## 6) 구조 분석 결론

- Card2 자체는 계약 구조 관점에서 정상이다.
- 문제의 중심은 카드 뼈대가 아니라, 추천 입력(`kw_map`)과 표현 레이어의 깊이다.
- 따라서 Card2 개선 포인트는 "카드 제거/교체"가 아니라 "추천 로직 정밀화 + 표현 밀도 강화"에 있다.
