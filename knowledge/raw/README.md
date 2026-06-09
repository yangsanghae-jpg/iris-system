# docs — 문서 인덱스

문서는 두 가지 뷰로 접근할 수 있습니다:

- **Step별 뷰** ([by_step/](by_step/)) — Step1~6 흐름 관점으로 모든 문서를 step에 매핑
- **카테고리별 뷰** (아래) — 전체문서·시스템설계·개별개발·참조·백업 분류

---

## ⭐⭐ V2.0 종합 문서 (재개발 진입점)

> 시스템 구조·설계·개발·테스트·실행을 한 곳에 정리한 종합 문서 (한국어).
> 런타임은 V1.5 그대로, 문서 버전만 V2.0. 신규 합류자·재개발용.

| 영역 | 위치 |
|---|---|
| V2.0 인덱스 | [v2.0/README.md](v2.0/README.md) |
| 시스템 개요 | [v2.0/01_system_overview.md](v2.0/01_system_overview.md) |
| 아키텍처 | [v2.0/02_architecture.md](v2.0/02_architecture.md) |
| 데이터 모델 | [v2.0/03_data_model.md](v2.0/03_data_model.md) |
| Step 흐름 | [v2.0/04_step_flow.md](v2.0/04_step_flow.md) |
| 엔진 설계 (Ch0~Ch6) | [v2.0/05_engine_design.md](v2.0/05_engine_design.md) |
| API 계약 | [v2.0/06_api_contract.md](v2.0/06_api_contract.md) |
| 개발 가이드 | [v2.0/07_dev_guide.md](v2.0/07_dev_guide.md) |
| 테스트 가이드 | [v2.0/08_test_guide.md](v2.0/08_test_guide.md) |
| 운영 | [v2.0/09_operations.md](v2.0/09_operations.md) |
| ⭐ 재배포 지시서 | [v2.0/10_redeploy_guide.md](v2.0/10_redeploy_guide.md) |
| CHANGELOG v1.5→v2.0 | [v2.0/CHANGELOG_v1.5_to_v2.0.md](v2.0/CHANGELOG_v1.5_to_v2.0.md) |

---

## 🚀 Step별 뷰 (권장)

진단툴 흐름 (Step1 → Step1.5 → Step2 → ... → Step5 → Step6) 단위로 관련 문서를 모은 인덱스.

| 영역 | 위치 |
|---|---|
| 전체 인덱스 | [by_step/README](by_step/README.md) |
| 공통·아키텍처·계약 | [by_step/common](by_step/common.md) |
| Step1 — 산업 (A~H) | [by_step/step1](by_step/step1.md) |
| **Step1.5 — 세부 산업 + 대표 공정** ⭐ | [by_step/step1_5](by_step/step1_5.md) |
| Step2 — Routing 5종 | [by_step/step2](by_step/step2.md) |
| Step3 — Scale (S1~S4) | [by_step/step3](by_step/step3.md) |
| Step4 — Automation Level | [by_step/step4](by_step/step4.md) |
| Step5 — 컨설팅 보고서 (ch0~ch6) | [by_step/step5](by_step/step5.md) |
| Step6 — 자사 솔루션 카탈로그 | [by_step/step6](by_step/step6.md) |
| **Raw 데이터·가중치** ⭐ — step1~5 카탈로그 자동 추출 (ko/zh/en 37 md) | [by_step/data/](by_step/data/) |

## 🗂️ 산업·메타 문서 (별도 트리)

| 영역 | 위치 |
|---|---|
| 8대 산업 × v2 분지 제안 (ko/zh/en) | [industries/](industries/) |
| 산업 메타축 (value_chain, regulation_tier, theme v11) | [industries/_meta/](industries/_meta/) |
| Step1.5 → Step2 routing 매핑 데이터 | [industries/_mapping/](industries/_mapping/) |

---

## 📂 카테고리별 뷰

문서는 **전체 문서**와 **프로젝트 문서**로 구분하며, 프로젝트 문서는 다시 시스템 설계·개별 개발·참조·백업으로 분류합니다.

### 폴더 구조

```
docs/
├── by_step/                     # ⭐ Step별 인덱스 (신규)
│   ├── README.md
│   ├── common.md
│   ├── step1.md
│   ├── step1_5.md
│   ├── step2.md
│   ├── step3.md
│   ├── step4.md
│   ├── step5.md
│   └── step6.md
├── industries/                  # 산업·메타·매핑 (신규)
│   ├── README.md
│   ├── _meta/                   # value_chain / regulation_tier / theme_taxonomy_v2
│   ├── _mapping/                # sub_to_routing (ko/zh/en)
│   ├── A_project_special/       # ko/zh/en
│   ├── B_semiconductor/
│   ├── C_electronics_jobshop/
│   ├── D_panel_newenergy/
│   ├── E_process_chemical/
│   ├── F_consumer_food/
│   ├── G_pharma/
│   └── H_auto_mobility/
├── 전체문서/                    # 프로젝트 전반·아키텍처·운영 구조
├── 프로젝트문서/
│   ├── 시스템설계/              # 레이어·계약·설계서
│   ├── 개별개발/                # Step4·Step5·Step6·Migration·i18n
│   ├── 참조/                    # 실행·전환·설정 참조
│   └── 백업/                    # old·backup·reports (참조/보관용)
├── step4/                       # Step4 UI 구조 (V1.6)
├── step5/                       # Step5 베이스라인·Ch2 보고
├── releases/                    # 릴리즈 이력
├── history/                     # CH2 카드 릴리즈 history
└── README.md                    # 본 인덱스
```

---

## 1. 전체 문서

프로젝트 전체 구조·시스템 설계·UI/엔진/데이터 개요·운영 구조도.

