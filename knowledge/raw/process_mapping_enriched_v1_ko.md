# 세부 산업별 제조 공정 상세 맵핑 보완안 v1

> 작성 기준: 업로드된 `industries_sub_industries_ko_zh.md`의 8대 산업/49개 세부 산업 구조와 `process_analysis_raw_v0.md`의 기존 raw 라우팅·MVP·KPI 구조를 유지하면서, 공정 상세·라우팅 해석·핵심 관리 포인트를 보강한 버전.

> 목적: Step1.5 세부 산업 선택 이후 Step3/Step5에서 “실제 공정 흐름이 보이는” 결과를 생성할 수 있도록 데이터화 가능한 기준 문구 제공.


## 0. 라우팅 타입 정의

- **RT_PROJECT** — 프로젝트형(Project/ETO): 고객/프로젝트/사이트 단위로 WBS·자재·도면·공정이 묶이며, 동일 제품 반복보다 단계 게이트와 변경관리, 장납기 자재, 현장 진도가 핵심이다.
- **RT_REENTRANT** — 재진입형(Re-entrant): 동일 설비군/공정군을 여러 번 반복 통과한다. Lot 우선순위, Q-time, 레시피, 챔버/마스크/캐리어 이력, 병목 디스패칭이 CT와 수율을 좌우한다.
- **RT_BATCH** — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.
- **RT_LINE** — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.
- **RT_JOBSHOP** — 잡샵형(Job-shop/High-mix): 제품·고객·옵션별 라우팅이 다르며, 공정 경로가 유연하다. WO별 routing version, 대체 설비, setup, 작업자 숙련도, WIP 위치와 납기 우선순위가 핵심이다.

## 1. 데이터화 권장 필드


```json
{
  "slug": "sub_industry_code",
  "routing_type": "RT_LINE | RT_BATCH | RT_REENTRANT | RT_PROJECT | RT_JOBSHOP",
  "process_steps_ko": ["8~15개 상세 공정"],
  "routing_explanation_ko": "해당 산업에서 라우팅이 왜 그렇게 동작하는지",
  "control_points_ko": ["5~8개 현장 일일 관리 포인트"],
  "data_capture_points": ["lot_id", "equipment_id", "recipe_id", "operator_id", "inspection_result", "hold_release_status"]
}
```


# A. 프로젝트형 제조 / 项目型制造


## A-1. 플랜트 EPC / 工厂 EPC

- `slug`: `plant_epc`
- `routing`: `RT_PROJECT` — 프로젝트형(Project/ETO): 고객/프로젝트/사이트 단위로 WBS·자재·도면·공정이 묶이며, 동일 제품 반복보다 단계 게이트와 변경관리, 장납기 자재, 현장 진도가 핵심이다.

### 공정 상세
1. 사업성/기본 요구 확정 — 생산능력·공법·부지·유틸리티·인허가 조건을 정의
2. FEED/기본설계 — PFD/P&ID, 장비 리스트, 공정 조건, 배치 개념 확정
3. 상세설계 — 배관·전기·계장·토건·구조 도면과 MTO 산출
4. 장납기 기자재 발주 — 압력용기, 반응기, 압축기, 전기실, DCS/PLC 등 조달
5. Vendor document review — 승인도, FAT 계획, 인터페이스 조건 검토
6. 현장 토건/기초 공사 — 토목, 철골, 기초, 배수, 접지 시공
7. 기계·배관·전기·계장 설치 — 배관 spool, 케이블, 계기, 제어반 설치
8. Pre-commissioning — flushing, blowing, loop check, pressure/leak test
9. Commissioning/Start-up — cold/hot commissioning, 성능시험, punch close
10. 인수인계 — as-built, O&M 매뉴얼, spare part, 교육, PAC/FAC

### 핵심 관리 포인트
- WBS·도면·자재코드·계약 패키지의 일치성
- 장납기 기자재 납기와 현장 설치 가능일의 동기화
- 설계 변경/현장 변경에 따른 MTO·비용·일정 영향 추적
- 검사/시험 기록 압력시험, loop check, FAT/SAT의 서명 상태
- Punch list severity와 미결 항목 aging
- 시운전 조건, interlock bypass, temporary line 제거 이력
- 하도급 작업 진도와 실제 물량 progress 검증

### MES/데이터 수집 포인트
`project_id`, `WBS/activity_id`, `drawing_revision`, `material_package`, `vendor_document_status`, `inspection_record`, `punch_status`, `progress_qty`


## A-2. 중공업 장비 / 重工业装备

- `slug`: `heavy_equipment`
- `routing`: `RT_PROJECT` — 프로젝트형(Project/ETO): 고객/프로젝트/사이트 단위로 WBS·자재·도면·공정이 묶이며, 동일 제품 반복보다 단계 게이트와 변경관리, 장납기 자재, 현장 진도가 핵심이다.

### 공정 상세
1. 수주 사양 검토 — 고객 도면, 용량, 하중, 인증 조건 확인
2. 기본/상세 설계 — 구조·구동·유압·전장 설계 및 BOM 확정
3. 대형 소재 조달 — 주조품, 단조품, 강판, 베어링, 모터 등 발주
4. 소재 입고/검사 — 성적서, 열번호, 치수, 내부 결함 확인
5. 절단·용접·열처리 — 대형 구조물 제작 및 응력 제거
6. 대형 정밀가공 — 보링, 밀링, 선삭, 기어 가공
7. 표면처리/도장 — shot blasting, primer, top coat
8. 서브모듈 조립 — 유압, 전장, 구동부, 안전장치 조립
9. 최종 조립/정렬 — 베이스 레벨링, 축정렬, 간극 조정
10. 무부하/부하 시험 — 진동, 온도, 토크, 성능 테스트
11. 분해/포장/출하 — 운송 분할, 방청, 현장 설치 준비

### 핵심 관리 포인트
- 소재 heat number와 부품 serial의 추적
- 용접 WPS/PQR, 용접사 자격, NDT 결과
- 가공 기준면과 누적 공차 관리
- 대형품 외주가공 납기와 검사 성적서 회수
- 조립 축정렬, run-out, backlash, 체결 torque 기록
- 도장 두께·표면 조도·건조 조건
- FAT 불합격 항목의 원인/재시험 이력

### MES/데이터 수집 포인트
`project_id`, `WBS/activity_id`, `drawing_revision`, `material_package`, `vendor_document_status`, `inspection_record`, `punch_status`, `progress_qty`


## A-3. 반도체 장비 / 半导体装备

- `slug`: `semi_equipment`
- `routing`: `RT_PROJECT` — 프로젝트형(Project/ETO): 고객/프로젝트/사이트 단위로 WBS·자재·도면·공정이 묶이며, 동일 제품 반복보다 단계 게이트와 변경관리, 장납기 자재, 현장 진도가 핵심이다.

### 공정 상세
1. 고객 URS/SEMI 요구 검토 — 청정도, safety, host interface, utility 조건 정의
2. 시스템 설계 — chamber, robot, vacuum, gas, RF, thermal, EFEM 설계
3. 정밀 부품 가공/세정 — chamber part, stage, showerhead, gas line 제작
4. 전장/제어 제작 — PLC/IPC, interlock, recipe, SECS/GEM 구성
5. 모듈 조립 — vacuum module, transfer module, gas box, RF box 조립
6. 클린 조립/particle 관리 — cleanroom 조립, leak check, particle baseline
7. SW/Recipe 통합 — sequence, alarm, interlock, host command 검증
8. Factory Acceptance Test — wafer handling, repeatability, process uniformity 검증
9. Decontamination/포장 — 청정 포장, shock/vibration 대비
10. Site installation/SAT — utility hook-up, exhaust, gas, host 연동, qualification

