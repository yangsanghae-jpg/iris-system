from fastapi import FastAPI, Header, Query, Request
from pydantic import BaseModel, ConfigDict, Field

try:
    from .engine import ingest, lint, merge, query
    from .history import list_recent_history
except ImportError:
    from engine import ingest, lint, merge, query
    from history import list_recent_history

app = FastAPI(
    title="IRIS 위키 엔진",
    version="0.1.0",
    description=(
        "IRIS 지식 저장소 관리 API입니다. "
        "원본 문서 반영, 지식 조회, 품질 점검, 처리 이력을 운영자가 확인할 수 있습니다.\n\n"
        "권장 사용 순서:\n"
        "1) /wiki/ingest 로 raw 반영\n"
        "2) /wiki/lint 로 품질 점검\n"
        "3) 필요 시 /wiki/merge 로 통합 반영\n"
        "4) /wiki/query 로 조회 검증\n"
        "5) /wiki/history 로 처리 이력 추적"
    ),
)


class QueryRequest(BaseModel):
    model_config = ConfigDict(title="지식조회요청")

    question: str = Field(
        ...,
        description=(
            "위키 문서를 바탕으로 답할 질문입니다. "
            "예: 'MES 생산 실행 시스템 핵심 기능을 요약해줘'"
        ),
    )


class IngestRequest(BaseModel):
    model_config = ConfigDict(title="지식반영요청")

    files: list[str] | None = Field(
        None,
        description=(
            "처리할 raw 파일명 목록입니다. "
            "비우면 raw 디렉터리 전체를 대상으로 반영합니다."
        ),
    )
    force: bool = Field(
        False,
        description="동일 내용이라도 스킵하지 않고 강제로 다시 반영할지 여부입니다.",
    )


class MergeRequest(BaseModel):
    model_config = ConfigDict(title="지식병합요청")

    files: list[str] = Field(
        ...,
        min_length=1,
        description="병합에 사용할 raw 파일명 목록입니다. 최소 1개 이상 필요합니다.",
    )
    force: bool = Field(
        False,
        description="예약 필드입니다(향후 동일 raw 스킵 정책 등 확장 시 사용).",
    )


@app.get(
    "/health",
    tags=["상태"],
    summary="상태 확인",
    description=(
        "위키 엔진 서버 프로세스의 기본 동작 상태를 확인합니다.\n\n"
        "- `ok=true`: 서버가 요청을 정상 수신/응답 가능\n"
        "- 이 API는 앱 생존 여부 확인용이며, 지식 품질 검증은 /wiki/lint 를 사용하세요."
    ),
)
def health():
    return {"ok": True, "service": "iris-wiki-engine"}


@app.post(
    "/wiki/ingest",
    tags=["지식"],
    summary="지식 반영",
    description=(
        "raw 문서를 읽어 wiki 문서를 생성/갱신합니다.\n\n"
        "- 신규 원본 추가 후 첫 반영 단계\n"
        "- `files` 지정 시 선택 반영, 미지정 시 전체 반영\n"
        "- `force=true` 시 동일 내용도 재처리\n"
        "- 처리 결과(성공/스킵/오류)는 처리 이력에 기록됩니다."
    ),
)
def wiki_ingest(req: IngestRequest | None = None):
    if req is None:
        return ingest(files=None, force=False)
    return ingest(files=req.files, force=req.force)


@app.post(
    "/wiki/merge",
    tags=["지식"],
    summary="지식 병합",
    description=(
        "기존 wiki와 신규 raw 내용을 비교해 지식을 통합 반영합니다.\n\n"
        "- 중복/충돌 가능성이 있는 주제를 정리할 때 사용\n"
        "- 품질 점검 결과(`quality_gate`)에 따라 병합이 제한될 수 있음\n"
        "- 운영 권장: ingest -> lint 확인 후 merge 실행"
    ),
)
def wiki_merge(req: MergeRequest):
    return merge(files=req.files, force=req.force)


@app.post(
    "/wiki/query",
    tags=["지식"],
    summary="지식 조회",
    description=(
        "wiki 문서를 근거로 질의응답을 수행합니다.\n\n"
        "- 질문 입력 시 답변(`answer`)을 생성\n"
        "- 근거 후보 문서(`candidates`)를 함께 반환할 수 있음\n"
        "- 최신 반영 내용을 보려면 ingest/merge 이후 조회하세요."
    ),
)
def wiki_query(req: QueryRequest):
    from fastapi.responses import JSONResponse
    from .secure_gate import filter_secure_rows

    result = query(req.question)
    # V2.6 Phase 2.4 — K5 secure 응답 차단
    candidates = result.get("candidates", [])
    if isinstance(candidates, list):
        filtered, excluded = filter_secure_rows(candidates)
        result["candidates"] = filtered
        return JSONResponse(
            content=result,
            headers={"X-IRIS-Secure-Excluded": str(excluded)},
        )
    return result


@app.get(
    "/wiki/lint",
    tags=["품질"],
    summary="지식 품질 점검",
    description=(
        "wiki 문서 품질을 자동 점검합니다.\n\n"
        "- 점검 항목: 중복, 깨진 링크, 고립 문서, 약한 문서\n"
        "- 결과: `quality_gate`(pass/warn/block), `policy_checks`\n"
        "- `block`이면 운영 반영(특히 merge) 전에 수정이 필요합니다."
    ),
)
def wiki_lint():
    return lint()


