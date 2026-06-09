# Card1 Exec Industry Snapshots (Step B)

## 1) 목적

Step B는 구조 분석이 아닌 실제 `/api/diagnose` 출력 스냅샷 수집 단계다. 이번 문서는 A~H 8대 산업의 Card1(생산 실행) 결과를 동일 조건으로 기록한다.

## 2) 공통 호출 조건

- endpoint: `POST /api/diagnose`
- `debug: true`
- scale: `M/M/M` (equipment/employees/revenue)
- 공통 payload:

```json
{
  "scale": {
    "equipment": "M",
    "employees": "M",
    "revenue": "M"
  },
  "automation_level": "L3",
  "keywords": [
    "EAP",
    "FDC",
    "APC",
    "SPC",
    "BI"
  ],
  "debug": true
}
```

## 3) 8대 산업 스냅샷 표

| 산업 | normalize 결과 | 후보 시스템 | role 요약 | cap 요약 | iface 요약 | 메모 |
|---|---|---|---|---|---|---|
| A | S2 | MES, SFC, LINE_EXEC, DISPATCH | 基础执行系统: MES（制造执行系统） / SFC | MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制 | MES（制造执行系统）: import:工艺路线 / 工单 / ERP / export:产出/报工 / WIP状态 / 追溯链路 | generic MES 경향 |
| B | S2 | MES, DISPATCH, TRACE_EXEC, ROUTE_EXEC | 基础执行系统: MES（制造执行系统） | MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制 | MES（制造执行系统）: import:Recipe / 批次数据 / Genealogy / export:产出/报工 / WIP状态 / 追溯链路 | 반도체 표현 일부 존재 |
| C | S2 | MES, SFC, LINE_EXEC, TRACE_EXEC | 基础执行系统: MES（制造执行系统） / SFC | MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制 | MES（制造执行系统）: import:Feeder / Test station / SMT/AOI/SPI / export:产出/报工 / WIP状态 / 追溯链路 | 라인 중심 표현 보임 |
| D | S2 | MES, TRACE_EXEC, ROUTE_EXEC, DISPATCH | 基础执行系统: MES（制造执行系统） | MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制 | MES（制造执行系统）: import:EAP / 量测数据 / 设备状态 / export:产出/报工 / WIP状态 / 追溯链路 | generic MES 경향 |
| E | S2 | MES, SFC, TRACE_EXEC, LINE_EXEC | 基础执行系统: MES（制造执行系统） / SFC | MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制 | MES（制造执行系统）: import:Recipe / Recipe management / Batch record / export:产出/报工 / WIP状态 / 追溯链路 | generic MES 경향 |
| F | S2 | MES, BATCH_EXEC, ROUTE_EXEC | 基础执行系统: MES（制造执行系统） | MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制 | MES（制造执行系统）: import:包装线 / 报工 / ERP订单 / export:产出/报工 / WIP状态 / 追溯链路 | 배치/규제 관련 후보 보임 |
| G | S2 | MES, BATCH_EXEC, EBR, TRACE_EXEC | 基础执行系统: MES（制造执行系统） | MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制 | MES（制造执行系统）: import:QMS / LIMS / EBR / export:产出/报工 / WIP状态 / 追溯链路 | 배치/규제 관련 후보 보임 |
| H | S2 | MES, SFC, LINE_EXEC, WO_EXEC | 基础执行系统: MES（制造执行系统） / SFC | MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制 | MES（制造执行系统）: import:序列号 / Test station / SMT/AOI/SPI / export:产出/报工 / WIP状态 / 追溯链路 | generic MES 경향 |

## 4) 산업별 상세 스냅샷

### A

