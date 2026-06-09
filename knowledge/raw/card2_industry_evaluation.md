# Step5 CH2 Card2 산업별 평가 (Step C)

## 1) 목적

Card2를 Card1과 동일한 4축 프레임으로 평가한다.  
대상은 "Execution 제외 지원 시스템 카드"이며, 판정은 구조 자체가 아니라 추천 적합성과 표현 품질을 본다.

참고 입력:

- [Card2 구조 분석](docs/card2_structure_analysis.md)
- [Card2 산업별 스냅샷](docs/card2_industry_snapshots.md)

## 2) 평가 기준 (4축)

1. 범위 적합성
2. 산업 적합성
3. 일관성
4. 표현력

판정 레벨:

- **OK**: 범위/산업/일관성/표현력이 모두 안정
- **WEAK**: 범위는 맞지만 산업성 또는 표현력이 약함
- **NG**: 범위 위반 또는 내부 모순이 큼

## 3) 산업별 4축 평가

| 산업 | 범위 적합성 | 산업 적합성 | 일관성 | 표현력 | 판정 |
|---|---|---|---|---|---|
| A | OK | WEAK | WEAK | WEAK | WEAK |
| B (Semiconductor) | OK | WEAK | WEAK | WEAK | WEAK |
| C | OK | WEAK | WEAK | WEAK | WEAK |
| D | OK | WEAK | WEAK | WEAK | WEAK |
| E | OK | WEAK | WEAK | WEAK | WEAK |
| F | OK | WEAK | WEAK | WEAK | WEAK |
| G | OK | WEAK | WEAK | WEAK | WEAK |
| H | OK | WEAK | WEAK | WEAK | WEAK |

판정 근거 요약:

- 범위 적합성은 높다. Card2가 실행 카드로 넘어가지는 않는다.
- 하지만 A~H 결과가 거의 동일해 산업 적합성이 약하다.
- 도메인별 추천은 존재하지만 반복 패턴이 강해 일관성은 "안정"이 아니라 "고정화"에 가깝다.
- 최종 표현은 추천 시스템 나열 중심이라 value narrative가 약하다.

## 4) 문제 유형 분류 (필수 4종)

### 1) Keyword 의존성 문제

- `keywords`가 없으면 Card2는 `NO_KW_HIT`로 붕괴한다.
- 키워드 설계 품질이 곧 Card2 품질을 결정한다.

### 2) 산업 반영 부족

- A~H 차이가 거의 없다.
- 산업별 컨텍스트(`industry`)가 Card2 추천 결과 분기에 충분히 기여하지 못한다.

### 3) 도메인 불균형

- 특정 코드가 다중 도메인에서 반복된다(예: `Analytics`, `FDC`).
- 도메인 경계가 약해 "어느 도메인에 왜 배치됐는지" 설명력이 낮아진다.

### 4) 표현 문제

- 현재 출력은 추천 리스트 중심 단순 나열이다.
- 카드가 "왜 이 조합이 맞는가"를 산업 문맥으로 풀어주지 못한다.

## 5) 최종 결론

❌ 잘못된 결론

- "Card2가 틀렸다"

✅ 올바른 결론

- Card2는 구조 문제가 아니라  
  **추천 로직(`kw_map`) + 표현 레이어 문제**다.

정리:

- Card2 카드 껍데기는 정상이다.
- 실제 개선 타깃은 `kw_map`의 산업 분해능과, 추천 결과를 의미 있게 번역하는 표현 규칙이다.
