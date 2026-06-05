# IRIS Wiki 품질 관리 운영 규칙

LLM·Router·저장 파이프라인과 별개로, **쌓인 `/wiki`를 건강하게 유지**하기 위한 사람·프로세스 기준이다.  
merge(통합 ingest) 전에 이 규칙을 우선한다.

## 1. 주기적 lint

- `GET /wiki/lint`(또는 Router `knowledge_lint`)로 `summary`·`policy_checks`·`issues`를 본다.
- `summary.issue_count`가 0이 아니면, 아래 항목별로 원인을 나눠 본다.
- **기계 판정**(엔진이 채움):
  - `summary.quality_gate`: `pass` | `warning` | `block`
    - **block**: 깨진 링크(`broken_links`)가 하나라도 있음 → merge 등 누적 작업은 하지 않는 것을 권장.
    - **warning**: 깨진 링크는 없으나 기타 이슈(고립·중복 후보·약한 문서)가 있음.
    - **pass**: 이슈 카운트 0.
  - `policy_checks.merge_allowed`: `quality_gate != block` (깨진 링크가 없으면 true).
  - `policy_checks.broken_links_priority` 등: 해당 유형 검토가 필요한지 여부.

## 2. broken_links 최우선

- `[[대상]]`에 대응하는 문서가 없으면 **가짜 구조**가 된다.
- 대응: stub 페이지 추가, 링크 문구를 실제 파일명·제목에 맞게 수정, 또는 의도적 개념 링크면 별도 정책으로 문서화한다.

## 3. duplicate_candidates 결정

- 동일·유사 개념이 여러 파일로 쪼개져 있으면 **통합·대표 문서 지정·교차 링크** 중 하나를 문서마다 결정한다.
- merge로 자동 합치기 전에, **어떤 문서를 canonical로 둘지**부터 정한다.

## 4. orphan_pages 완화

- 들어오는 링크도 거의 없고 나가는 링크도 거의 없으면 검색·탐색에서 고립된다.
- 대응: 관련 문서에서 `[[이 문서]]`를 추가하거나, 이 문서에서 다른 문서로 링크를 연다. 의도적 단독 노트면 예외로 목록에 남긴다.

## 5. weak_pages 보강

- Summary·본문 길이·wikilink 부족은 query 후보 품질을 떨어뜨린다.
- `CLAUDE.md`의 페이지 구조(Title, Summary, Key Concepts, Related Links, Source Notes)에 맞춰 최소한을 채운다.

## 6. merge·대규모 ingest 전 조건

- **lint 이슈를 줄인 뒤** merge/통합 작업을 한다.
- 당장 못 고치면, 남은 이슈를 **수용 범위로 명시**하고 진행한다(기술 부채).
- **`POST /wiki/merge`** 는 엔진 내부에서 **먼저 `run_lint()`** 를 호출한다.
  - `quality_gate == block` 이면 merge는 실행하지 않고 **`merge_blocked`** 이력만 남긴다.
  - `warning` / `pass` 에서만 실제 LLM 병합(update-aware rewrite)이 돌아간다.
- Router는 merge 가능 여부를 **판단하지 않는다**; Wiki 엔진의 gate만 따른다.

## 6b. ingest vs merge

- **`/wiki/ingest`**: raw → 위키 초안 생성(기존과 유사한 흐름).
- **`/wiki/merge`**: 기존 위키 페이지(또는 후보) + raw를 함께 넣어 **덮어쓰기가 아닌 통합 재작성**.

## 7. 저장소 경계 유지

- `/raw`는 원본 보존, 정리·수정은 **`/wiki`만**.
- 처리 이력은 엔진 SQLite(`ingest_history`)로 추적하며, Router는 DB를 직접 수정하지 않는다.

---

이 파일은 **운영 규칙**이다. ingest 프롬프트 규칙은 `CLAUDE.md`를 따른다.
