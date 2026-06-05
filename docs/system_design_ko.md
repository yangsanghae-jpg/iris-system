# iris-system 시스템 설계서 (L4-K Knowledge Center)

> **계층**: L4-K (Knowledge Center 프로토타입)
> **버전**: V2.5 정본 (2026-05-22)
> **상태**: 사양·인제스트 파이프라인·검색 골격 가동 / 큐레이션 콘텐츠 채움·통합 엔드포인트 진행 중
> **작성**: 2026-05-31

## 1. 한 줄 정의

IRIS 아키텍처의 **L4-K Knowledge Center 프로토타입**으로, 원시 자료(`raw`)와 외부 정본(reference lane)을 정형화·인덱싱하여 **단일 통합 검색 엔드포인트**(`/api/v1/retrieval` 사양)와 위키 형태로 큐레이션된 지식 자산을 IRIS 전체에 공급한다.

핵심 사양: [knowledge/wiki/architecture/V2.5_2026-05-22.md](../knowledge/wiki/architecture/V2.5_2026-05-22.md)
통합 구조도: [knowledge/통합 구조도.md](../knowledge/통합%20구조도.md)

## 2. 아키텍처

```
호출자 (iris-claw / iris-stack l2-gateway / OpenWebUI 등)
    ↓ HTTP
[router :18080]                       — apps/router/server.py
    ↓ 한국어 키워드 분기
[wiki  :18081]                        — apps/wiki/server.py
    ├─ /wiki/ingest    (외부 정본 등록)
    ├─ /wiki/merge     (중복 정리)
    ├─ /wiki/query     (검색)
    ├─ /wiki/lint      (품질 게이트)
    └─ /wiki/history   (처리 이력)
            ↓
        Ollama (127.0.0.1:11434) — qwen2.5:14b (응답 생성)
        knowledge/_index.db (SQLite + FTS5)
        knowledge/wiki/  (큐레이션 마크다운)
        storage/sqlite/wiki_history.db (처리 이력)

[ingest CLI] apps/ingest/reference_diagnosis.py
    ↓ no-copy 등록 (경로 포인터)
diagnosis-tool/server/data/ (외부 정본)

[quartz 발행기] apps/quartz/  — V2.6 본격 발행 예정
    ↓ content/ = knowledge/wiki/ 비추기
디지털 가든 (정적 사이트)
```

## 3. 핵심 디렉터리

| dir | path | 역할 |
|---|---|---|
| apps/ | [apps/](../apps/) | FastAPI 서비스(router·wiki), 인제스터, Quartz 발행기 |
| knowledge/ | [knowledge/](../knowledge/) | raw 원본, 큐레이션 wiki, `_index.db`(SQLite+FTS5) |
| storage/ | [storage/](../storage/) | 처리 이력 SQLite (`sqlite/wiki_history.db`) |
| Makefile | [Makefile](../Makefile) | 인제스트·인덱스 운영 verb |

루트 README 없음. `.venv/` 로컬 Python.

## 4. apps/ 상세

### apps/router/ — 입력 분기 라우터

| 항목 | 값 |
|---|---|
| 진입 | [apps/router/server.py](../apps/router/server.py) |
| 포트 | **18080** ([test_router.sh](../apps/router/test_router.sh)) |
| 의존 | `fastapi / uvicorn / requests` |
| 역할 | 한국어 키워드(`지식베이스에 반영`, `위키에서` 등)로 `knowledge_ingest / merge / query / lint / chat` 분기 후 wiki 엔진으로 프록시 |

### apps/wiki/ — 지식 엔진

| 항목 | 값 |
|---|---|
| 진입 | [apps/wiki/server.py](../apps/wiki/server.py) |
| 포트 | **18081** |
| 엔드포인트 | `/wiki/ingest`, `/wiki/merge`, `/wiki/query`, `/wiki/lint`, `/wiki/history` |
| 부속 모듈 | [engine.py](../apps/wiki/engine.py), [retrieval.py](../apps/wiki/retrieval.py), [lint.py](../apps/wiki/lint.py), [history.py](../apps/wiki/history.py) |
| LLM | `OLLAMA_URL` 기본 `http://127.0.0.1:11434`, 기본 모델 `qwen2.5:14b` |

### apps/ingest/ — K1d Reference Lane

| 파일 | 용도 |
|---|---|
| [reference_diagnosis.py](../apps/ingest/reference_diagnosis.py) | `/diagnosis-tool/server/data/`(외부 정본)를 **복사 없이** 메타 + 경로 포인터로 `_index.db`에 등록 |
| [schema.sql](../apps/ingest/schema.sql) | `documents` (matrix key: industry/area/level + lane/trust/path) + FTS5 `documents_fts` + `chunks` + `meta_kv`; `chunk_vec` (sqlite-vec)는 K4-EMB 대기로 주석 처리 |

### apps/quartz/ — 디지털 가든 발행기

