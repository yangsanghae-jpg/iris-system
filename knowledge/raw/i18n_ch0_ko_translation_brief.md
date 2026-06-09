# Step5 Ch0 한국어 번역 지시서

## 목적
Step5 Executive Summary(Ch0)에 한국어 평행 필드를 추가한다. 기존 중국어(`_cn`) 필드는 절대 수정/삭제하지 말고, 옆에 한국어 형제 필드(`_ko`)를 신규 추가만 한다.

## 작업 범위
다음 2개 파일을 편집한다. (3·4는 선택 작업)

| # | 파일 (절대경로) | 작업 |
|---|---|---|
| 1 | `/Users/iris/Documents/0Dev/diagnosis-tool/server/data/industry_profile_text.json` | 산업 A~H 각각에 `_ko` 추가 |
| 2 | `/Users/iris/Documents/0Dev/diagnosis-tool/server/data/rule_params.json` | `step5.exec_defaults`에 `_ko` 추가 |
| 3 (선택) | `/Users/iris/Documents/0Dev/diagnosis-tool/server/data/industry_master.json` | 산업별 `exec_oneLine_ko` 추가 |
| 4 (선택) | `/Users/iris/Documents/0Dev/diagnosis-tool/server/data/ch0_exec/exec_oneLine_library.json` | `lines[].text_ko` 추가 |

## 절대 규칙 (모든 작업에 적용)
1. **기존 키는 건드리지 않는다**: `_cn`, `_zh`, `_kr`, `name_ko` 등 어떤 키도 이름변경/삭제/내용수정 금지.
2. **신규 키는 `_ko`로 통일**: `_kr`, `_kor`, `_korean` 등 다른 표기 사용 금지. 기존에 `_kr`이 있어도 새로 추가하는 것은 `_ko`.
3. **배열은 길이·순서 동일**: 원문 배열이 3개면 번역도 3개, 인덱스 0↔0, 1↔1, 2↔2 일대일 대응.
4. **JSON 형식 유지**: 들여쓰기 2 spaces, UTF-8, 마지막 줄에 newline 1개.
5. **편집 후 JSON 유효성 검증 필수**: 작업 종료 시 아래 명령으로 파싱 성공 확인.
   ```bash
   python3 -c "import json; json.load(open('PATH'))" && echo OK
   ```
6. **다른 파일/디렉터리 손대지 않는다**.

## 번역 톤·문체 가이드
- **대상 독자**: 제조업 임원/공장장(C-level, 부장급)
- **문체**: 컨설팅 보고서. 격식 평서체. "~합니다"가 아닌 **"~한다 / ~된다"** 종결.
- **금지**: "여러분", "우리는", "당사", 이모지, 느낌표, 의문문
- **한자어 우선**: "확보한다(O) / 챙긴다(X)", "구축한다(O) / 만든다(X)"
- **약어**: MES, ERP, WIP, BOM, KPI, AMHS, AI 등은 영문 대문자 그대로
- **길이**: 원문과 비슷한 분량. 너무 짧게 압축하거나 부연 설명 추가 금지.
- **예시**:
  - 중문: `以"标准化优先 + 执行闭环"为起点，逐步构建可复制、可扩展的智能制造体系。`
  - 한국어: `"표준화 우선 + 실행 폐루프"를 출발점으로, 복제 가능하고 확장 가능한 스마트제조 체계를 단계적으로 구축한다.`

---

## 작업 1: `industry_profile_text.json`

### 위치
`/Users/iris/Documents/0Dev/diagnosis-tool/server/data/industry_profile_text.json`

### 현재 구조 (산업 B 예시)
```json
{
  "version": "...",
  "industries": {
    "A": { "industry_definition_cn": "...", "industry_characteristics_cn": [...] },
    "B": {
      "industry_definition_cn": "半导体制造是在多次再入工艺与强设备约束条件下...",
      "industry_characteristics_cn": [
        "典型的再入型工艺结构...",
        "设备能力、状态与调度优先级...",
        "自动化与AMHS并非效率工具..."
      ]
    },
    "C": { ... }, ... "H": { ... }
  }
}
```

