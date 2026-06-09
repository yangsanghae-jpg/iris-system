# Step5 전 챕터 다국어 데이터 보완 지시서 (v1)

## 목적
Step5 Ch0~Ch6의 내부 데이터에 한국어(`_ko`) 평행 필드를 추가한다. 기존 중국어(`_cn`/`_zh`/일반 키) 필드는 **절대 수정/삭제하지 말고**, 한국어 형제 필드를 **신규 추가만** 한다.

> **다른 언어 확장 시**: 본 지시서는 `_ko` 기준이다. `_en`/`_ja`도 동일 패턴으로 확장 가능 (`_en` / `_ja` suffix). 엔진의 `_pick_lang` 헬퍼가 `lang=="ko"` 분기만 지원하므로 `_en`/`_ja` 추가 시 엔진 헬퍼도 함께 확장 필요.

---

## 절대 규칙 (모든 작업 공통)

1. **기존 키 불변**: `_cn`/`_zh`/`label_zh` 등 어떤 키도 이름변경·삭제·내용수정 금지.
2. **신규 키는 `_ko`로 통일**: `_kr`/`_kor`/`_korean` 사용 금지. 기존에 `_kr`이 있어도 신규는 `_ko`.
3. **키 명명 규칙**:
   - `*_cn` 접미사가 있는 키 → `_cn`을 `_ko`로 치환 (예: `industry_definition_cn` → `industry_definition_ko`)
   - `label_zh` → `label_ko` (이미 사용 중인 패턴)
   - `_zh` 접미사 → `_ko`로 치환
   - 접미사 없는 일반 필드(중문 값) → 같은 키명에 `_ko` 부착 (예: `oneLine` → `oneLine_ko`)
4. **배열 길이·순서 동일**: 원문 N개면 번역도 N개, 인덱스 1:1 대응.
5. **JSON 형식 유지**: 들여쓰기 2 spaces, UTF-8, 마지막 줄 newline.
6. **JSON 유효성 검증 필수**:
   ```bash
   python3 -c "import json; json.load(open('PATH'))" && echo OK
   ```
7. **다른 파일/디렉터리 손대지 않는다**.

## 번역 톤·문체 가이드 (전 챕터 공통)

- **대상 독자**: 제조업 임원/공장장(C-level, 부장급)
- **문체**: 컨설팅 보고서. 격식 평서체. `~한다 / ~된다` 종결 ("~합니다" 금지).
- **금지어**: "여러분", "우리는", "당사", 이모지, 느낌표, 의문문
- **한자어 우선**: "확보한다"(O) / "챙긴다"(X), "구축한다"(O) / "만든다"(X)
- **약어**: MES, ERP, WIP, BOM, KPI, AMHS, AI, JIT, JIS, OEE, GMP, APC, AGV 등은 영문 대문자 그대로
- **길이**: 원문과 비슷한 분량. 압축·부연 금지.

---

# 챕터별 작업

## Ch0 — Executive Summary (✅ 완료, 변경 없음)

이미 적용 완료된 파일:
- `server/data/industry_profile_text.json` — A~H 각 `industry_definition_ko`, `industry_characteristics_ko`
- `server/data/rule_params.json` — `step5.exec_defaults.{oneLine,topPriorities,topRisks}_ko`

> 비고: `industry_master.exec_oneLine`, `automation_interpretation.exec_oneLine`, `operation_focus_map`, `exec_oneLine_library.json`은 **현재 사문 코드**로 비어있어 실제 미사용. 살리려면 Ch0 보완 작업 (선택, 본 지시서 범위 외).

---

## Ch1 — Management Analysis (부분 완료)

### Ch1-1 (✅ 완료) — 코드 카탈로그 라벨

- `server/data/ch1/catalogs/{mvp,module,direction,kpi}_codes.json`의 `label_ko`는 이미 존재.

### Ch1-2 (대규모) — 산업/세부산업/라우팅 팩

**대상 파일**:
- `server/data/ch1/industry_packs/industry_A.json` ~ `industry_H.json` (8개)
- `server/data/ch1/routing_packs/RT_*.json` (라우팅 팩)
- `server/data/ch1/packs/industry_*.json` (있는 경우)