### 핵심 관리 포인트
- BOM/도면 revision과 장비 serial의 freeze 상태
- 청정 세정 등급, particle count, 잔류 이온/유기물 관리
- vacuum leak rate, base pressure, pump-down time
- robot teach point, wafer handling misalign/slot error
- interlock bypass 사용 이력과 해제 승인
- recipe parameter lock과 변경 승인
- SECS/GEM event/alarm mapping 완성도
- FAT/SAT item별 pass/fail 및 고객 waiver

### MES/데이터 수집 포인트
`project_id`, `WBS/activity_id`, `drawing_revision`, `material_package`, `vendor_document_status`, `inspection_record`, `punch_status`, `progress_qty`


## A-4. 디스플레이 장비 / 显示装备

- `slug`: `display_equipment`
- `routing`: `RT_PROJECT` — 프로젝트형(Project/ETO): 고객/프로젝트/사이트 단위로 WBS·자재·도면·공정이 묶이며, 동일 제품 반복보다 단계 게이트와 변경관리, 장납기 자재, 현장 진도가 핵심이다.

### 공정 상세
1. 고객 glass size/세대/공정 사양 검토
2. 광학·기구·제어 설계 — 정렬, coating, bonding, 검사 모듈 설계
3. 정밀 프레임/스테이지 가공
4. 반송/핸들링 모듈 제작 — 대면적 glass 처짐·파손 방지
5. 광학계/카메라/조명 조립
6. 진공/열/UV/압착 모듈 조립
7. 제어 SW/알고리즘 통합 — alignment, recipe, vision 검사
8. 공정 샘플 테스트 — 균일도, 정렬도, defect 검출력 검증
9. FAT — tact, 반복정밀도, glass breakage 검증
10. 현장 설치/SAT — 라인 인터페이스, host, material handling 연동

### 핵심 관리 포인트
- glass size별 recipe와 jig/fixture 매칭
- 스테이지 평탄도·반복정밀도·열변형
- 광학 보정값, 카메라 calibration, 조명 aging
- glass breakage/edge chip 원인 기록
- cleanliness와 particle/foreign material 관리
- 라인 tact와 upstream/downstream handshake
- 검사 알고리즘 false call/miss call 비율

### MES/데이터 수집 포인트
`project_id`, `WBS/activity_id`, `drawing_revision`, `material_package`, `vendor_document_status`, `inspection_record`, `punch_status`, `progress_qty`


## A-5. 배터리 장비 / 电池装备

- `slug`: `battery_equipment`
- `routing`: `RT_PROJECT` — 프로젝트형(Project/ETO): 고객/프로젝트/사이트 단위로 WBS·자재·도면·공정이 묶이며, 동일 제품 반복보다 단계 게이트와 변경관리, 장납기 자재, 현장 진도가 핵심이다.

### 공정 상세
1. 고객 cell format/공정능력 요구 정의 — cylindrical/prismatic/pouch, ppm, dry-room 조건
2. 기본 설계 — coating, calendering, slitting, stacking/winding, formation 장비 구성
3. 정밀 롤/노즐/금형 제작
4. 구동·장력·비전·계측 모듈 조립
5. dry-room/방폭/집진/solvent 대응 설계 반영
6. 제어 SW/recipe/traceability 구현
7. 공정 샘플 시험 — 코팅 균일도, burr, alignment, tension 검증
8. 안전 시험 — interlock, fire/explosion, emergency 대응
9. FAT — speed, yield, parameter window 검증
10. 현장 설치/SAT — utility, MES/SCADA, dry-room 안정화

### 핵심 관리 포인트
- 제품 format별 교체부품/changeover 조건
- roll gap, web tension, edge alignment 관리
- 분진/금속 이물, dry-room dew point
- coating/press/slit 핵심 파라미터 수집 주기
- 방폭·solvent exhaust·집진 interlock
- 비전 검사 defect code와 실제 불량 매칭
- 고객 소재별 recipe parameter window

### MES/데이터 수집 포인트
`project_id`, `WBS/activity_id`, `drawing_revision`, `material_package`, `vendor_document_status`, `inspection_record`, `punch_status`, `progress_qty`


## A-6. 항공·우주 장비 / 航空航天装备

- `slug`: `aerospace_equipment`
- `routing`: `RT_PROJECT` — 프로젝트형(Project/ETO): 고객/프로젝트/사이트 단위로 WBS·자재·도면·공정이 묶이며, 동일 제품 반복보다 단계 게이트와 변경관리, 장납기 자재, 현장 진도가 핵심이다.

### 공정 상세
1. 요구/인증 기준 검토 — AS9100, 고객 spec, 소재/공정 승인 조건
2. 설계 및 configuration baseline 확정
3. 소재 구매/입고 — 항공 소재 성적서, lot, heat trace 확보
4. 정밀가공 — 5축, 난삭재 가공, 공정 중 치수검사
5. 특수공정 — 열처리, shot peening, coating, bonding
6. NDT — UT, RT, PT, MT 등 비파괴검사
7. 서브조립 — 구조, 배관, 전장 harness 조립
8. 기능/환경 시험 — vibration, thermal, pressure, leak, EMI
9. 최종 검사/FAI — First Article Inspection 및 문서 패키지
10. 출하/수명주기 문서 인계

### 핵심 관리 포인트
- 소재 mill certificate와 부품 serial 추적
- 특수공정 승인 공장/작업자/조건 기록
- FAI balloon drawing과 치수 결과 일치
- NDT 판정자 자격과 defect disposition
- configuration change와 deviation/waiver 승인
- 체결 torque, locking, sealant cure time
- 시험 장비 calibration 유효성

### MES/데이터 수집 포인트
`project_id`, `WBS/activity_id`, `drawing_revision`, `material_package`, `vendor_document_status`, `inspection_record`, `punch_status`, `progress_qty`


## A-7. 조선 / 船舶制造

- `slug`: `shipbuilding`
- `routing`: `RT_PROJECT` — 프로젝트형(Project/ETO): 고객/프로젝트/사이트 단위로 WBS·자재·도면·공정이 묶이며, 동일 제품 반복보다 단계 게이트와 변경관리, 장납기 자재, 현장 진도가 핵심이다.

### 공정 상세
1. 선주 요구/기본설계 — 선종, 선급, 주요 제원, GA 확정
2. 상세/생산설계 — block division, piping/electrical spool, outfitting plan
3. 강재 입고/전처리 — shot blasting, primer, heat number 관리
4. 절단/성형 — CNC cutting, bending, beveling
5. 소조/중조/대조립 — panel line, sub-block, block 제작
6. 선행의장 — pipe, cable tray, equipment foundation 사전 설치
7. 도장 — block painting, tank coating, corrosion protection
8. 탑재/erection — dock/berth에서 block 탑재 및 용접
9. 진수 — watertight, underwater work 완료 후 launch
10. 안벽 의장/시운전 — 기계·전기·항해 장비 commissioning
11. 해상시운전/인도 — speed, maneuvering, safety, class inspection

