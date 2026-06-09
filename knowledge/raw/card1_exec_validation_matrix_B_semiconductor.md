# Card1 Exec Validation Matrix (B Semiconductor)

목적: 반도체(B) 산업 기준으로 S1~S4 입력 케이스의 Card1(생산 실행) 정합성을 `normalize 결과` 기준으로 검증한다.

검증 기준:
- 로직/데이터 수정 없이 `/api/diagnose` (`debug: true`) 실응답 사용
- 엔진 후보: `get_execution_candidates_for_card1_with_meta(...)._meta_debug`
- 최종 카드 추적: `decision.ch2.domain_cards.exec._debug_trace`

## 공통 요청 조건

- `industry`: `B`
- `automation_level`: `L3`
- `keywords`: `["EAP","FDC","APC","SPC","BI"]`
- `debug`: `true`

## S1~S4 검증 매트릭스

| 케이스 | 요청 scale payload | normalize 결과(scale_normalized) | 엔진 후보(selected_candidates) | compose 추적(_debug_trace) | 기대 후보 방향 | 판정 |
|---|---|---|---|---|---|---|
| S1 | `S/S/S` | `S1` | `MES, DISPATCH, ROUTE_EXEC` | `role=1, cap=3, iface=3` | S1: MES/현장 실행 중심 | OK |
| S2 | `M/M/M` | `S2` | `MES, DISPATCH, TRACE_EXEC, ROUTE_EXEC` | `role=2, cap=4, iface=4` | S2: MES+dispatch/trace 확장 | OK |
| S3 | `L/L/L` | `S3` | `EXEC_MGMT, MOM, MES, TRACE_EXEC, ROUTE_EXEC` | `role=3, cap=5, iface=5` | S3: `EXEC_MGMT` 등장 필요 | OK |
| S4 | `XL/XL/XL` | `S3` | `EXEC_MGMT, MOM, MES, TRACE_EXEC, ROUTE_EXEC` | `role=3, cap=5, iface=5` | S4: `GLOBAL_MES` 또는 `EXEC_MGMT+GLOBAL_MES` | NG (normalize가 S4로 안 올라감) |

## 케이스별 스냅샷

### S1

- payload: `{"scale":{"equipment":"S","employees":"S","revenue":"S"}}`
- `_meta_debug.input_context`: `{"industry":"B","scale_raw":"S1","scale_normalized":"S1"}`
- `_meta_debug.selected_candidates`: `["MES","DISPATCH","ROUTE_EXEC"]`
- `exec._debug_trace`: `{"selected_candidates":["MES","DISPATCH","ROUTE_EXEC"],"role_sections_count":1,"cap_sections_count":3,"iface_sections_count":3}`
- 카드 요약
  - role: `MES（制造执行系统）`
  - cap: `工单/工序执行控制与报工 / WIP在制可视化与滞留控制`

### S2

- payload: `{"scale":{"equipment":"M","employees":"M","revenue":"M"}}`
- `_meta_debug.input_context`: `{"industry":"B","scale_raw":"S2","scale_normalized":"S2"}`
- `_meta_debug.selected_candidates`: `["MES","DISPATCH","TRACE_EXEC","ROUTE_EXEC"]`
- `exec._debug_trace`: `{"selected_candidates":["MES","DISPATCH","TRACE_EXEC","ROUTE_EXEC"],"role_sections_count":2,"cap_sections_count":4,"iface_sections_count":4}`
- 카드 요약
  - role: `MES（制造执行系统）`
  - cap: `工单/工序执行控制与报工 / WIP在制可视化与滞留控制`

### S3

- payload: `{"scale":{"equipment":"L","employees":"L","revenue":"L"}}`
- `_meta_debug.input_context`: `{"industry":"B","scale_raw":"S3","scale_normalized":"S3"}`
- `_meta_debug.selected_candidates`: `["EXEC_MGMT","MOM","MES","TRACE_EXEC","ROUTE_EXEC"]`
- `exec._debug_trace`: `{"selected_candidates":["EXEC_MGMT","MOM","MES","TRACE_EXEC","ROUTE_EXEC"],"role_sections_count":3,"cap_sections_count":5,"iface_sections_count":5}`
- 카드 요약
  - role: `MES（制造执行系统）`
  - cap: `多工厂执行治理 / 共通运营政策管控`

### S4

- payload: `{"scale":{"equipment":"XL","employees":"XL","revenue":"XL"}}`
- `_meta_debug.input_context`: `{"industry":"B","scale_raw":"S3","scale_normalized":"S3"}`
- `_meta_debug.selected_candidates`: `["EXEC_MGMT","MOM","MES","TRACE_EXEC","ROUTE_EXEC"]`
- `exec._debug_trace`: `{"selected_candidates":["EXEC_MGMT","MOM","MES","TRACE_EXEC","ROUTE_EXEC"],"role_sections_count":3,"cap_sections_count":5,"iface_sections_count":5}`
- 카드 요약
  - role: `MES（制造执行系统）`
  - cap: `多工厂执行治理 / 共通运营政策管控`

## 해석 및 주의점

- 검증 기준은 **입력 payload 텍스트가 아니라 normalize 결과**다.
- 본 검증에서 `XL/XL/XL`은 내부적으로 `S4`가 아닌 `S3`로 해석되어 S4 기대값과 불일치했다.
- 즉 Card1 결과 이상 여부 판단 전에 `_meta_debug.input_context.scale_normalized`를 먼저 확인해야 한다.

## 다음 액션 제안 (검증 관점)

- S4 검증을 위해 현재 normalize가 인식하는 `S4` 입력 패턴을 먼저 확정
- 이후 동일 매트릭스를 그대로 재실행하여 S4 케이스 재판정