**추가할 키 (각 파일)**:
| 기존 키 | 신규 키 |
|---|---|
| `industry_message_theme` | `industry_message_theme_ko` |
| `routing_theme` (라우팅 팩) | `routing_theme_ko` |
| `sub_profiles.<코드>.override_theme` | `override_theme_ko` |
| 그 외 산업·라우팅 설명 텍스트 필드(`description`, `message`, `narrative`) | 동일 키 + `_ko` |

> 코드 필드(`code`, `priority_axes`, `mvp_boost` 등 코드 식별자)는 번역하지 않는다.

### Ch1-3 (대규모) — 카탈로그 context_explain

**대상**: `server/data/ch1/catalogs/{mvp,module,direction,kpi}_codes.json` 각 entry의 `context_explain` 객체.

**현 구조 예시 (mvp_codes.json)**:
```json
{
  "code": "MVP_BATCH_TRACE",
  "label_zh": "批次追溯",
  "label_ko": "배치 추적",
  "context_explain": {
    "industry": {
      "F": "消费品与食品制造需要...",
      "G": "医药制造需要满足GMP..."
    },
    "routing": { "RT_BATCH": "...", "RT_LINE": "..." },
    "default": "用于记录生产过程中的批次信息..."
  }
}
```

**추가할 키**: `context_explain` **옆에** `context_explain_ko` 추가 (병렬 객체).
```json
"context_explain_ko": {
  "industry": {
    "F": "소비재 및 식품 제조는 식품안전·추적·리콜 관리 요건을 충족해야 하므로, 배치 추적이 핵심 역량이 된다.",
    "G": "의약품 제조는 GMP 및 감사 요구사항을 충족해야 하므로, 완전한 배치 기록과 추적 근거를 보존해야 한다."
  },
  "routing": {
    "RT_BATCH": "배치형 생산에서는 원료·공정 조건·품질 결과를 연계해야 한다.",
    "RT_LINE": "라인형 생산에서는 투입 배치·생산 과정·산출 결과의 연결에 활용한다."
  },
  "default": "생산 과정의 배치 정보를 기록하여 품질 추적 및 원인 추적을 구현한다."
}
```

**대상 파일 4개** (`mvp/module/direction/kpi_codes.json`) × 각 코드(파일당 약 20~30개) × `industry`(A~H 일부) + `routing`(RT_*) + `default` ≒ 약 **300~500 문장**.

### Ch1-4 — summary_rules.py 템플릿 (Python 코드)

**대상**: `server/assemble/ch1_mgmt/summary_rules.py`

현재 산업별 4블록 템플릿(약 50문장)이 Python 딕셔너리에 중국어로 하드코딩됨. 동적 f-string도 중국어 패턴 사용.

**보완 방안 (2안 중 택1)**:
- **A안 (권장)**: 템플릿을 JSON으로 분리 → `server/data/ch1/summary_templates.json`에 `zh`/`ko` 평행 작성, `summary_rules.py`는 lang을 받아 로드.
- **B안**: Python 딕셔너리 안에 `_zh`/`_ko` 평행 키 추가하고 `build_summary(lang=...)` 분기.

**문장 패턴 예시**:
- 중: `"建议优先建立以批次追溯和质量监控为核心的食品制造闭环..."`
- 한: `"배치 추적과 품질 모니터링을 핵심으로 한 식품 제조 폐루프 우선 구축을 권장한다..."`

---

## Ch2 — System Mapping (전체 미번역, 가장 큰 작업)

### 대상 디렉터리
`server/data/ch2/catalog/`

### 파일별 작업

#### Ch2-1 `systems_catalog.json`
시스템(MES, ERP, WMS 등) 정의 카탈로그.
- 각 entry의 `name`/`desc`/`function`/`value_proposition` 등 텍스트 필드 → `_ko` 추가.

#### Ch2-2 `domain_cards_catalog.json`
6개 도메인 카드(계획/실행/품질/물류/설비/통합) 텍스트.
- `title`/`subtitle`/`why`/`how`/`risk`/`outcome` 류의 텍스트 → `_ko` 추가.

#### Ch2-3 `keywords_catalog.json`, `keywords_map.json`, `keywords_map_merged.json`
키워드 사전. `label`/`description` 필드 → `_ko`.
- `keywords_map.json`은 매핑이라 키 자체는 식별자. 값 측 텍스트만 번역.