### 핵심 관리 포인트
- block 단위 진도와 실제 물량 earned value
- 강재 heat number와 block/plate trace
- 용접 seam별 WPS, NDT, repair rate
- 도장 DFT, 표면처리 grade, 환경조건
- 선행의장율과 탑재 전 미완료 작업
- 선급 검사 hold point와 승인 상태
- block 탑재 순서와 크레인/도크 부하
- punch item close와 sea trial defect 처리

### MES/데이터 수집 포인트
`project_id`, `WBS/activity_id`, `drawing_revision`, `material_package`, `vendor_document_status`, `inspection_record`, `punch_status`, `progress_qty`


## A-8. 특수 구조물 제조 / 特殊结构制造

- `slug`: `special_structural`
- `routing`: `RT_PROJECT` — 프로젝트형(Project/ETO): 고객/프로젝트/사이트 단위로 WBS·자재·도면·공정이 묶이며, 동일 제품 반복보다 단계 게이트와 변경관리, 장납기 자재, 현장 진도가 핵심이다.

### 공정 상세
1. 고객 도면/구조 계산 검토
2. 소재 조달 — 형강, 강판, 철근, 특수 소재
3. 절단/개선 — CNC cutting, drilling, beveling
4. 성형/벤딩 — plate rolling, bending
5. 가조립/fit-up — 치수 기준점 확인
6. 용접/접합 — WPS 기반 구조 용접
7. 열처리/응력제거 필요시 수행
8. NDT/치수검사 — UT/RT/PT/MT, 3D scan
9. 표면처리/방청/도장
10. 현장 운송/설치/시공 시험

### 핵심 관리 포인트
- 도면 revision과 현장 설치 interface 확인
- 소재 성적서·heat number 추적
- fit-up gap, root face, weld sequence
- 용접 변형과 치수 누적오차
- NDT defect 위치/보수 이력
- 도장 전 표면조도·염분·습도
- 운송 lifting point와 변형/손상 기록

### MES/데이터 수집 포인트
`project_id`, `WBS/activity_id`, `drawing_revision`, `material_package`, `vendor_document_status`, `inspection_record`, `punch_status`, `progress_qty`


# B. 반도체 제조 / 半导体制造


## B-1. 로직/파운드리 / 逻辑/代工

- `slug`: `logic_foundry`
- `routing`: `RT_REENTRANT` — 재진입형(Re-entrant): 동일 설비군/공정군을 여러 번 반복 통과한다. Lot 우선순위, Q-time, 레시피, 챔버/마스크/캐리어 이력, 병목 디스패칭이 CT와 수율을 좌우한다.

### 공정 상세
1. 웨이퍼 입고/lot release
2. 산화/박막 증착 — CVD/PVD/ALD 등 막 형성
3. 포토 공정 — coat, bake, exposure, develop
4. 식각 — plasma/wet etch로 패턴 전사
5. PR strip/clean — 잔류물 제거
6. 이온주입/확산·어닐 — 도핑 및 활성화
7. CMP — 평탄화 및 두께 제어
8. 계측/검사 — CD, overlay, film thickness, defect inspection
9. 반복 layer build — FEOL/MOL/BEOL 재진입 반복
10. 금속 배선/패시베이션
11. 웨이퍼 sort/EDS
12. 출하 또는 패키징 인계

### 핵심 관리 포인트
- lot별 route step/rework/hold 상태
- mask ID, exposure tool, overlay/CD trend
- chamber/recipe/wafer slot genealogy
- Q-time window와 queue aging
- film thickness/uniformity, etch depth, CMP removal rate
- defect map과 공정 step 매핑
- SPC violation과 APC feedback 적용 여부
- FOUP/reticle/chemical batch 추적

### MES/데이터 수집 포인트
`lot_id`, `route_step`, `equipment_id`, `recipe_id`, `carrier_id`, `mask_or_reticle_id`, `Q_time`, `metrology_result`, `defect_map`


## B-2. 메모리(DRAM/NAND) / 存储(DRAM/NAND)

- `slug`: `memory_dram_nand`
- `routing`: `RT_REENTRANT` — 재진입형(Re-entrant): 동일 설비군/공정군을 여러 번 반복 통과한다. Lot 우선순위, Q-time, 레시피, 챔버/마스크/캐리어 이력, 병목 디스패칭이 CT와 수율을 좌우한다.

### 공정 상세
1. 웨이퍼 start
2. FEOL transistor/array 형성
3. 포토/식각/증착 반복
4. capacitor 또는 3D NAND stack deposition
5. high aspect ratio etch/channel 형성
6. wordline/bitline 형성
7. CMP/clean 반복
8. periphery circuit 형성
9. metallization/BEOL
10. wafer sort 및 repair/binning
11. KGD 판정 후 패키징 인계

### 핵심 관리 포인트
- cell array layer별 CD/overlay/etch profile
- 3D NAND stack 막 두께·응력·균일도
- HAR etch endpoint와 profile control
- wafer map 기반 die repair/binning
- Q-time 민감 공정 대기시간
- furnace/batch load 구성과 slot effect
- particle/metal contamination trend
- 공정 변경 시 device parameter drift

### MES/데이터 수집 포인트
`lot_id`, `route_step`, `equipment_id`, `recipe_id`, `carrier_id`, `mask_or_reticle_id`, `Q_time`, `metrology_result`, `defect_map`


## B-3. 아날로그/혼성신호 / 模拟/混合信号

- `slug`: `analog_mixed`
- `routing`: `RT_REENTRANT` — 재진입형(Re-entrant): 동일 설비군/공정군을 여러 번 반복 통과한다. Lot 우선순위, Q-time, 레시피, 챔버/마스크/캐리어 이력, 병목 디스패칭이 CT와 수율을 좌우한다.

### 공정 상세
1. 웨이퍼 fab start
2. well/isolation 형성
3. resistor/capacitor/inductor 등 precision device 형성
4. CMOS/Bipolar/BCD 공정 반복
5. trim structure 형성
6. metal interconnect
7. passivation/opening
8. wafer probe
9. laser/e-fuse trim·calibration
10. package assembly
11. final test/temperature test

### 핵심 관리 포인트
- precision resistor/capacitor 공정 편차
- trim 전후 parameter drift
- 고전압/저누설 공정 isolation 관리
- wafer probe bin과 final test correlation
- 온도 조건별 calibration data
- fab lot과 package lot genealogy
- ESD/latch-up 관련 test failure trend

### MES/데이터 수집 포인트
`lot_id`, `route_step`, `equipment_id`, `recipe_id`, `carrier_id`, `mask_or_reticle_id`, `Q_time`, `metrology_result`, `defect_map`


## B-4. 전력/디스크리트 / 功率/分立

- `slug`: `power_discrete`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. substrate/epi wafer 준비
2. 산화/포토/식각으로 cell pattern 형성
3. 이온주입/확산 및 activation
4. trench/gate 형성
5. metal deposition 및 backside grinding/metallization
6. wafer probe
7. dicing
8. die attach/clip 또는 wire bonding
9. molding/encapsulation
10. plating/trim/form
11. burn-in/reliability screen
12. final test/binning

### 핵심 관리 포인트
- epi thickness/resistivity와 wafer lot trace
- diffusion/furnace batch profile
- trench depth/gate oxide integrity
- backside thickness/warpage
- die attach void, bond pull/shear
- high current/thermal resistance test trend
- burn-in 조건과 failure mode
- AEC/JEDEC 신뢰성 lot 관리

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