| 항목 | 값 |
|---|---|
| 스택 | TypeScript / Quartz v4 (Jack Zhao) |
| `content/` | knowledge/wiki/ 비추기 (symlink/사본) |
| 진입 | `npx quartz build|serve` |
| 설정 | [quartz.config.ts](../apps/quartz/quartz.config.ts) |
| 상태 | **V2.6 이월** — 본격 발행은 다음 사양에서 |

## 5. knowledge/ 구조

```
knowledge/
├── _index.db               (~1.9 MB, SQLite + FTS5, primary index)
├── CLAUDE.md               (LLM 작성 규칙)
├── IRIS_WIKI_QUALITY_RULES.md (품질 게이트)
├── 통합 구조도.md
├── raw/
│   ├── Nanoln 지표 트리 (4건)
│   └── mes.txt
└── wiki/
    ├── architecture/V2.3, V2.4, V2.5 + index.md  (정본 V2.5)
    ├── _templates/page.md
    ├── industries/A_project_eto_ato ~ H_auto_mobility   (폴더만, 내부 빈)
    ├── areas/{equipment,logistics,planning,quality}     (빈 스켈레톤)
    ├── concepts/, sources/                              (빈 스켈레톤)
    ├── mes_생산_실행_시스템.md, mes_생산실행시스템.md     (중복 후보)
    └── z_lint_*.md                                      (lint 테스트 픽스처)
```

> 매출/제품/세일즈 플레이북 같은 상업적 자산 **없음**. 현재 제조업 산업/영역 분류 + Nanoln 지표 구조 중심.

## 6. storage/

| 파일 | 용도 |
|---|---|
| [storage/_index.db](../storage/_index.db) | 0바이트 (예약) |
| [storage/sqlite/wiki_history.db](../storage/sqlite/wiki_history.db) | wiki 처리 이력 (ingest/merge/skip/error) |

**실 데이터의 1차 보관소**는 `knowledge/_index.db`. `storage/`는 처리 이력만 분리.

## 7. 데이터 모델 ([apps/ingest/schema.sql](../apps/ingest/schema.sql))

### documents
| 컬럼 | 비고 |
|---|---|
| matrix key | industry / area / level |
| metadata | lane (`raw` / `wiki` / `reference`), trust, path |
| 본문 | title / summary / content |

### chunks
| 컬럼 | 비고 |
|---|---|
| `document_id` | FK |
| `chunk_index` / `text` | 청크 단위 |

### documents_fts (FTS5)
- 가상 테이블, `documents` + `chunks` 결합 인덱스

### meta_kv
- 자유 키-값

### chunk_vec (주석 처리)
- sqlite-vec 제약 + FAISS 외부 인덱스 운영 예정 (V2.5 사양)

## 8. Makefile

| 타깃 | 동작 |
|---|---|
| `ingest-reference` | `apps/ingest/reference_diagnosis.py` 실행 — 외부 정본 등록 |
| `reindex-fts` | `documents_fts`를 documents+chunks로 재구축 |
| `stats` | (lane, area)별 문서 카운트 |
| `clean-reference` | `lane='reference'` 문서 삭제 |

> 빌드·서버 기동·임베딩 타깃 **없음** — 인제스트와 인덱스 운영 verb만 제공.

## 9. 외부 통합

### HTTP API
- Router: `:18080`
- Wiki: `:18081`
- V2.5 사양상 표준 엔드포인트는 `GET /api/v1/retrieval?mode=auto|matrix|fts|semantic` + `X-IRIS-Caller` 헤더 — **현재 구현은 `/wiki/*`까지**, 표준 인터페이스는 진행 중

### LLM
- Ollama `http://127.0.0.1:11434` (기본 `qwen2.5:14b`)
- 시맨틱 검색은 Ollama 임베딩 + FAISS 외부 인덱스로 계획 (V2.5)

### No-Copy 정본 연결
- `/diagnosis-tool/server/data/` 의 JSON을 **경로 포인터로 등록** — 원본은 그대로 외부 위치

## 10. 다른 iris-* 와 관계

| 시스템 | 관계 |
|---|---|
| **iris-claw** (L1) | V2.6 이월: "L1-claw ↔ L2-gateway 통합" 후 K5 호출 |
| **iris-stack l2-gateway** (L2) | `X-IRIS-Caller: L2-Gate` 헤더로 K5 검색 호출, 결과를 `[IRIS_KNOWLEDGE_CONTEXT]` 형태로 프롬프트 주입 (V2.5 사양) |
| **iris-memory** (L3) | 분리 — 직접 의존 없음. L3는 워킹/영속 메모리, 본 시스템은 큐레이션 자산 |
| **iris-gateway** (L4-C) | (간접) |
| **diagnosis-tool** (L6-D1) | **가장 강한 결합**: K5 HTTP 실패 시 `IRIS_K5_MODE=embedded`로 로컬 파싱 fallback 계약 + `/server/data/` 정본의 reference lane 인제스트 |
| **iris-stack observability** | Promtail이 `iris-system/storage`를 read-only 마운트 — K5 telemetry 로그 외부 수집 |

## 11. 데이터 흐름