### 추가할 키
산업 `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H` **각각**에 다음 2개 키 추가:
- `industry_definition_ko`: `industry_definition_cn`의 한국어 번역 (문자열)
- `industry_characteristics_ko`: `industry_characteristics_cn`의 한국어 번역 (문자열 배열, 길이 동일)

### 결과 예시 (B)
```json
"B": {
  "industry_definition_cn": "半导体制造是在多次再入工艺与强设备约束条件下，通过稳定WIP流、精细化执行控制与高度自动化系统来保障良率、产能与一致性的高复杂度制造体系。",
  "industry_definition_ko": "반도체 제조는 다수의 재진입(re-entry) 공정과 강한 설비 제약 조건 하에서, 안정적인 WIP 흐름, 정밀한 실행 제어, 고도로 자동화된 시스템을 통해 수율·생산능력·일관성을 보장하는 고복잡도 제조 체계이다.",
  "industry_characteristics_cn": [
    "典型的再入型工艺结构使生产路径高度非线性，计划复杂度随WIP规模呈指数级上升。",
    "设备能力、状态与调度优先级直接决定生产结果，实时执行控制的重要性显著高于静态计划。",
    "自动化与AMHS并非效率工具，而是维持工厂可运行性的基础设施。"
  ],
  "industry_characteristics_ko": [
    "전형적인 재진입 공정 구조로 인해 생산 경로가 고도로 비선형이며, 계획 복잡도는 WIP 규모에 따라 지수적으로 증가한다.",
    "설비 능력·상태·스케줄링 우선순위가 생산 결과를 직접 결정하므로, 실시간 실행 제어의 중요도가 정적 계획보다 현저히 높다.",
    "자동화와 AMHS는 효율화 수단이 아니라, 공장 가동성을 유지하는 기반 인프라이다."
  ]
}
```

---

## 작업 2: `rule_params.json`

### 위치
`/Users/iris/Documents/0Dev/diagnosis-tool/server/data/rule_params.json`

### 현재 구조 (해당 경로만)
```json
{
  "step5": {
    "exec_defaults": {
      "oneLine": "以\"标准化优先 + 执行闭环\"为起点，逐步构建可复制、可扩展的智能制造体系。",
      "topPriorities": [
        "统一主数据与版本口径（物料 / 工艺 / 资源 / 权限）",
        "构建 MES 执行闭环（工单 / WIP / 追溯 / 异常 / Hold）",
        "按自动化等级逐步扩展（设备闭环 → 物流闭环 → AI 闭环）"
      ],
      "topRisks": [
        "数据口径不统一导致系统上线后报表不可用",
        "现场规则未固化，系统被绕过，仍依赖人工经验",
        "系统接口责任不清，形成双录入与对账负担"
      ]
    }
  }
}
```

### 추가할 키
`step5.exec_defaults` 안에 다음 3개 키 추가:
- `oneLine_ko`: 문자열
- `topPriorities_ko`: 문자열 배열 (길이 3, 인덱스 일대일)
- `topRisks_ko`: 문자열 배열 (길이 3, 인덱스 일대일)

### 결과 예시
```json
"exec_defaults": {
  "oneLine": "以\"标准化优先 + 执行闭环\"为起点，逐步构建可复制、可扩展的智能制造体系。",
  "oneLine_ko": "'표준화 우선 + 실행 폐루프'를 출발점으로, 복제 가능하고 확장 가능한 스마트제조 체계를 단계적으로 구축한다.",
  "topPriorities": [
    "统一主数据与版本口径（物料 / 工艺 / 资源 / 权限）",
    "构建 MES 执行闭环（工单 / WIP / 追溯 / 异常 / Hold）",
    "按自动化等级逐步扩展（设备闭环 → 物流闭环 → AI 闭环）"
  ],
  "topPriorities_ko": [
    "마스터 데이터와 버전 기준 통일(자재 / 공정 / 자원 / 권한)",
    "MES 실행 폐루프 구축(작업지시 / WIP / 추적 / 이상 / Hold)",
    "자동화 수준에 따라 단계적으로 확장(설비 폐루프 → 물류 폐루프 → AI 폐루프)"
  ],
  "topRisks": [
    "数据口径不统一导致系统上线后报表不可用",
    "现场规则未固化，系统被绕过，仍依赖人工经验",
    "系统接口责任不清，形成双录入与对账负担"
  ],
  "topRisks_ko": [
    "데이터 기준이 통일되지 않아 시스템 가동 후 리포트가 사용 불가해진다",
    "현장 규칙이 정착되지 않아 시스템이 우회되고 여전히 인력 경험에 의존한다",
    "시스템 인터페이스 책임이 불분명해 이중 입력 및 대사(對賬) 부담이 발생한다"
  ]
}
```