- payload: `{"industry": "A", "scale": {"equipment": "M", "employees": "M", "revenue": "M"}, "automation_level": "L3", "keywords": ["EAP", "FDC", "APC", "SPC", "BI"], "debug": true}`
- `_meta_debug.input_context`: `{"industry": "A", "scale_raw": "S2", "scale_normalized": "S2"}`
- `_meta_debug.selected_candidates`: `["MES", "SFC", "LINE_EXEC", "DISPATCH"]`
- `_debug_trace`: `{"selected_candidates": ["MES", "SFC", "LINE_EXEC", "DISPATCH"], "role_sections_count": 2, "cap_sections_count": 4, "iface_sections_count": 4}`
- role 요약:
  - 基础执行系统: MES（制造执行系统） / SFC
  - 多线扩展系统: LINE_EXEC / DISPATCH
- cap 요약:
  - MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制
  - SFC: 工位执行与报工 / 产线节奏控制
  - LINE_EXEC: 产线节奏控制 / 工位同步
- iface 요약:
  - MES（制造执行系统）: import:工艺路线 / 工单 / ERP / export:产出/报工 / WIP状态 / 追溯链路
  - SFC: import:MES工单 / 设备/条码 / 作业指导 / export:报工数据 / WIP状态 / 异常事件
  - LINE_EXEC: import:MES/排程 / 设备状态 / WMS / export:产线状态 / 产出/报工 / 齐套预警

### B

- payload: `{"industry": "B", "scale": {"equipment": "M", "employees": "M", "revenue": "M"}, "automation_level": "L3", "keywords": ["EAP", "FDC", "APC", "SPC", "BI"], "debug": true}`
- `_meta_debug.input_context`: `{"industry": "B", "scale_raw": "S2", "scale_normalized": "S2"}`
- `_meta_debug.selected_candidates`: `["MES", "DISPATCH", "TRACE_EXEC", "ROUTE_EXEC"]`
- `_debug_trace`: `{"selected_candidates": ["MES", "DISPATCH", "TRACE_EXEC", "ROUTE_EXEC"], "role_sections_count": 2, "cap_sections_count": 4, "iface_sections_count": 4}`
- role 요약:
  - 基础执行系统: MES（制造执行系统）
  - 多线扩展系统: DISPATCH / TRACE_EXEC
- cap 요약:
  - MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制
  - DISPATCH: 派工规则与优先级 / 资源分配与负载均衡
  - TRACE_EXEC: 批次/序列号追溯 / 关键件绑定
- iface 요약:
  - MES（制造执行系统）: import:Recipe / 批次数据 / Genealogy / export:产出/报工 / WIP状态 / 追溯链路
  - DISPATCH: import:MES工单 / 设备/产线状态 / APS排程 / export:派工指令 / 执行状态 / 负载反馈
  - TRACE_EXEC: import:MES执行数据 / 检验/测试数据 / 物料批次 / export:追溯链路 / 追溯报告 / 合规证据

### C

- payload: `{"industry": "C", "scale": {"equipment": "M", "employees": "M", "revenue": "M"}, "automation_level": "L3", "keywords": ["EAP", "FDC", "APC", "SPC", "BI"], "debug": true}`
- `_meta_debug.input_context`: `{"industry": "C", "scale_raw": "S2", "scale_normalized": "S2"}`
- `_meta_debug.selected_candidates`: `["MES", "SFC", "LINE_EXEC", "TRACE_EXEC"]`
- `_debug_trace`: `{"selected_candidates": ["MES", "SFC", "LINE_EXEC", "TRACE_EXEC"], "role_sections_count": 2, "cap_sections_count": 4, "iface_sections_count": 4}`
- role 요약:
  - 基础执行系统: MES（制造执行系统） / SFC
  - 多线扩展系统: LINE_EXEC / TRACE_EXEC
- cap 요약:
  - MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制
  - SFC: 工位执行与报工 / 产线节奏控制
  - LINE_EXEC: 产线节奏控制 / 工位同步
- iface 요약:
  - MES（制造执行系统）: import:Feeder / Test station / SMT/AOI/SPI / export:产出/报工 / WIP状态 / 追溯链路
  - SFC: import:MES工单 / 设备/条码 / 作业指导 / export:报工数据 / WIP状态 / 异常事件
  - LINE_EXEC: import:MES/排程 / 设备状态 / WMS / export:产线状态 / 产出/报工 / 齐套预警

### D

