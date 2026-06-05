---
title: IRIS Knowledge Center (L4-K)
---

# IRIS 지식센터 — L4-K Gold Vault

V2.3 사양: `iris-system/knowledge/wiki/` = K4 Gold tier · Obsidian vault · git 정본.
편집은 [K6 Curate](../CLAUDE.md)에서. 본 vault는 **사람 검수를 통과한 최종본**만 들어옵니다.

## 분류 축

V2.3 매트릭스: **8산업(A~H) × 4영역 × 5단계(L0~L4)**

### 산업 (`industries/`) — diagnosis-tool `industry_master.json` 기준

- [[A_project_eto_ato]] — 프로젝트·특수 제조 (ETO/ATO)
- [[B_semiconductor_fab_backend]] — 반도체 (Fab/Backend)
- [[C_electronics_discrete_highmix]] — 전자·정밀 이산 (다품종)
- [[D_panel_newenergy_lineflow]] — 디스플레이·신에너지 (Line Flow)
- [[E_process_chemical]] — 공정화·화학
- [[F_fmcg_food]] — 소비재·식품
- [[G_pharma_bio]] — 의약 (Pharma/Bio)
- [[H_auto_mobility]] — 자동차·모빌리티

### 영역 (`areas/`)

- [[planning]] · [[quality]] · [[equipment]] · [[logistics]]

### 기타

- [[concepts]] — 산업·영역 횡단 개념 (MES, APS, SPC 등)
- [[sources]] — 1차 자료 노트 (raw/staging 추적)
- [[architecture/index|architecture]] — IRIS V2.x 계층구조 사양 이력
- `_templates/page.md` — frontmatter 표준

## 운영 규칙

- frontmatter 필수: `industry / area / level / status / trust / sources[]`
- 본문 구조는 V2.3에서 **미확정** — 첫 3~5개 샘플로 패턴 발견 후 템플릿화
- 품질 규칙: [IRIS_WIKI_QUALITY_RULES.md](../IRIS_WIKI_QUALITY_RULES.md), [lint.py](../../apps/wiki/lint.py)
- 승격 게이트(Silver→Gold): 사람 검수 + lint 통과 (자동 금지)

## 소비자

- **L6-D1 diagnosis** → K5-① 매트릭스 조회 (`industry/area/level`)
- **L6-R 보고서** → K5-② 키워드 + K5-① 매트릭스
- **L6-C 대화** → L2 Gateway가 K5 호출 (검토 단계)
