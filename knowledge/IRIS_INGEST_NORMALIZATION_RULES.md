# IRIS 지식 추출·정규화 규칙 (Ingest Normalization Rules)

입력(문서·AI 대화·웹)이 LLM을 거쳐 **정규화된 md**가 되기까지의 변환 규격이다.
`OBSIDIAN_작성_가이드`(사람이 쓸 때)와 `IRIS_WIKI_QUALITY_RULES`(쌓인 후 유지)의 **앞 단계**를 담당한다.

## 0. 전체 흐름 (한 장 요약)

```
원본 보존 → ① 추출(md 변환) → ② 정규화(LLM) → ③ 개념 매칭 → ④ 저장 라우팅 → ⑤ 승격(사람)
   originals/      raw/            문서노트(Silver)     concepts.yaml      아래 표          wiki/ (Gold)
```

**대원칙: 입력 1건 = 문서노트 1개(Silver).** wiki(Gold)에는 문서노트를 직접 넣지 않는다.
Gold 개념 노트는 문서노트가 승격 게이트를 통과할 때 **근거(sources)로 연결**될 뿐이다.

## 1. 산출물은 두 종류다 — 섞지 말 것

| 산출물 | 무엇 | 위치 | 만드는 주체 |
|---|---|---|---|
| **문서노트** | 입력 1건의 요약·핵심·수치 | `raw/`(→ silver) | LLM 자동 |
| **개념노트** | MES, 수율 등 개념 단위 정리 | `wiki/` (Gold) | 사람 (LLM은 후보 제안만) |

그래프 인사이트는 개념노트에 문서노트 링크가 **집중**될 때 나온다.
문서노트를 wiki에 쏟아 넣으면 파일명 노드만 늘고 인사이트는 사라진다 (현재 증상의 원인).

## 2. 문서노트 정규화 스키마 (LLM 출력 규격)

### frontmatter (필수)

```yaml
---
title: ""                # 원본 제목 그대로. 없으면 내용 기반 생성 후 (생성) 표기
doc_id: ""               # 채번 규칙: {channel}_{YYYYMMDD}_{seq} 예: doc_20260702_0413
channel: ""              # doc | chat | web  ← 창구 구분 (신뢰 관리의 축)
source: ""               # 원본 파일 경로 | 대화 세션 id | URL
ingested_at: ""          # 수집일 YYYY-MM-DD
industry: ""             # A~H, 판단 불가 시 "" (억지로 채우지 말 것)
area: ""                 # planning | quality | equipment | logistics
level: ""                # L0~L4
status: "draft"
trust: ""                # 채널별 기본값 — doc: clipped / chat: auto / web: auto
concepts: []             # ③에서 매칭된 canonical 개념명만. 사전에 없는 건 candidates로
candidates: []           # 사전에 없는 신규 개념 후보 (링크 아님, 검토 큐)
extraction_note: ""      # 추출 손실 기록 예: "표 3개 이미지라 미추출"
tags: []
---
```

### 본문 구조 (고정 5섹션)

```markdown
## 요약
(2~3문장. 이 문서가 무엇이고 왜 중요한지)

## 핵심 내용
- (사실 단위 bullet. 원문에 있는 것만)

## 주요 수치·데이터
- (숫자는 원문에 실제로 있는 것만. 원문 위치 병기: "p.12", "슬라이드 8")

## 관련 개념
- [[mes]] [[capacity_planning]]   ← concepts.yaml에 있는 것만

## 해석·한계 (LLM 소견)
- (추론·평가는 반드시 이 섹션에만. 위 섹션과 섞지 말 것)
```

### LLM 금지 사항 (프롬프트에 그대로 넣을 것)

1. **숫자 창조 금지** — 원문에 없는 수치·비율·연도를 쓰지 않는다.
2. **자유 링크 금지** — `[[...]]`는 개념 사전에 있는 canonical 명만. 새 개념은 `candidates:`에.
3. **사실과 해석 혼합 금지** — 추론은 "해석·한계" 섹션에만.
4. **문서 병합 금지** — 입력 여러 건을 한 노트로 합치지 않는다 (통합은 Gold 승격 때 사람이).
5. **Gold 판단 금지** — status/trust 승격은 LLM이 하지 않는다.

## 3. 개념 매칭 (③) — 그래프 품질의 핵심

- 사전: `knowledge/concepts.yaml` — canonical 명(영문 snake_case) + alias(한/영/중) + wiki 경로.

```yaml
# concepts.yaml 예시
mes:
  aliases: [MES, 생산실행시스템, 생산 실행 시스템, 제조실행시스템, 制造执行系统]
  path: wiki/concepts/mes.md
```

- LLM이 뽑은 개념(3~7개)을 사전에 **매칭 성공 → `concepts:`**, 실패 → `candidates:`.
- `candidates:`는 주 1회 검토: 사전 등록(+ wiki에 stub 노트 생성) 또는 기각.
- 이 게이트가 없으면 `[[MES]]` `[[생산실행시스템]]`이 별개 노드로 갈라져 그래프가 깨진다
  (현 vault의 `mes_생산실행시스템` / `mes_생산_실행_시스템` 중복이 그 사례).

## 4. 채널별 특칙

| 항목 | doc (문서 추출) | chat (AI 대화) | web (웹 검색) |
|---|---|---|---|
| 기본 trust | clipped | auto | auto |
| source 기록 | 원본 경로 + 문서일자·작성자(있으면) | 세션 id + 대화일 + 모델명 | URL + fetched_at |
| 특칙 | 추출 손실을 extraction_note에 기록 (표·이미지·수식) | 잡담 제거, **주장·결정·인사이트만** 추출. 전부 미검증 취급 | 인용 vs 의역 구분. 1년 경과 시 재검토 대상 |
| Gold 근거 사용 | 검수 후 가능 | **사람 검증 전 불가** | 검증 + 원출처 확인 후 가능 |

## 5. 저장 라우팅 (④)

| 대상 | 위치 | 파일명 |
|---|---|---|
| 원본 | `originals/{channel}/` (수정 금지) | 원본명 유지 |
| 추출 원문 md | `raw/{doc_id}.md` | doc_id |
| 문서노트 | `raw/notes/{doc_id}.md` (또는 silver/) | doc_id |
| 개념노트 | `wiki/` 기존 체계 (concepts/, industries/, areas/) | 영문 snake_case |

## 6. 저장 전 검증 게이트 (자동)

- [ ] frontmatter 필수 필드 채움 (doc_id, channel, source, ingested_at)
- [ ] `[[링크]]` 전부 concepts.yaml에 존재
- [ ] "주요 수치" 섹션의 숫자가 추출 원문에 실재 (샘플 검사라도)
- [ ] 본문 320자 이상, 5섹션 구조 준수
- 실패 시 저장하지 않고 `staging/failed/`로 — 깨진 노트가 쌓이는 것보다 낫다

## 7. 승격 (⑤) — Silver → Gold

1. 문서노트가 어떤 개념에 몰리는지 집계 (concepts 필드 group by)
2. 문서 N건(권장 3+)이 모인 개념 → 사람이 개념노트 작성/갱신, `sources:`에 doc_id 연결
3. 이때만 `trust: verified`, `status: published` 부여
4. **A2 진단 데이터는 Gold에서만 도출** — chat/web 유래 미검증 내용이 진단에 흘러들지 않게 하는 구조적 차단선