- payload: `{"industry": "D", "scale": {"equipment": "M", "employees": "M", "revenue": "M"}, "automation_level": "L3", "keywords": ["EAP", "FDC", "APC", "SPC", "BI"], "debug": true}`
- `_meta_debug.input_context`: `{"industry": "D", "scale_raw": "S2", "scale_normalized": "S2"}`
- `_meta_debug.selected_candidates`: `["MES", "TRACE_EXEC", "ROUTE_EXEC", "DISPATCH"]`
- `_debug_trace`: `{"selected_candidates": ["MES", "TRACE_EXEC", "ROUTE_EXEC", "DISPATCH"], "role_sections_count": 2, "cap_sections_count": 4, "iface_sections_count": 4}`
- role 요약:
  - 基础执行系统: MES（制造执行系统）
  - 多线扩展系统: TRACE_EXEC / ROUTE_EXEC
- cap 요약:
  - MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制
  - TRACE_EXEC: 批次/序列号追溯 / 关键件绑定
  - ROUTE_EXEC: 工艺路线执行 / 配方/参数下发
- iface 요약:
  - MES（制造执行系统）: import:EAP / 量测数据 / 设备状态 / export:产出/报工 / WIP状态 / 追溯链路
  - TRACE_EXEC: import:MES执行数据 / 检验/测试数据 / 物料批次 / export:追溯链路 / 追溯报告 / 合规证据
  - ROUTE_EXEC: import:PLM/工艺主数据 / MES工单 / 设备/配方库 / export:工序执行记录 / 参数履历 / 合规结果

### E

- payload: `{"industry": "E", "scale": {"equipment": "M", "employees": "M", "revenue": "M"}, "automation_level": "L3", "keywords": ["EAP", "FDC", "APC", "SPC", "BI"], "debug": true}`
- `_meta_debug.input_context`: `{"industry": "E", "scale_raw": "S2", "scale_normalized": "S2"}`
- `_meta_debug.selected_candidates`: `["MES", "SFC", "TRACE_EXEC", "LINE_EXEC"]`
- `_debug_trace`: `{"selected_candidates": ["MES", "SFC", "TRACE_EXEC", "LINE_EXEC"], "role_sections_count": 2, "cap_sections_count": 4, "iface_sections_count": 4}`
- role 요약:
  - 基础执行系统: MES（制造执行系统） / SFC
  - 多线扩展系统: TRACE_EXEC / LINE_EXEC
- cap 요약:
  - MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制
  - SFC: 工位执行与报工 / 产线节奏控制
  - TRACE_EXEC: 批次/序列号追溯 / 关键件绑定
- iface 요약:
  - MES（制造执行系统）: import:Recipe / Recipe management / Batch record / export:产出/报工 / WIP状态 / 追溯链路
  - SFC: import:MES工单 / 设备/条码 / 作业指导 / export:报工数据 / WIP状态 / 异常事件
  - TRACE_EXEC: import:MES执行数据 / 检验/测试数据 / 物料批次 / export:追溯链路 / 追溯报告 / 合规证据

### F

- payload: `{"industry": "F", "scale": {"equipment": "M", "employees": "M", "revenue": "M"}, "automation_level": "L3", "keywords": ["EAP", "FDC", "APC", "SPC", "BI"], "debug": true}`
- `_meta_debug.input_context`: `{"industry": "F", "scale_raw": "S2", "scale_normalized": "S2"}`
- `_meta_debug.selected_candidates`: `["MES", "BATCH_EXEC", "ROUTE_EXEC"]`
- `_debug_trace`: `{"selected_candidates": ["MES", "BATCH_EXEC", "ROUTE_EXEC"], "role_sections_count": 2, "cap_sections_count": 3, "iface_sections_count": 3}`
- role 요약:
  - 基础执行系统: MES（制造执行系统）
  - 多线扩展系统: BATCH_EXEC / ROUTE_EXEC
- cap 요약:
  - MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制
  - BATCH_EXEC: 批次生产控制 / 配方与阶段控制
  - ROUTE_EXEC: 工艺路线执行 / 配方/参数下发
