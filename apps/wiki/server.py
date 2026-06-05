from fastapi import FastAPI, Query
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
    return query(req.question)


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