---

## 작업 3 (선택): `industry_master.json`

### 위치
`/Users/iris/Documents/0Dev/diagnosis-tool/server/data/industry_master.json`

### 작업 내용
`industries.A`~`industries.H` 각각에 `exec_oneLine`(중문)과 `exec_oneLine_ko`(한국어)를 한 줄 결론으로 추가한다. 현재 양쪽 모두 비어 있으므로 **신규 작성**해도 좋다. 한 산업의 핵심 운영 방향성을 1문장으로 압축.

### 예시 (B 반도체)
```json
"B": {
  "industry_code": "B",
  "name_cn": "半导体",
  "name_ko": "반도체",
  "exec_oneLine": "以稳态WIP与设备-AMHS联动为核心，通过执行控制与高度自动化保障良率与产能。",
  "exec_oneLine_ko": "안정적 WIP 흐름과 설비-AMHS 연동을 중심으로, 실행 제어와 고도 자동화를 통해 수율과 생산능력을 보장한다.",
  ... (다른 기존 필드 유지)
}
```

---

## 작업 4 (선택): `ch0_exec/exec_oneLine_library.json`

### 위치
`/Users/iris/Documents/0Dev/diagnosis-tool/server/data/ch0_exec/exec_oneLine_library.json`

### 작업 내용
`industries.*.lines[]`의 각 항목에 `text_ko` 필드 추가. **주의**: 이 파일은 기존에 `industry_name_kr`(밑줄+kr)을 사용 중이지만, **신규 추가는 `text_ko`**로 한다 (다른 파일과 통일).

### 예시
```json
{
  "id": "B_PLAN_01",
  "tag": "plan",
  "text": "围绕WIP稳定与设备调度优先级，统一计划-执行-反馈节奏，保障产能与一致性。",
  "text_ko": "WIP 안정화와 설비 스케줄링 우선순위를 중심으로, 계획-실행-피드백 리듬을 통일해 생산능력과 일관성을 보장한다.",
  "hints": ["WIP","设备调度","一致性"]
}
```

각 산업당 lines 6개 × A~H 8산업 = 약 48개 항목.

---

## 작업 종료 시 체크리스트

- [ ] 작업 1: `industry_profile_text.json`에서 A~H 8개 산업 모두 `_ko` 2종(definition + characteristics) 추가됨
- [ ] 작업 2: `rule_params.json`의 `step5.exec_defaults`에 `_ko` 3종 추가됨
- [ ] (선택) 작업 3, 4 수행 여부 명시
- [ ] 모든 배열은 원문과 길이·인덱스 일치
- [ ] 모든 기존 키는 그대로 보존
- [ ] JSON 파싱 성공 확인:
  ```bash
  python3 -c "import json; json.load(open('/Users/iris/Documents/0Dev/diagnosis-tool/server/data/industry_profile_text.json'))" && echo OK
  python3 -c "import json; json.load(open('/Users/iris/Documents/0Dev/diagnosis-tool/server/data/rule_params.json'))" && echo OK
  ```
- [ ] 추가된 `_ko` 키 개수를 리포트
  ```bash
  grep -o '"[a-zA-Z_]*_ko"' /Users/iris/Documents/0Dev/diagnosis-tool/server/data/industry_profile_text.json | sort | uniq -c
  grep -o '"[a-zA-Z_]*_ko"' /Users/iris/Documents/0Dev/diagnosis-tool/server/data/rule_params.json | sort | uniq -c
  ```

## 작업 완료 후

번역 완료 보고만 하면 됩니다. 엔진(`server/assemble/ch0_exec/engine.py`) 수정과 언어 분기 처리, UI 와이어링, 도커 리빌드, 8산업 스모크 검증은 사용자(이리스)가 진행합니다.