@app.get(
    "/wiki/history",
    tags=["이력"],
    summary="처리 이력 조회",
    description=(
        "지식 반영/건너뜀/오류/병합 등의 최근 처리 이력을 조회합니다.\n\n"
        "- 문제 발생 시 원인 추적용으로 사용\n"
        "- `limit`으로 조회 건수를 조절(기본 20, 최대 500)"
    ),
)
def wiki_history(
    limit: int = Query(20, ge=1, le=500, description="최대 조회 건수"),
):
    items = list_recent_history(limit=limit)
    return {"status": "ok", "count": len(items), "items": items}


# ─── V2.6 Phase 5 — K5 표준 API (/api/v1/retrieval) ──────────────────────

import time
try:
    from .dispatcher import dispatch
    from .secure_gate import filter_secure_rows
    from . import telemetry
except ImportError:
    from dispatcher import dispatch
    from secure_gate import filter_secure_rows
    import telemetry


@app.get(
    "/api/v1/retrieval",
    tags=["K5 표준"],
    summary="K5 표준 retrieval (V2.5 §5 정본)",
    description=(
        "단일 retrieval 엔드포인트 (V2.5 §5).\n\n"
        "- 헤더 `X-IRIS-Caller` 필수 (누락 시 telemetry에 FAULT:anonymous)\n"
        "- 응답 헤더 `X-IRIS-Secure-Excluded` (V2.6 Phase 2)\n"
        "- 응답 헤더 `X-IRIS-Mode` (실제 사용된 모드, auto 폴백 시 변경됨)\n"
        "- mode=auto 휴리스틱: matrix(키 셋 있음) → fts → semantic(활성 시)"
    ),
)
def k5_retrieval(
    request: Request,
    q: str = Query("", description="검색 텍스트"),
    mode: str = Query("auto", pattern="^(auto|matrix|fts|semantic)$"),
    industry: str | None = Query(None),
    area: str | None = Query(None),
    level: str | None = Query(None),
    lane: str | None = Query(None, description="기본 None=전체 (단 secure는 자동 제외)"),
    limit: int = Query(20, ge=1, le=100),
    x_iris_caller: str | None = Header(None, alias="X-IRIS-Caller"),
):
    from fastapi.responses import JSONResponse

    t0 = time.perf_counter()
    rows, effective_mode, fallback, fallback_to = dispatch(
        mode, q,
        industry=industry, area=area, level=level, lane=lane, limit=limit,
    )
    filtered, excluded = filter_secure_rows(rows)
    latency_ms = (time.perf_counter() - t0) * 1000.0

    telemetry.append(
        endpoint="/api/v1/retrieval",
        caller=x_iris_caller,
        mode=effective_mode,
        industry=industry, area=area, lane=lane,
        query_len=len(q or ""),
        result_count=len(filtered),
        latency_ms=latency_ms,
        secure_excluded=excluded,
        fallback=fallback,
        fallback_to=fallback_to,
    )

    return JSONResponse(
        content={
            "ok": True,
            "mode": effective_mode,
            "fallback": fallback,
            "fallback_to": fallback_to,
            "count": len(filtered),
            "results": filtered,
        },
        headers={
            "X-IRIS-Mode": effective_mode,
            "X-IRIS-Secure-Excluded": str(excluded),
            "X-IRIS-Fallback": "1" if fallback else "0",
        },
    )


@app.get(
    "/api/v1/skills/knowledge_search",
    tags=["K5 Skill"],
    summary="Skill: knowledge_search (V2.6 Phase 5.8 시범)",
    description=(
        "외부 LLM Wiki V1.0의 Knowledge_Search Skill 사상을 thin wrapper로 채용.\n"
        "fts + semantic(활성 시) 앙상블, lane=secure 자동 제외, X-IRIS-Caller 필수."
    ),
)
def skill_knowledge_search(
    request: Request,
    q: str = Query(..., description="검색 텍스트 (필수)"),
    industry: str | None = Query(None),
    area: str | None = Query(None),
    limit: int = Query(10, ge=1, le=50),
    x_iris_caller: str | None = Header(None, alias="X-IRIS-Caller"),
):
    """fts + semantic 앙상블 — 중복 doc_id 제거, fts 우선."""
    from fastapi.responses import JSONResponse
    from .retrieval import query_fts
    from .semantic import is_active as semantic_active, query_semantic

    t0 = time.perf_counter()
    fts_rows = query_fts(q, industry=industry, area=area, lane=None, limit=limit)
    sem_rows = (
        query_semantic(q, industry=industry, area=area, lane=None, limit=limit)
        if semantic_active() else []
    )

    seen: set[str] = set()
    merged: list[dict] = []
    for r in fts_rows + sem_rows:
        did = r.get("doc_id")
        if did in seen:
            continue
        seen.add(did)
        merged.append(r)

    filtered, excluded = filter_secure_rows(merged)
    latency_ms = (time.perf_counter() - t0) * 1000.0

    telemetry.append(
        endpoint="/api/v1/skills/knowledge_search",
        caller=x_iris_caller,
        mode="ensemble",
        industry=industry, area=area, lane=None,
        query_len=len(q or ""),
        result_count=len(filtered),
        latency_ms=latency_ms,
        secure_excluded=excluded,
        fallback=False,
        fallback_to=None,
        extra={"fts_count": len(fts_rows), "semantic_count": len(sem_rows)},
    )

    return JSONResponse(
        content={
            "ok": True,
            "skill": "knowledge_search",
            "fts_count": len(fts_rows),
            "semantic_count": len(sem_rows),
            "count": len(filtered),
            "results": filtered[:limit],
        },
        headers={
            "X-IRIS-Skill": "knowledge_search",
            "X-IRIS-Secure-Excluded": str(excluded),
        },
    )