## B-5. 광·센서 / 光学/传感

- `slug`: `optical_sensor`
- `routing`: `RT_REENTRANT` — 재진입형(Re-entrant): 동일 설비군/공정군을 여러 번 반복 통과한다. Lot 우선순위, Q-time, 레시피, 챔버/마스크/캐리어 이력, 병목 디스패칭이 CT와 수율을 좌우한다.

### 공정 상세
1. sensor wafer fab start
2. photodiode/CMOS pixel 형성
3. color filter/microlens 형성
4. passivation/opening
5. wafer-level optical/electrical test
6. backgrinding/dicing
7. optical alignment/attach
8. package/lens/filter assembly
9. calibration — dark current, sensitivity, color, focus
10. final optical/electrical test

### 핵심 관리 포인트
- pixel defect map과 wafer defect correlation
- color filter/microlens alignment
- dark current/noise/sensitivity drift
- 광학 부품 lot와 sensor die 매칭
- cleanliness/particle/foreign material
- calibration recipe와 test environment
- package stress와 focus shift

### MES/데이터 수집 포인트
`lot_id`, `route_step`, `equipment_id`, `recipe_id`, `carrier_id`, `mask_or_reticle_id`, `Q_time`, `metrology_result`, `defect_map`


## B-6. 화합물 반도체(SiC/GaN) / 化合物半导体(SiC/GaN)

- `slug`: `compound_semi`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. 원료 정제/seed 준비
2. bulk crystal growth — SiC boule 또는 GaN substrate
3. slicing/lapping/grinding
4. polishing/CMP 및 substrate inspection
5. epitaxy — CVD/MOCVD layer growth
6. device isolation/mesa etch
7. ohmic/Schottky/gate metallization
8. passivation/field plate
9. wafer probe
10. dicing/package
11. burn-in/reliability test

### 핵심 관리 포인트
- crystal defect micropipe/dislocation density
- wafer bow/warp/thickness variation
- epi thickness, doping, uniformity
- MOCVD/CVD chamber recipe와 run history
- metal contact resistance
- surface roughness/clean contamination
- high voltage leakage/breakdown trend
- wafer defect map과 device yield correlation

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


## B-7. 조립·패키징 / 封装

- `slug`: `assembly_packaging`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. wafer saw/dicing
2. die pick & place
3. die attach — epoxy/sinter/solder
4. cure 또는 reflow
5. wire bonding/flip-chip/TCB
6. underfill/flux clean
7. molding/encapsulation
8. post mold cure
9. marking/singulation
10. plating/trim/form
11. inspection/X-ray/SAM
12. final test/pack

### 핵심 관리 포인트
- wafer lot-die-package lot genealogy
- die attach void/tilt/bleed
- bond force, loop height, pull/shear
- flip-chip bump coplanarity/void
- mold compound lot와 cure profile
- warpage, delamination, moisture sensitivity
- X-ray/SAM defect code와 rework
- test bin과 assembly defect correlation

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


## B-8. 테스트 / 测试

- `slug`: `test`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. wafer sort/probe card setup
2. probe test — parametric/function/binning
3. wafer map 생성 및 inkless bin control
4. burn-in board loading
5. burn-in/HTOL/temperature stress
6. post burn-in test
7. final test — handler/tester/socket
8. mark/pack/label
9. QA sample/reliability confirm
10. shipment release

### 핵심 관리 포인트
- tester program revision과 limit lock
- probe card needle wear/contact resistance
- socket/handler jam 및 contact fail
- temperature calibration와 soak time
- burn-in condition/load board mapping
- bin definition 변경 이력
- retest rate와 false fail 분석
- lot release hold/QA disposition

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


# C. 전자 조립 제조 / 电子装配制造


## C-1. EMS 전자 수탁 제조 / EMS 电子代工

- `slug`: `ems`
- `routing`: `RT_JOBSHOP` — 잡샵형(Job-shop/High-mix): 제품·고객·옵션별 라우팅이 다르며, 공정 경로가 유연하다. WO별 routing version, 대체 설비, setup, 작업자 숙련도, WIP 위치와 납기 우선순위가 핵심이다.

### 공정 상세
1. 고객 수주/forecast 수신
2. BOM/Gerber/ECN/AVL 검토
3. DFM/DFT 및 NPI 준비
4. 자재 입고/IQC/MSD 관리
5. SMT setup — stencil, feeder, program, first article
6. SMT 생산 — print, SPI, placement, reflow, AOI/X-ray
7. DIP/수삽/웨이브 또는 selective solder
8. 기구 조립/라벨/serialization
9. ICT/FCT/aging test
10. 포장/출하 및 고객별 문서 제출

### 핵심 관리 포인트
- 고객/제품별 BOM revision과 ECN cut-in
- AVL 대체자재 승인과 lot trace
- feeder setup verification와 first article pass
- MSD floor life와 baking 이력
- SPI/AOI defect pareto와 rework loop
- test program version과 fixture calibration
- serial-level genealogy와 고객 RMA 연결

### MES/데이터 수집 포인트
`work_order_id`, `lot_or_serial_id`, `route_version`, `equipment_or_station_id`, `recipe_or_program_id`, `material_lot`, `inspection_result`, `hold_release_status`


## C-2. SMT 조립 / SMT 贴装

- `slug`: `smt_assembly`
- `routing`: `RT_LINE` — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.

### 공정 상세
1. PCB loader
2. solder paste printing
3. SPI — paste volume/height/offset 검사
4. chip mounter — high-speed placement
5. fine pitch/BGA placement
6. reflow soldering — thermal profile
7. AOI — polarity, missing, bridge, tombstone
8. X-ray — BGA/QFN void/short 검사
9. ICT/FCT
10. rework/repair
11. depanel/pack

### 핵심 관리 포인트
- stencil ID, paste lot, paste open time
- SPI volume/height/offset trend
- feeder part number와 reel lot verification
- placement offset, nozzle 상태, pickup error
- reflow zone profile와 peak/TAL
- AOI false call/miss call tuning
- BGA void rate/X-ray criteria
- rework 횟수 제한과 repair genealogy

### MES/데이터 수집 포인트
`line_id`, `station_id`, `takt_time`, `material_lot`, `equipment_status`, `inspection_result`, `defect_code`, `packing_label`


## C-3. PCB/PCBA / PCB/PCBA

- `slug`: `pcb_pcba`
- `routing`: `RT_LINE` — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.

### 공정 상세
1. CAM/DFM 검토
2. inner layer imaging/etching
3. lamination
4. drilling/laser via
5. desmear/electroless copper
6. pattern plating/outer layer etch
7. solder mask
8. surface finish — HASL/ENIG/OSP
9. electrical test/AOI
10. routing/V-cut
11. SMT/assembly 연계

### 핵심 관리 포인트
- layer stack-up와 impedance control
- drill registration, hole wall quality
- plating thickness와 via reliability
- etch compensation와 line/space CD
- solder mask alignment/coverage
- surface finish thickness/contamination
- electrical test fail map
- PCB lot와 PCBA serial genealogy

### MES/데이터 수집 포인트
`line_id`, `station_id`, `takt_time`, `material_lot`, `equipment_status`, `inspection_result`, `defect_code`, `packing_label`


## C-4. 산업용 전자 / 工业电子

