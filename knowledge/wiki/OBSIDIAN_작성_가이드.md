---
title: Obsidian 작성 가이드 (IRIS Gold Wiki)
industry: ""
area: planning
level: L0
status: published
trust: verified
sources: []
tags: [guide, k6, obsidian]
---

# Obsidian 작성 가이드 — IRIS Gold Wiki

> **대상:** `iris-system/knowledge/wiki/` 를 Obsidian vault로 쓰는 사람  
> **목적:** 지금처럼 루트에 파일이 흩어지지 않게, **관리해서 넣는** 규칙을 한 장으로 정리

---

## 1. 먼저 구분 (헷갈리지 않기)

| 구분 | 위치 | 넣는 방식 |
|------|------|-----------|
| **Gold (공식 지식)** | `knowledge/wiki/` 이 vault | 아래 규칙 **필수** |
| **개인 초안·구조도** | vault **밖** (`knowledge/통합 구조도.md` 등) | 자유. Gold에 올릴 때만 이관 |
| **Silver / raw** | `knowledge/raw/`, `staging/` | Obsidian wiki에 **직접 넣지 않음** (파이프라인 후 Gold) |

**Quartz(:8080)** 는 `wiki/` 만 보여 줍니다. vault 루트가 `knowledge/` 전체면, Obsidian 트리와 Quartz 트리가 **다르게** 보일 수 있습니다.  
**권장:** Obsidian vault 폴더 = **`knowledge/wiki/`** 만 연다.

---

## 2. 새 노트 만드는 순서 (5분 체크리스트)

### ① 어디에 둘지 정한다

```
wiki/
├── index.md                 ← 홈 (건드리지 않음)
├── architecture/            ← IRIS 사양·버전 이력만
├── industries/              ← 산업별 (A~H)
│   └── B_semiconductor_fab_backend/
│       └── (주제).md
├── areas/                   ← 영역 횡단 (planning, quality, …)
├── concepts/                ← MES, APS, SPC 등 공통 개념
├── sources/                 ← 출처·클리핑 메모
├── _templates/              ← 템플릿만 (본문 노트 아님)
└── (루트에 새 md 넣지 말 것)  ← ❌ mes_xxx.md 흩어짐 방지
```

| 내용 유형 | 넣을 폴더 |
|-----------|-----------|
| 반도체 Fab, CIM, 공정 | `industries/B_semiconductor_fab_backend/` |
| MES/APS/SPC 일반 개념 | `concepts/` |
| 계획·품질·설비·물류 (산업 공통) | `areas/planning` 등 |
| IRIS V2.x 계층·로드맵 | `architecture/` |
| URL·문헌·근거 | `sources/` |

**산업 코드 (파일명·frontmatter):**

| 코드 | 폴더 |
|------|------|
| A | `A_project_eto_ato` |
| B | `B_semiconductor_fab_backend` |
| C | `C_electronics_discrete_highmix` |
| D | `D_panel_newenergy_lineflow` |
| E | `E_process_chemical` |
| F | `F_fmcg_food` |
| G | `G_pharma_bio` |
| H | `H_auto_mobility` |

### ② 템플릿으로 시작

1. Obsidian: **템플릿** → `_templates/page.md` 복사  
2. 또는: 해당 산업 폴더에서 새 노트 → frontmatter 붙이기

### ③ frontmatter 채우기 (필수)

```yaml
---
title: "반도체 CIM 개요"          # 화면 제목 (비우지 말 것)
industry: "B"                      # A~H 하나
area: "equipment"                  # planning | quality | equipment | logistics
level: "L2"                        # L0~L4
status: "draft"                    # draft → review → published
trust: "verified"                  # verified | clipped | auto
sources: []                        # 출처 있으면 doc_id/url
tags: []
---
```

### ④ 본문 최소 구조

```markdown
## 요약
(2~3문장)

## 핵심 개념
- ...

## 관련 링크
- [[B_semiconductor_fab_backend]]   ← 산업 허브
- [[concepts]]                      ← 필요 시

## 출처 노트
- (선택)
```

- 본문 **320자 이상**, wikilink **최소 1개** 권장 (lint `weak_pages` 방지)
- 제목은 파일 상단 `#` 또는 frontmatter `title` 중 하나로 통일