- iface 요약:
  - MES（制造执行系统）: import:包装线 / 报工 / ERP订单 / export:产出/报工 / WIP状态 / 追溯链路
  - BATCH_EXEC: import:MES/ERP批次需求 / 配方库 / 质量放行 / export:批次记录 / 批次状态 / 放行事件
  - ROUTE_EXEC: import:PLM/工艺主数据 / MES工单 / 设备/配方库 / export:工序执行记录 / 参数履历 / 合规结果

### G

- payload: `{"industry": "G", "scale": {"equipment": "M", "employees": "M", "revenue": "M"}, "automation_level": "L3", "keywords": ["EAP", "FDC", "APC", "SPC", "BI"], "debug": true}`
- `_meta_debug.input_context`: `{"industry": "G", "scale_raw": "S2", "scale_normalized": "S2"}`
- `_meta_debug.selected_candidates`: `["MES", "BATCH_EXEC", "EBR", "TRACE_EXEC"]`
- `_debug_trace`: `{"selected_candidates": ["MES", "BATCH_EXEC", "EBR", "TRACE_EXEC"], "role_sections_count": 2, "cap_sections_count": 4, "iface_sections_count": 4}`
- role 요약:
  - 基础执行系统: MES（制造执行系统）
  - 多线扩展系统: BATCH_EXEC / EBR
- cap 요약:
  - MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制
  - BATCH_EXEC: 批次生产控制 / 配方与阶段控制
  - EBR: 电子批记录 / 电子签名与审计
- iface 요약:
  - MES（制造执行系统）: import:QMS / LIMS / EBR / export:产出/报工 / WIP状态 / 追溯链路
  - BATCH_EXEC: import:MES/ERP批次需求 / 配方库 / 质量放行 / export:批次记录 / 批次状态 / 放行事件
  - EBR: import:MES批次 / LIMS/检验 / 设备数据 / export:审计包 / 合规告警 / 签名/审计日志

### H

- payload: `{"industry": "H", "scale": {"equipment": "M", "employees": "M", "revenue": "M"}, "automation_level": "L3", "keywords": ["EAP", "FDC", "APC", "SPC", "BI"], "debug": true}`
- `_meta_debug.input_context`: `{"industry": "H", "scale_raw": "S2", "scale_normalized": "S2"}`
- `_meta_debug.selected_candidates`: `["MES", "SFC", "LINE_EXEC", "WO_EXEC"]`
- `_debug_trace`: `{"selected_candidates": ["MES", "SFC", "LINE_EXEC", "WO_EXEC"], "role_sections_count": 2, "cap_sections_count": 4, "iface_sections_count": 4}`
- role 요약:
  - 基础执行系统: MES（制造执行系统） / SFC
  - 多线扩展系统: LINE_EXEC
- cap 요약:
  - MES（制造执行系统）: 工单/工序执行控制与报工 / WIP在制可视化与滞留控制
  - SFC: 工位执行与报工 / 产线节奏控制
  - LINE_EXEC: 产线节奏控制 / 工位同步
- iface 요약:
  - MES（制造执行系统）: import:序列号 / Test station / SMT/AOI/SPI / export:产出/报工 / WIP状态 / 追溯链路
  - SFC: import:MES工单 / 设备/条码 / 作业指导 / export:报工数据 / WIP状态 / 异常事件
  - LINE_EXEC: import:MES/排程 / 设备状态 / WMS / export:产线状态 / 产出/报工 / 齐套预警

## 5) 수집 총평

- A~H 대부분에서 normalize 결과는 `S2`로 수렴했다.
- 후보 시스템은 산업별로 일부 차이가 있으며, MES 중심 공통축이 보였다.
- B/C/H는 라인/라우트/추적 관련 표현이 일부 확인됐다.
- F/G는 배치/규제 성격 후보(BATCH_EXEC/EBR) 포함이 확인됐다.
- 본 스냅샷은 Step C의 산업 정의 대조/판정 입력으로 사용 가능하다.