- `slug`: `industrial_electronics`
- `routing`: `RT_JOBSHOP` — 잡샵형(Job-shop/High-mix): 제품·고객·옵션별 라우팅이 다르며, 공정 경로가 유연하다. WO별 routing version, 대체 설비, setup, 작업자 숙련도, WIP 위치와 납기 우선순위가 핵심이다.

### 공정 상세
1. 수주/사양 확정
2. BOM/도면/firmware revision 관리
3. PCBA 생산
4. conformal coating/potting 필요시 수행
5. 함체/기구 조립
6. firmware download/parameter setting
7. 기능시험
8. 환경시험 — burn-in, thermal cycling, vibration
9. 최종 검사/라벨/포장

### 핵심 관리 포인트
- firmware/hardware revision compatibility
- 고신뢰 부품 lot와 derating 확인
- coating 두께/coverage/cure 조건
- torque/grounding/insulation resistance
- 환경시험 조건과 failure log
- 제품 serial별 test result 저장
- field failure와 production genealogy 연결

### MES/데이터 수집 포인트
`work_order_id`, `lot_or_serial_id`, `route_version`, `equipment_or_station_id`, `recipe_or_program_id`, `material_lot`, `inspection_result`, `hold_release_status`


## C-5. 통신 장비 / 通信设备

- `slug`: `telecom_equipment`
- `routing`: `RT_JOBSHOP` — 잡샵형(Job-shop/High-mix): 제품·고객·옵션별 라우팅이 다르며, 공정 경로가 유연하다. WO별 routing version, 대체 설비, setup, 작업자 숙련도, WIP 위치와 납기 우선순위가 핵심이다.

### 공정 상세
1. BOM/RF/광 사양 검토
2. PCBA/SMT
3. RF shielding/thermal module 조립
4. optical transceiver/module assembly
5. firmware/software loading
6. RF calibration/alignment
7. optical power/BER/EVM test
8. network compatibility/aging
9. final QA/pack

### 핵심 관리 포인트
- RF calibration data와 test environment
- optical module serial matching
- thermal pad/heat sink torque 및 gap
- firmware version/config parameter
- EMI/EMC shield 상태
- BER/EVM/throughput trend
- burn-in failure와 component lot correlation

### MES/데이터 수집 포인트
`work_order_id`, `lot_or_serial_id`, `route_version`, `equipment_or_station_id`, `recipe_or_program_id`, `material_lot`, `inspection_result`, `hold_release_status`


## C-6. 소비자 전자 / 消费电子

- `slug`: `consumer_electronics`
- `routing`: `RT_LINE` — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.

### 공정 상세
1. demand/SKU plan 수신
2. material kitting
3. SMT/PCBA
4. case/미들프레임 조립
5. display/battery/camera/speaker 등 모듈 조립
6. firmware download
7. calibration — touch, camera, sensor
8. functional test/aging
9. cosmetic inspection
10. pack/label/palletizing

### 핵심 관리 포인트
- SKU/색상/국가별 label·firmware 매칭
- 모듈 serial scan 누락 방지
- screw torque, adhesive cure, gap/flush
- calibration yield와 station drift
- cosmetic defect code 표준화
- 라인 tact와 bottleneck station
- packing label/IMEI/serial consistency

### MES/데이터 수집 포인트
`line_id`, `station_id`, `takt_time`, `material_lot`, `equipment_status`, `inspection_result`, `defect_code`, `packing_label`


## C-7. 정밀 모듈 / 精密模组

- `slug`: `precision_modules`
- `routing`: `RT_JOBSHOP` — 잡샵형(Job-shop/High-mix): 제품·고객·옵션별 라우팅이 다르며, 공정 경로가 유연하다. WO별 routing version, 대체 설비, setup, 작업자 숙련도, WIP 위치와 납기 우선순위가 핵심이다.

### 공정 상세
1. 정밀 부품/렌즈/센서 입고
2. 부품 세정/particle 관리
3. sub-module assembly
4. active alignment
5. adhesive dispense/cure
6. electrical/optical calibration
7. environmental stress screening
8. final inspection
9. clean pack

### 핵심 관리 포인트
- active alignment offset/focus/tilt
- adhesive volume, 위치, cure profile
- particle/foreign material control
- sensor/lens/actuator serial matching
- calibration data와 test jig drift
- thermal/humidity stress 후 shift
- high-value module scrap disposition

### MES/데이터 수집 포인트
`work_order_id`, `lot_or_serial_id`, `route_version`, `equipment_or_station_id`, `recipe_or_program_id`, `material_lot`, `inspection_result`, `hold_release_status`


# D. 디스플레이·신에너지 제조 / 面板与新能源制造


## D-1. LCD / LCD

- `slug`: `lcd`
- `routing`: `RT_LINE` — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.

### 공정 상세
1. glass substrate cleaning
2. TFT array — deposition/photo/etch 반복
3. color filter fabrication
4. alignment layer coating/rubbing
5. cell assembly — sealant, spacer, LC filling
6. cell cutting/polarizer attach
7. driver IC bonding — COG/COF
8. backlight unit assembly
9. module assembly
10. optical/electrical inspection
11. aging/packing

### 핵심 관리 포인트
- glass particle/scratch/edge crack
- array CD/overlay/film thickness
- CF color uniformity/black matrix alignment
- LC filling bubble/contamination
- cell gap uniformity
- COG/COF bonding alignment/force/temp
- mura/line defect 검사 기준
- panel lot-cell-module genealogy

### MES/데이터 수집 포인트
`line_id`, `station_id`, `takt_time`, `material_lot`, `equipment_status`, `inspection_result`, `defect_code`, `packing_label`


## D-2. OLED / OLED

- `slug`: `oled`
- `routing`: `RT_REENTRANT` — 재진입형(Re-entrant): 동일 설비군/공정군을 여러 번 반복 통과한다. Lot 우선순위, Q-time, 레시피, 챔버/마스크/캐리어 이력, 병목 디스패칭이 CT와 수율을 좌우한다.

### 공정 상세
1. substrate cleaning
2. LTPS/LTPO TFT backplane
3. anode patterning
4. organic material evaporation with FMM
5. cathode deposition
6. encapsulation — TFE 또는 glass/frit
7. cell cutting
8. polarizer/touch integration
9. driver IC bonding
10. module assembly
11. optical aging/test

### 핵심 관리 포인트
- LTPS/LTPO backplane defect density
- FMM alignment와 shadow/contamination
- organic layer thickness/uniformity
- evaporation chamber vacuum/material lot
- encapsulation WVTR/leak risk
- mura, dark spot, pixel defect
- driver bonding alignment
- aging burn-in 조건과 luminance decay

### MES/데이터 수집 포인트
`lot_id`, `route_step`, `equipment_id`, `recipe_id`, `carrier_id`, `mask_or_reticle_id`, `Q_time`, `metrology_result`, `defect_map`


## D-3. 태양광 PV / 太阳能光伏

- `slug`: `solar_pv`
- `routing`: `RT_LINE` — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.

### 공정 상세
1. polysilicon/ingot growth
2. wafer slicing/texturing
3. diffusion/doping 또는 TOPCon/HJT 공정
4. edge isolation/passivation
5. screen printing/metallization
6. cell firing/anneal
7. cell test/binning
8. stringing/tabbing
9. layup — glass/EVA/cell/backsheet
10. lamination
11. framing/junction box
12. EL/flash/insulation test
13. pack