#### Ch2-4 `messages_catalog.json`
도메인별 추천 메시지. **가장 노출 빈도 높음**.
- 모든 `text` / `message` / `recommendation` 필드 → 동일 키 + `_ko`.

#### Ch2-5 `execution_candidate_master_v1_52.json`, `execution_industry_features.json`
실행 후보 마스터.
- `feature_name`/`benefit`/`risk`/`note` 등 텍스트 필드 → `_ko`.

#### Ch2-6 `stack_library/<stack_id>.json`
스택 라이브러리(파일당 1 stack). 각 파일의 `name`/`description`/`compact_io_labels` 등.
- 이미 `compact_io_labels_i18n.{zh,en}` 구조가 있는 경우 `ko` 키 추가만 하면 됨.
- 그 외 평문 텍스트는 일반 `_ko` 패턴 적용.

#### Ch2-7 `domain_alias.json`, `quality_level_mapping_v1_7.json`, `subindustry_bridge_v1_7.json`
주로 매핑 테이블이므로 값측에 텍스트가 있는 필드(`label`/`display_name`)만 `_ko`.

#### Ch2-8 `knowledge/step5/ch2/card6/10_card6_master.json`
Card6(통합 카드) 마스터. 텍스트 필드 → `_ko`.

### Ch2 엔진/렌더러 보완
- **렌더러 측**: `client/src/ui/step5/2_system/ch2_render.js` line 115/157 이미 `lang` 분기 패턴 존재 (`compact_io_labels_i18n[lang]`). 동일 패턴으로 다른 텍스트 필드 확장.
- **서버 측**: `server/assemble/ch2_system/` 내 `compose.py`, `engine_bridge.py`, `catalog_provider.py`에서 텍스트를 출력에 실어내는 지점에 `lang` 인자 추가.

### Ch2-9 (별도) — DB 동기화
이 데이터들은 `server/storage/app_knowledge.db`에도 패키지(`pack_release_id`)로 적재됨. 번역 후 DB 재패킹 필요할 수 있음 (별도 절차, 코드 변경 아님).

---

## Ch3 — Scope (텍스트 데이터 거의 없음)

### 대상
`server/assemble/ch3_scope/engine.py`는 직접 데이터 파일을 읽지 않고 step3 결과 + 이미 번역된 knowledge dict를 소비한다.

### 작업
- Ch3가 사용하는 상위 데이터(`rule_params.json`의 `step5.scope_adjustment`, `delivery_risk_annotation` 등) 안의 텍스트성 필드(`annotation_style` 등)에 `_ko` 추가.
- 엔진이 하드코딩 문구를 출력하는지 검토 후 발견 시 별도 보고.

> 실제로 Ch3은 출력 텍스트가 적어 작업량은 미미.

---

## Ch4 — Delivery Plan

### 대상
`server/assemble/ch4_plan/engine.py` — 텍스트 데이터 파일 없음. step3 + knowledge 소비만.

### 작업
- 엔진 내 하드코딩 라벨/단계명(예: "단계1", "Phase 1") 그레프 후 발견 시 외부 JSON으로 추출 + `_ko` 추가.
- **현재 추정**: 텍스트 거의 없음. 검토만 필요.

---

## Ch5 — Team Governance

### 대상 파일
`server/data/team_governance/defaults.py` (**JSON 아닌 Python 모듈**)

### 현황
- `TEAM_GOVERNANCE_DEFAULTS` 딕셔너리에 역할명/책임/RACI 텍스트가 중국어 리터럴로 하드코딩.

### 보완 방안 (택1)
- **A안 (권장)**: 텍스트만 JSON으로 분리 → `server/data/team_governance/defaults.json` (zh/ko 평행) 만들고 `composer.py`가 lang에 따라 picker 적용.
- **B안**: Python 딕셔너리에 `_zh`/`_ko` 평행 키 추가 후 composer에서 분기.

### 키 패턴
- `role_name` → `role_name_ko`
- `responsibility` → `responsibility_ko`
- `raci_*` 라벨 → `*_ko`

---

## Ch6 — ROI Logic

### 대상 파일
`server/data/roi/roi_logic_catalog_v1.json`