| 문서 | 설명 |
|------|------|
| [전체문서/diagnosis-tool_전체_운영_구조도_V1.0.md](전체문서/diagnosis-tool_전체_운영_구조도_V1.0.md) | IRIS 환경 전체 운영 구조 (ChatGPT·Cursor·GitHub·맥 3대·백업) |
| [전체문서/01_overall_architecture.md](전체문서/01_overall_architecture.md) | 전체 구조 설계서 (요약·레이어·흐름) |
| [전체문서/02_system_design.md](전체문서/02_system_design.md) | 시스템 설계서 (API·배포) |
| [전체문서/03_ui_structure.md](전체문서/03_ui_structure.md) | UI 구조 설계서 (Step·챕터 규칙) |
| [전체문서/04_engine_structure.md](전체문서/04_engine_structure.md) | 엔진 구조 설계서 (파이프라인·챕터) |
| [전체문서/05_data_structure.md](전체문서/05_data_structure.md) | 데이터 구조 설계서 (Result·Knowledge·DB 계약) |
| [전체문서/06_start_stop.md](전체문서/06_start_stop.md) | 시스템 시작·종료 작업서 |
| [전체문서/07_data_and_reference.md](전체문서/07_data_and_reference.md) | 데이터 및 관련 설명서 (목차) |

---

## 2. 프로젝트 문서

### 2.1 시스템 설계 관련 문서

레이어별 상세·Step4/Step5 설계·계약·데이터 아키텍처.

| 위치 | 설명 |
|------|------|
| [프로젝트문서/시스템설계/architecture/](프로젝트문서/시스템설계/architecture/) | 레이어별 상세 설계 (00_overview ~ 05_layer5_llm_service) |
| [프로젝트문서/시스템설계/step4_design.md](프로젝트문서/시스템설계/step4_design.md) | Step4 설계 (4영역×5단계, 8산업 Baseline) |
| [프로젝트문서/시스템설계/step5_contract_v1.md](프로젝트문서/시스템설계/step5_contract_v1.md) | Step5 Contract JSON v1 |
| [프로젝트문서/시스템설계/contract_step5_engine_data.md](프로젝트문서/시스템설계/contract_step5_engine_data.md) | Step5 엔진·데이터·UI 계약 |
| [프로젝트문서/시스템설계/step5_structure_overview.md](프로젝트문서/시스템설계/step5_structure_overview.md) | Step5 전체 구조·DOM·로직 |
| [프로젝트문서/시스템설계/data_architecture_vNext.md](프로젝트문서/시스템설계/data_architecture_vNext.md) | 데이터 아키텍처 (Result/Fixed/Extended/Rules) |

### 2.2 개별 개발 관련 문서

Step4·Step5·Step6·Migration·i18n 상세.

| 위치 | 설명 |
|------|------|
| [프로젝트문서/개별개발/step5/](프로젝트문서/개별개발/step5/) | Step5·Ch1/Ch2 상세 (챕터 참조, CH2 엔진·카드, 검증, DB 점검 등) |
| [프로젝트문서/개별개발/step4/](프로젝트문서/개별개발/step4/) | Step4 UI 요약·로드맵 |
| [프로젝트문서/개별개발/step6/](프로젝트문서/개별개발/step6/) | Step6 UI 구조 |
| [프로젝트문서/개별개발/migration/](프로젝트문서/개별개발/migration/) | Migration v2·P1/P2·B단계 |
| [프로젝트문서/개별개발/i18n/](프로젝트문서/개별개발/i18n/) | i18n 체크리스트·v15 구현 |

### 2.3 참조 관련 문서

실행·전환·설정·쿼리 참조.

| 문서 | 설명 |
|------|------|
| [프로젝트문서/참조/app_run_queries.md](프로젝트문서/참조/app_run_queries.md) | app_run.db 쿼리 세트 |
| [프로젝트문서/참조/m2_single_host_setup.md](프로젝트문서/참조/m2_single_host_setup.md) | M2 단일 호스트 설정 |
| [프로젝트문서/참조/version_switch_procedure.md](프로젝트문서/참조/version_switch_procedure.md) | v1.0/v1.5 전환 절차 |
| [프로젝트문서/참조/worktree_v1_v15_setup.md](프로젝트문서/참조/worktree_v1_v15_setup.md) | worktree v1/v1.5 설정 |

### 2.4 백업 문서

과거 분석·지시서·백업·보고서 (참조/보관용).

| 위치 | 설명 |
|------|------|
| [프로젝트문서/백업/old/](프로젝트문서/백업/old/) | 과거 분석·지시서·백업 |
| [프로젝트문서/백업/backup_20260311/](프로젝트문서/백업/backup_20260311/) | 2026-03-11 문서 정리 시 백업 |
| [프로젝트문서/백업/reports/](프로젝트문서/백업/reports/) | ROI 리팩터·LLM ON/OFF 테스트 등 보고서 |

---

## 빠른 링크

- **운영 구조**: [전체문서/diagnosis-tool_전체_운영_구조도_V1.0.md](전체문서/diagnosis-tool_전체_운영_구조도_V1.0.md)
- **Step5 챕터 참조**: [프로젝트문서/개별개발/step5/step5_chapters_reference.md](프로젝트문서/개별개발/step5/step5_chapters_reference.md)
- **CH2 엔진·데이터**: [프로젝트문서/개별개발/step5/CH2_ENGINE_AND_DATA_REFERENCE.md](프로젝트문서/개별개발/step5/CH2_ENGINE_AND_DATA_REFERENCE.md)
- **v1.0/v1.5 전환**: [프로젝트문서/참조/version_switch_procedure.md](프로젝트문서/참조/version_switch_procedure.md)