### 핵심 관리 포인트
- wafer thickness, micro-crack, saw mark
- texturing uniformity와 reflectance
- dopant/passivation layer uniformity
- metallization line width/contact resistance
- cell bin matching and string current balance
- lamination vacuum/temp/time/bubble
- EL crack/black spot classification
- flash test calibration and power binning

### MES/데이터 수집 포인트
`line_id`, `station_id`, `takt_time`, `material_lot`, `equipment_status`, `inspection_result`, `defect_code`, `packing_label`


## D-4. 2차전지 / 二次电池

- `slug`: `battery`
- `routing`: `RT_LINE` — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.

### 공정 상세
1. active material/binder/solvent mixing
2. electrode coating and drying
3. calendering/pressing
4. slitting/notching
5. vacuum drying
6. cell assembly — winding/stacking
7. tab welding/case insertion
8. electrolyte filling/wetting
9. formation charge/discharge
10. aging/OCV/IR grading
11. module/pack assembly if applicable
12. final safety test

### 핵심 관리 포인트
- slurry viscosity/solid content/dispersion
- coating loading, thickness, moisture
- drying solvent residual and temperature profile
- roll gap/density/porosity
- slitting burr and particle contamination
- dry-room dew point and moisture exposure time
- welding quality and internal short risk
- electrolyte filling amount/wetting time
- formation recipe, OCV/IR trend, gas/swelling

### MES/데이터 수집 포인트
`line_id`, `station_id`, `takt_time`, `material_lot`, `equipment_status`, `inspection_result`, `defect_code`, `packing_label`


## D-5. ESS 에너지 저장 시스템 / ESS 储能系统

- `slug`: `energy_storage`
- `routing`: `RT_PROJECT` — 프로젝트형(Project/ETO): 고객/프로젝트/사이트 단위로 WBS·자재·도면·공정이 묶이며, 동일 제품 반복보다 단계 게이트와 변경관리, 장납기 자재, 현장 진도가 핵심이다.

### 공정 상세
1. cell incoming inspection
2. cell sorting/matching
3. module assembly — compression, busbar, sensing harness
4. BMS installation and parameter setting
5. rack/cabinet assembly
6. PCS/EMS integration
7. thermal/fire suppression system installation
8. factory integration test
9. site installation
10. commissioning/grid connection
11. performance acceptance

### 핵심 관리 포인트
- cell lot/grade matching and imbalance
- module compression force/insulation resistance
- busbar torque/weld quality
- BMS firmware/config version
- thermal runaway detection and fire interlock
- PCS-EMS communication mapping
- site wiring/grounding/insulation test
- commissioning alarm and acceptance records

### MES/데이터 수집 포인트
`project_id`, `WBS/activity_id`, `drawing_revision`, `material_package`, `vendor_document_status`, `inspection_record`, `punch_status`, `progress_qty`


# E. 프로세스·화학 제조 / 流程化工制造


## E-1. 석유화학 / 石油化工

- `slug`: `petrochemical`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. feedstock receiving/storage
2. pretreatment/desalting/drying
3. distillation or separation
4. cracking/reforming/reaction
5. quench/heat recovery
6. compression/separation/purification
7. polymerization or derivative synthesis
8. stabilization/additive blending
9. tank farm/packaging
10. QC release/shipment

### 핵심 관리 포인트
- feedstock composition and impurity
- reactor temperature/pressure/catalyst activity
- distillation cut point/reflux ratio
- safety interlock/relief/flare status
- online analyzer calibration
- batch/tank genealogy and blend ratio
- off-spec material hold/rework
- emission/wastewater compliance data

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


## E-2. 정밀화학 / 精细化工

- `slug`: `fine_chemical`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. raw material weighing/charging
2. reaction synthesis
3. temperature/pressure/pH control
4. aging/holding
5. phase separation/extraction
6. filtration/centrifuge
7. crystallization
8. drying
9. milling/sieving
10. packaging/QC release

### 핵심 관리 포인트
- weighing accuracy and material lot
- reaction endpoint and heat release control
- pH/moisture/impurity profile
- solvent recovery/reuse trace
- filter integrity and cake moisture
- crystal size distribution
- drying LOD/residual solvent
- cleaning validation/cross contamination

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


## E-3. 고분자 소재 / 高分子材料

- `slug`: `polymer_materials`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. monomer/feedstock preparation
2. polymerization reaction
3. devolatilization/degassing
4. additive compounding
5. extrusion/pelletizing
6. cooling/classification
7. silo blending
8. QC — MFI, viscosity, mechanical properties
9. bagging/bulk shipment

### 핵심 관리 포인트
- monomer purity and inhibitor level
- reactor temp/pressure/catalyst feed
- molecular weight/MFI trend
- additive dosing accuracy
- extruder torque/temp profile
- pellet size/fines/black speck
- silo lot blending genealogy
- off-grade segregation

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


## E-4. 특수가스 / 特种气体

- `slug`: `specialty_gas`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. source material receiving
2. purification — adsorption/distillation/getter
3. gas blending or synthesis
4. cylinder/canister cleaning and evacuation
5. filling
6. leak test
7. analytical QC — purity/trace impurity
8. labeling and certification
9. shipment/return cylinder management

### 핵심 관리 포인트
- cylinder identity and cleaning history
- moisture/oxygen/particle/metal impurity
- purifier breakthrough monitoring
- blend concentration accuracy
- filling pressure/weight/temp compensation
- leak rate and valve integrity
- COA release and shelf-life
- return cylinder contamination risk

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


## E-5. 무기 소재 / 无机材料

- `slug`: `inorganic_materials`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. ore/precursor receiving
2. crushing/grinding/classification
3. calcination/roasting
4. leaching/dissolution
5. precipitation
6. filtration/washing
7. drying/calcination
8. milling/sieving
9. surface treatment/blending
10. packaging/QC

### 핵심 관리 포인트
- raw material composition variability
- particle size distribution
- calcination temperature/time profile
- pH/concentration during precipitation
- washing conductivity/impurity
- moisture/LOI
- metal contamination
- lot blending and customer spec matching

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


# F. 소비재·식품 제조 / 消费品与食品制造


## F-1. 식품 가공 / 食品加工

- `slug`: `food_processing`
- `routing`: `RT_LINE` — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.

### 공정 상세
1. raw material receiving
2. storage/cold chain
3. washing/sorting/trimming
4. mixing/cooking/processing
5. metal detection or sieving
6. filling/portioning
7. heat treatment or chilling/freezing
8. packaging/sealing
9. labeling/coding
10. finished goods QA/release

### 핵심 관리 포인트
- supplier lot and allergen status
- cold chain temperature/time
- foreign material removal and metal detector challenge test
- CCP temperature/time/pH/water activity
- cleaning/sanitation verification
- pack seal integrity
- label/allergen/country code accuracy
- retain sample and traceability

### MES/데이터 수집 포인트
`line_id`, `station_id`, `takt_time`, `material_lot`, `equipment_status`, `inspection_result`, `defect_code`, `packing_label`


## F-2. 음료·주류 / 饮料·酒类

- `slug`: `beverage`
- `routing`: `RT_LINE` — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.

### 공정 상세
1. water treatment
2. syrup/ingredient preparation
3. blending/mixing
4. filtration/deaeration
5. pasteurization or UHT/aseptic processing
6. container rinsing/sterilization
7. filling/capping/seaming
8. coding/labeling
9. case packing/palletizing
10. QC release