### 작업
- 카탈로그 내 모든 entry의 텍스트 필드(`name`/`description`/`assumption`/`formula_explain`/`risk_note`) → 같은 키 + `_ko`.
- 산업별 override 섹션이 있다면(`industry_overrides.{A..H}.*`) 동일 패턴.
- **수식·숫자 파라미터는 절대 번역하지 않는다**.

---

# 엔진/와이어링 보완 (데이터 작업과 별개)

데이터에 `_ko`만 추가해도 엔진이 안 읽으면 무효. 각 챕터마다 다음이 필요:

| 챕터 | 엔진 변경점 |
|---|---|
| Ch0 | ✅ 이미 적용 (`engine.py` `_pick_lang`, `compose(... lang=)`) |
| Ch1 | ✅ Ch1-1 완료. Ch1-2/3/4 진행 시 `code_to_explain(lang=)`, `compose_ch1_four_blocks` 내 추가 분기, `summary_rules.build_summary(lang=)` 확장 필요 |
| Ch2 | `compose_ch2_v1`, `build_ch2_engine_from_kw_map`, `compose.py` 텍스트 출력 지점 전부에 `lang` 인자 추가 필요. 분량 큼 |
| Ch3~6 | `compose_scope/plan/team/roi(... lang=)` 시그니처 확장. `assemble/__init__.py` 디스패처도 `lang` 전달 |
| 전역 | `server/diagnose_legacy.py`에서 모든 composer 호출에 `lang=payload.lang` 전달 (현재는 Ch0/Ch1만 전달) |

### `_pick_lang` 헬퍼 재사용
Ch0 엔진의 `_pick_lang(d, key, lang)` 패턴(`_cn`→`_ko` 치환 + `<key>_ko` append)을 공용 모듈로 추출해 다른 챕터에서 import 가능하도록 한다. 권장 위치: `server/assemble/_i18n.py`.

---

# 작업 종료 체크리스트

- [ ] JSON 파싱 성공 확인:
  ```bash
  find server/data -name '*.json' -exec python3 -c "import json,sys; json.load(open(sys.argv[1]))" {} \;
  ```
- [ ] `_ko` 키 카운트 증분 확인:
  ```bash
  grep -ro '"[a-zA-Z_]*_ko"' server/data | wc -l
  ```
- [ ] 기존 키 보존 확인 (zh 카운트 변동 없어야 함):
  ```bash
  grep -ro '"[a-zA-Z_]*_zh"\|"[a-zA-Z_]*_cn"' server/data | wc -l
  ```
- [ ] 8 산업 × 2 언어 스모크 테스트 (zh/ko):
  ```bash
  for I in A B C D E F G H; do for L in zh ko; do
    curl -s -X POST http://localhost:8000/api/diagnose \
      -H 'Content-Type: application/json' \
      -d "{\"industry\":\"$I\",\"product_type\":\"discrete\",\"automation_level\":\"AUTO2\",\"scale\":{\"equipment\":\"M\",\"employees\":\"M\",\"revenue\":\"M\"},\"lang\":\"$L\"}" \
      | python3 -c "import sys,json; d=json.load(sys.stdin); print('$I/$L OK' if d.get('ok') else '$I/$L FAIL')"
  done; done
  ```
- [ ] 도커 리빌드: `./down.sh && ./build.sh && ./up.sh`

---

# 우선순위 권장 순서

1. **Ch2 messages_catalog.json + domain_cards_catalog.json** — 가장 노출도 높고 분량 큼. 먼저 처리하면 체감 효과 최대.
2. **Ch1-2 (industry/routing packs)** — Ch1 summary 톤 한국어화의 전제 조건.
3. **Ch6 roi_logic_catalog_v1.json** — 단일 파일, 영향도 큼.
4. **Ch1-3 (context_explain_ko)** — 분량 크지만 노출은 hover/explain 부분에 한정.
5. **Ch1-4 summary_rules** — 코드 리팩토링 동반.
6. **Ch2 나머지 카탈로그** — systems/keywords/execution_candidate 등.
7. **Ch5 team_governance** — 별도 분리 작업.
8. **Ch3/Ch4** — 검토 후 미미하면 skip.

각 단계마다 데이터 추가 → 엔진 lang 분기 추가 → 도커 리빌드 → 스모크 순서로 한 사이클씩 완결.