### ⑤ 파일 이름

- **영문 snake_case** 권장: `cim_system_overview.md`
- 루트에 `mes_생산_실행_시스템.md` 처럼 두지 말고 → `industries/.../mes_production_execution.md` 로 이동
- **같은 주제 중복 파일** (`mes_생산_실행` / `mes_생산실행` 두 개) → 하나로 합치고 다른 쪽은 삭제 또는 redirect 링크

### ⑥ 저장 후 점검

```bash
cd /Users/iris/Documents/0Dev/iris-system
python3 apps/wiki/lint.py
```

- `broken_links` → 링크 대상 문서 만들거나 `[[이름]]` 수정  
- `orphan_pages` → 다른 노트에서 `[[이 문서]]` 로 연결  
- `z_lint_*.md` → **lint 테스트용**이므로 본문 작업 노트로 쓰지 말 것

### ⑦ git (정본 기록)

```bash
cd /Users/iris/Documents/0Dev/iris-system
git add knowledge/wiki/
git commit -m "wiki: add/update (주제 한 줄)"
```

---

## 3. 지금 정리가 필요한 것 (현재 vault 기준)

| 상태 | 파일/위치 | 조치 |
|------|-----------|------|
| ❌ 루트 흩어짐 | `wiki/mes_*.md` (2개) | `industries/.../` 또는 `concepts/` 로 **이동** 후 wikilink 수정 |
| ⚠️ 테스트 전용 | `z_lint_broken.md`, `z_lint_orphan.md` | 그대로 두되 **새 글 아님** — lint 샘플 |
| ⚠️ vault 밖 | `knowledge/통합 구조도.md` | Gold에 넣을 거면 `architecture/` 또는 `concepts/` 로 **복사·정리** |
| ✅ 허브 | `index.md`, `architecture/*` | 유지 |
| 📁 빈 폴더 | `industries/*/`, `areas/*/` | 노트 추가 시 여기에만 생성 |

---

## 4. Obsidian에서 쓰면 좋은 습관

1. **Daily / 무제 노트** → `wiki/` 밖 개인 vault에 두기  
2. **Gold로 승격할 때만** `wiki/` 아래에 생성  
3. 그래프뷰에서 고립 노트 보이면 → 관련 문서에 `[[링크]]` 한 줄 추가  
4. IRIS 사양·버전 문서는 **`architecture/`** 만 수정 (운영 지식과 분리)  
5. Quartz 미리보기: 호스트에서 `cd iris-system/apps/quartz && npx quartz build --serve` 후 **http://localhost:8080** 확인 (VM에서는 `http://10.211.55.2:8080`)

---

## 5. 하지 말 것

- `wiki/` 루트에 주제 md **난사** (지금 너저분함의 주원인)
- frontmatter 없이 장문만 쓰기
- 깨진 `[[링크]]` 방치 (lint block)
- Silver/raw를 wiki에 직접 복붙 (검수·lane 구분 깨짐)
- Obsidian sync 플러그인으로 **다른 vault와 자동 합치기** (git 정본과 충돌)

---

## 6. 자주 묻는 것

**Q. 그냥 추가하면 안 되나?**  
A. Obsidian에는 자유롭게. **이 폴더(`wiki/`)** 에는 “공식 지식”만, 규칙대로.

**Q. 저장하면 IRIS 전체가 아나?**  
A. 아니요. 파일 변경 + (선택) lint/git/Quartz 재빌드로만 반영. Open WebUI memory와 **무관**.

**Q. 본문 형식이 아직 미확정인데?**  
A. frontmatter + 요약/핵심/링크/출처 **최소 골격**만 지키고, 3~5개 샘플 쌓인 뒤 `_templates/page.md` 를 팀이 갱신.

---

## 7. 관련 문서

- [[index]] — 지식센터 홈  
- [IRIS_WIKI_QUALITY_RULES.md](../IRIS_WIKI_QUALITY_RULES.md) — lint·merge 정책  
- `_templates/page.md` — frontmatter 표준  

---

*최종 수정: 2026-05-22 · K6 Curate 운영용*