### 핵심 관리 포인트
- Brix/pH/acidity/CO2 concentration
- water quality and filter status
- pasteurization PU or UHT temp/time
- filler hygiene and CIP/SIP status
- fill level/cap torque/seam integrity
- foreign material and package defect
- label/date code match
- microbiology hold/release

### MES/데이터 수집 포인트
`line_id`, `station_id`, `takt_time`, `material_lot`, `equipment_status`, `inspection_result`, `defect_code`, `packing_label`


## F-3. 퍼스널 케어 / 个人护理

- `slug`: `personal_care`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. raw material receiving/QC
2. weighing/dispensing
3. water/oil phase preparation
4. emulsification/mixing
5. homogenization
6. cooling/deaeration
7. bulk hold/QC
8. filling/capping
9. labeling/packing
10. retain sample/release

### 핵심 관리 포인트
- formula/version and weighing accuracy
- mixing temp/speed/time
- viscosity/pH/specific gravity
- microbial control and preservative efficacy
- bulk hold time and tank ID
- filling weight/torque/leak
- packaging component lot matching
- cleaning/changeover allergen/fragrance carryover

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


## F-4. 홈 케어 / 家庭清洁

- `slug`: `home_care`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. surfactant/chemical receiving
2. weighing/charging
3. mixing/reaction or neutralization
4. viscosity/pH adjustment
5. fragrance/color/additive dosing
6. filtration/defoaming
7. bulk storage
8. bottle filling/capping
9. labeling/case packing
10. QC release

### 핵심 관리 포인트
- chemical concentration and compatibility
- pH/viscosity/density
- exotherm/neutralization control
- fragrance/color dosing accuracy
- foaming and filter clogging
- fill weight/cap torque/leak
- corrosive/hazardous material handling
- CIP/changeover residue

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


## F-5. 일반 소비재 / 一般消费品

- `slug`: `consumer_goods`
- `routing`: `RT_LINE` — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.

### 공정 상세
1. demand/SKU planning
2. material kitting
3. component molding/forming
4. sub-assembly
5. main assembly
6. functional/cosmetic inspection
7. packaging/labeling
8. carton/palletizing
9. shipment

### 핵심 관리 포인트
- SKU/BOM version and package artwork
- mold/fixture/tooling condition
- assembly torque/adhesive/cure
- visual defect standardization
- line balance and station bottleneck
- serial/lot trace if regulated
- packing count and label accuracy

### MES/데이터 수집 포인트
`line_id`, `station_id`, `takt_time`, `material_lot`, `equipment_status`, `inspection_result`, `defect_code`, `packing_label`


# G. 의약품·바이오 제조 / 制药与生物制造


## G-1. 원료의약품(API) / 原料药(API)

- `slug`: `api`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. raw material quarantine/release
2. dispensing/charging
3. reaction synthesis
4. in-process control
5. quench/work-up/extraction
6. crystallization
7. filtration/centrifugation
8. drying
9. milling/sieving/blending
10. packaging
11. QC/QA batch release

### 핵심 관리 포인트
- GMP status and material release
- batch record completeness and e-signature
- critical process parameters temp/pH/time
- impurity profile and endpoint test
- cleaning validation/cross contamination
- residual solvent/LOD
- deviation/OOS/CAPA
- QA release and COA

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


## G-2. 완제의약품 / 制剂

- `slug`: `drug_product`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. API/excipient dispensing
2. granulation or direct blending
3. drying/milling
4. final blending/lubrication
5. compression or capsule filling
6. coating if applicable
7. in-process weight/hardness/disintegration
8. primary packaging blister/bottle
9. secondary packaging/serialization
10. QC/QA release

### 핵심 관리 포인트
- recipe/master batch record version
- blend uniformity and segregation risk
- moisture after drying
- tablet weight/hardness/thickness
- coating weight gain/defect
- line clearance and mix-up prevention
- serialization aggregation
- deviation/OOS and batch release

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


## G-3. 바이오의약품 / 生物药

- `slug`: `biologics`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. cell bank thaw/seed train
2. upstream cell culture/fermentation
3. harvest/clarification
4. capture chromatography
5. viral inactivation/removal
6. polishing chromatography/UFDF
7. formulation
8. sterile filtration
9. fill-finish
10. QC/QA release

### 핵심 관리 포인트
- cell line/bank identity and passage number
- bioreactor pH/DO/temp/feed profile
- bioburden/endotoxin control
- chromatography column lot/cycle and yield
- viral clearance step parameters
- hold time and cold chain
- sterile filtration integrity
- aseptic fill environmental monitoring

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


## G-4. 백신 / 疫苗

- `slug`: `vaccine`
- `routing`: `RT_BATCH` — 배치형(Batch): 반응·열처리·혼합·숙성·검사 등이 배치/로트 단위로 진행된다. 배치 genealogy, 레시피, 투입량, hold/release, 샘플링 검사와 편차관리가 핵심이다.

### 공정 상세
1. seed/strain management
2. cell culture or egg/substrate preparation
3. virus/bacteria propagation
4. harvest
5. inactivation or attenuation step
6. purification/concentration
7. adjuvant/formulation
8. sterile filtration/fill finish
9. stability/QC
10. lot release

### 핵심 관리 포인트
- seed lot identity and biosafety level
- culture growth parameters
- inactivation completeness
- antigen content/potency
- adjuvant mixing uniformity
- sterility/bioburden/endotoxin
- cold chain and hold time
- regulatory lot release documentation

### MES/데이터 수집 포인트
`batch_id`, `recipe_version`, `material_lot`, `charge_qty`, `process_parameter`, `sample_result`, `deviation_id`, `release_status`


## G-5. CDMO / CDMO

- `slug`: `cdmo`
- `routing`: `RT_JOBSHOP` — 잡샵형(Job-shop/High-mix): 제품·고객·옵션별 라우팅이 다르며, 공정 경로가 유연하다. WO별 routing version, 대체 설비, setup, 작업자 숙련도, WIP 위치와 납기 우선순위가 핵심이다.

### 공정 상세
1. tech transfer from client
2. gap assessment and process fit
3. scale-up/engineering batch
4. method transfer/validation
5. GMP campaign planning
6. material procurement/release
7. GMP batch manufacturing
8. QC testing/QA review
9. client release package
10. changeover/cleaning for next client

### 핵심 관리 포인트
- client spec/version and tech transfer package completeness
- campaign segregation and confidentiality
- scale-up parameter comparability
- analytical method transfer status
- GMP batch record and deviation handling
- cross-contamination/cleaning validation
- client QA disposition and release timeline
- capacity slot and changeover loss

### MES/데이터 수집 포인트
`work_order_id`, `lot_or_serial_id`, `route_version`, `equipment_or_station_id`, `recipe_or_program_id`, `material_lot`, `inspection_result`, `hold_release_status`


# H. 자동차·장비 제조 / 汽车与装备制造


## H-1. 완성차 OEM / 整车 OEM

- `slug`: `vehicle_oem`
- `routing`: `RT_LINE` — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.

### 공정 상세
1. press/stamping
2. body shop welding
3. body inspection
4. paint pretreatment/e-coat
5. sealer/top coat/oven
6. powertrain/chassis subassembly
7. trim/chassis/final assembly
8. fluid filling
9. wheel alignment/ADAS calibration
10. end-of-line test
11. water leak/road test
12. shipping