### 인제스트 (reference)
```
diagnosis-tool/server/data/*.json
    ↓ make ingest-reference
apps/ingest/reference_diagnosis.py
    ↓ no-copy 메타 등록
knowledge/_index.db.documents (lane='reference', trust=high)
    + chunks + documents_fts
```

### 조회 (현 구현)
```
호출자 → router :18080
    ↓ 키워드 분기
wiki :18081 /wiki/query
    ↓ retrieval.py (matrix + FTS5)
    ↓ engine.py + Ollama → 응답 생성
호출자
```

### 조회 (V2.5 사양, 진행 중)
```
호출자 → /api/v1/retrieval?mode=auto&q=... (X-IRIS-Caller: L2-Gate)
    ↓ auto = matrix → fts → semantic 순차
    ↓ semantic은 FAISS + Ollama 임베딩
호출자
```

## 12. V2.5 완료 기준 (사양 명시)

| 지표 | 기준 |
|---|---|
| 정상호출 비율 | ≥ 95% |
| Gold 후보 | ≥ 3 |
| 헤더 누락 | < 1% |
| 가용성 | ≥ 99% |

## 13. 현재 상태 (work-in-progress 신호)

| 영역 | 상태 |
|---|---|
| 사양 V2.5 | 확정 — "실전 가동 라이브" 선언 |
| `wiki/areas/*` | 빈 스켈레톤 |
| `wiki/concepts/`, `wiki/sources/` | 빈 |
| `wiki/industries/*/` | 폴더만, 내부 빈 |
| `_index.db` 최근 갱신 | 2026-05-20 (V2.4 인제스트 시점) |
| `storage/_index.db` | 0바이트 |
| 시맨틱 검색 (`chunk_vec`/FAISS) | 코드 레벨 비활성 (주석) |
| MES 위키 | 중복 (`mes_생산_실행_시스템.md` vs `mes_생산실행시스템.md`) |
| lint 픽스처 | 잔존 (`z_lint_*.md`) |
| 표준 API `/api/v1/retrieval` + `X-IRIS-Caller` | 사양 단계, 현재 구현 `/wiki/*` |
| Quartz 본격 발행 | V2.6 이월 |

## 14. 재개발/유지보수 참고

- **흡수 결정 부록 (V2.5.1, 2026-06-05)**: 외부 LLM Wiki V1.0 사상 흡수/거부 매트릭스와 V2.6 로드맵 보강은 [/Users/iris/Documents/0Dev/docs/system/IRIS_V2.5.1_external_absorption_2026-06-05.md](../../docs/system/IRIS_V2.5.1_external_absorption_2026-06-05.md) 참조. V2.6 진입 시 K3 `kind` / `origin` 컬럼 + `lane='secure'` + Golden Q&A가 즉시 착수 항목.
- **새 wiki 페이지**: [_templates/page.md](../knowledge/wiki/_templates/page.md) 양식 + 품질 게이트 [IRIS_WIKI_QUALITY_RULES.md](../knowledge/IRIS_WIKI_QUALITY_RULES.md) 준수
- **인제스트 추가**: `apps/ingest/` 에 `reference_<source>.py` 추가 + Makefile 타깃
- **표준 API 구현 (V2.5 미완)**: `/api/v1/retrieval` 라우터 + `X-IRIS-Caller` 헤더 파싱 + mode dispatcher
- **시맨틱 검색 활성화**: Ollama 임베딩 + FAISS 인덱스 + `chunk_vec` 또는 외부 인덱스 결정
- **Quartz 발행**: `apps/quartz/` 에서 `npx quartz build` + 정적 호스팅
- **빈 스켈레톤 채움**: industries/areas 정본 콘텐츠 작성 (도메인 전문가 협업 필요)
- **MES 중복 정리**: `merge` 사용 또는 수동 통합
- **백업**: `knowledge/_index.db` 정기 스냅샷 + `wiki/` git 관리

## 참고

- 상위 IRIS 계층: [/Users/iris/Documents/0Dev/ARCHITECTURE.md](../../ARCHITECTURE.md)
- IRIS V2.5 사양: [/Users/iris/Documents/0Dev/docs/system/IRIS_V2.5_계층구조_2026-05-22.md](../../docs/system/IRIS_V2.5_계층구조_2026-05-22.md)
- IRIS V2.5.1 흡수 부록: [/Users/iris/Documents/0Dev/docs/system/IRIS_V2.5.1_external_absorption_2026-06-05.md](../../docs/system/IRIS_V2.5.1_external_absorption_2026-06-05.md)
- 외부 레퍼런스(LLM Wiki V1.0): [/Users/iris/Documents/0Dev/docs/system/reference/external_v1/](../../docs/system/reference/external_v1/)
- 다른 계층: [iris-claw](../../iris-claw/) (L1), [iris-stack](../../iris-stack/) (L2), [iris-memory](../../iris-memory/) (L3), [iris-gateway](../../iris-gateway/) (L4-C)
- 결합 시스템: [diagnosis-tool](../../diagnosis-tool/) (L6-D1)