### 핵심 관리 포인트
- press die condition and panel dimensional quality
- body weld spot count/strength and gap/flush
- paint thickness, oven temp, dust defect
- VIN-body-engine-battery genealogy
- andon stop and takt adherence
- torque traceability for safety critical joints
- ADAS/calibration data
- EOL defect and repair loop

### MES/데이터 수집 포인트
`line_id`, `station_id`, `takt_time`, `material_lot`, `equipment_status`, `inspection_result`, `defect_code`, `packing_label`


## H-2. 파워트레인 / 动力总成

- `slug`: `powertrain`
- `routing`: `RT_LINE` — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.

### 공정 상세
1. casting/forging receiving
2. machining of block/head/gear/shaft
3. washing/deburring
4. heat treatment if applicable
5. subassembly
6. main assembly
7. torque/press-fit control
8. cold/hot test
9. leak/noise/vibration test
10. final inspection

### 핵심 관리 포인트
- machining dimension and tool wear
- washing cleanliness particle count
- heat treatment hardness/distortion
- bearing/gear backlash/clearance
- torque-angle traceability
- leak test pressure decay
- NVH test trend
- serial genealogy to vehicle VIN

### MES/데이터 수집 포인트
`line_id`, `station_id`, `takt_time`, `material_lot`, `equipment_status`, `inspection_result`, `defect_code`, `packing_label`


## H-3. EV 구동 시스템 / EV 驱动系统

- `slug`: `ev_drive_system`
- `routing`: `RT_LINE` — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.

### 공정 상세
1. stator lamination/stacking
2. winding/insertion
3. impregnation/curing
4. rotor assembly/magnet insertion
5. motor assembly
6. inverter PCBA/power module assembly
7. e-axle gearbox assembly
8. cooling/sealing
9. end-of-line dynamometer test
10. NVH/electrical safety test

### 핵심 관리 포인트
- winding tension/slot fill and insulation damage
- impregnation resin amount/cure profile
- magnet polarity/balance
- inverter power module attach/void
- cooling channel leak
- high-voltage insulation/hipot
- dyno torque/speed/efficiency map
- software/calibration version

### MES/데이터 수집 포인트
`line_id`, `station_id`, `takt_time`, `material_lot`, `equipment_status`, `inspection_result`, `defect_code`, `packing_label`


## H-4. 섀시 부품 / 底盘部件

- `slug`: `chassis_components`
- `routing`: `RT_LINE` — 라인형(Linear/Flow): 고정된 순서의 연속 또는 반복 라인 흐름이다. takt, 라인 밸런스, 병목, 설비 정지, 투입-산출 동기화와 품질 게이트가 핵심이다.

### 공정 상세
1. raw material/forging/casting receiving
2. machining/forming
3. heat treatment
4. surface treatment/coating
5. bushing/bearing/ball joint assembly
6. welding if applicable
7. dimensional inspection
8. fatigue/load test sampling
9. packing

### 핵심 관리 포인트
- material grade/heat lot trace
- critical dimension and GD&T
- hardness/case depth
- coating thickness/corrosion protection
- press-fit force-displacement curve
- weld quality if applicable
- safety part traceability
- sample destructive test results

### MES/데이터 수집 포인트
`line_id`, `station_id`, `takt_time`, `material_lot`, `equipment_status`, `inspection_result`, `defect_code`, `packing_label`


## H-5. 자동차 전자·전장 / 汽车电子

- `slug`: `automotive_electronics`
- `routing`: `RT_JOBSHOP` — 잡샵형(Job-shop/High-mix): 제품·고객·옵션별 라우팅이 다르며, 공정 경로가 유연하다. WO별 routing version, 대체 설비, setup, 작업자 숙련도, WIP 위치와 납기 우선순위가 핵심이다.

### 공정 상세
1. BOM/ASIL/PPAP requirement review
2. SMT/PCBA
3. selective solder/conformal coating
4. housing/connector assembly
5. firmware flashing
6. ICT/FCT
7. environmental stress screening
8. EOL communication test
9. trace label/packing

### 핵심 관리 포인트
- component PPAP/lot trace
- MSD/ESD control
- coating coverage and cure
- firmware/calibration version
- CAN/LIN/Ethernet test logs
- thermal/vibration/burn-in failure
- functional safety critical parameter lock
- IATF documentation and change control

### MES/데이터 수집 포인트
`work_order_id`, `lot_or_serial_id`, `route_version`, `equipment_or_station_id`, `recipe_or_program_id`, `material_lot`, `inspection_result`, `hold_release_status`


## H-6. Tier1/Tier2 부품 공급사 / Tier1/Tier2 零部件

- `slug`: `tier1_tier2_suppliers`
- `routing`: `RT_JOBSHOP` — 잡샵형(Job-shop/High-mix): 제품·고객·옵션별 라우팅이 다르며, 공정 경로가 유연하다. WO별 routing version, 대체 설비, setup, 작업자 숙련도, WIP 위치와 납기 우선순위가 핵심이다.

### 공정 상세
1. customer order/forecast and EDI
2. APQP/PPAP/NPI
3. material receiving
4. component manufacturing — molding/stamping/machining/assembly
5. in-process inspection
6. subassembly/final assembly
7. EOL test
8. labeling/packing
9. JIT/JIS shipment

### 핵심 관리 포인트
- customer revision/engineering change cut-in
- PPAP status and control plan
- tooling cavity/mold/press condition
- lot trace and FIFO
- SPC for critical characteristics
- EOL tester calibration and result upload
- pack label/ASN accuracy
- customer complaint/RMA traceability

### MES/데이터 수집 포인트
`work_order_id`, `lot_or_serial_id`, `route_version`, `equipment_or_station_id`, `recipe_or_program_id`, `material_lot`, `inspection_result`, `hold_release_status`


# 2. 참고 공개 자료

- ASML, Semiconductor manufacturing steps: https://www.asml.com/news/stories/2021/semiconductor-manufacturing-process-steps
- Renesas, Semiconductor device manufacturing stages: https://www.renesas.com/en/blogs/semiconductor-device-manufacturing-process-challenges-and-opportunities
- NextPCB, SMT assembly process: https://www.nextpcb.com/blog/smt-assembly-process
- Atlas Copco, Lithium battery production process: https://www.atlascopco.com/en-us/compressors/wiki/compressed-air-articles/lithium-battery-production-process
- DOE, Solar photovoltaic manufacturing basics: https://www.energy.gov/cmei/systems/solar-photovoltaic-manufacturing-basics
- Toyota, Vehicle production process: https://global.toyota/en/company/plant-tours/stamping/index.html
- FDA, HACCP principles: https://www.fda.gov/food/hazard-analysis-critical-control-point-haccp/haccp-principles-application-guidelines
- FDA, Q7A GMP for APIs: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q7a-good-manufacturing-practice-guidance-active-pharmaceutical-ingredients
- Samsung Display, OLED evaporation / FMM: https://global.samsungdisplay.com/29396/
- EPA, Petroleum refining processes: https://gaftp.epa.gov/ap42/ch05/s01/final/c05s01_jan1995.pdf
- EIA, Refining crude oil: https://www.eia.gov/energyexplained/oil-and-petroleum-products/refining-crude-oil-the-refining-process.php
- Fukuzo, Shipbuilding process: https://www.fukuzo.co.jp/en/shipbuilding/process