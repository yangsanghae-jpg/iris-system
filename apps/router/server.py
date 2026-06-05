from typing import Any, Dict, Optional

import os

import requests
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI(
    title="IRIS 라우터",
    version="0.1.0",
    description=(
        "IRIS 시스템의 입력 분기 관리 API입니다. "
        "운영자가 사용자 요청이 어느 경로로 전달되는지 확인하고 테스트할 수 있습니다."
    ),
)

# Phase 0.5: 컨테이너에서는 서비스명, 호스트 네이티브 실행 시 127.0.0.1
WIKI_BASE_URL = os.environ.get("WIKI_BASE_URL", "http://127.0.0.1:18081")

route_map = {
    "knowledge_ingest": f"{WIKI_BASE_URL}/wiki/ingest",
    "knowledge_merge": f"{WIKI_BASE_URL}/wiki/merge",
    "knowledge_query": f"{WIKI_BASE_URL}/wiki/query",
    "knowledge_lint": f"{WIKI_BASE_URL}/wiki/lint",
}

INGEST_KEYWORDS = [
    "지식베이스에 반영",
    "위키에 넣어",
    "메모를 정리해서 저장",
    "지식으로 축적",
]

QUERY_KEYWORDS = [
    "위키 기준으로 설명",
    "지식베이스에서 찾아",
    "위키에서",
]

LINT_KEYWORDS = [
    "위키 중복 점검",
    "연결 안 된 문서",
    "지식 구조 점검",
    "중복 문서 점검",
]

MERGE_KEYWORDS = [
    "위키 병합",
    "지식 병합",
    "merge로 반영",
    "통합 반영",
]


class RouteRequest(BaseModel):
    model_config = ConfigDict(title="경로판단요청")

    user_text: str = Field(..., description="분기 판단에 사용할 사용자 입력 문장")
    files: list[str] | None = Field(
        None,
        description="지식 반영·지식 병합 시 처리할 raw 파일명 목록(선택)",
    )
    force: bool = Field(
        False,
        description="지식 반영 시 동일 내용이라도 다시 처리할지 여부(선택)",
    )


def wrap_response(route: str, ok: bool, result: Any, error: Optional[str] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "route": route,
        "ok": ok,
        "source": "wiki",
        "result": result,
    }
    if error:
        payload["error"] = error
    return payload


def detect_route(user_text: str) -> str:
    text = user_text.strip().lower()
    if any(keyword in text for keyword in INGEST_KEYWORDS):
        return "knowledge_ingest"
    if any(keyword in text for keyword in MERGE_KEYWORDS):
        return "knowledge_merge"
    if any(keyword in text for keyword in LINT_KEYWORDS):
        return "knowledge_lint"
    if any(keyword in text for keyword in QUERY_KEYWORDS):
        return "knowledge_query"
    return "chat"


def call_knowledge_route(
    route: str,
    user_text: str,
    files: list[str] | None = None,
    force: bool = False,
) -> Dict[str, Any]:
    try:
        if route == "knowledge_ingest":
            payload: Dict[str, Any] = {"force": force}
            if files is not None:
                payload["files"] = files
            resp = requests.post(route_map[route], json=payload, timeout=300)
        elif route == "knowledge_merge":
            payload = {"force": force, "files": files or []}
            resp = requests.post(route_map[route], json=payload, timeout=300)
        elif route == "knowledge_query":
            resp = requests.post(route_map[route], json={"question": user_text}, timeout=300)
        elif route == "knowledge_lint":
            resp = requests.get(route_map[route], timeout=60)
        else:
            return {
                "route": "chat",
                "ok": True,
                "source": "router",
                "result": {"message": "knowledge route not selected"},
            }

        resp.raise_for_status()
        return wrap_response(route=route, ok=True, result=resp.json())
    except Exception as e:
        return wrap_response(route=route, ok=False, result=None, error=str(e))


@app.get(
    "/health",
    tags=["상태"],
    summary="상태 확인",
    description="라우터 서버의 현재 동작 상태를 확인합니다.",
)
def health() -> Dict[str, Any]:
    return {"ok": True, "service": "iris-router"}


@app.post(
    "/route",
    tags=["경로"],
    summary="경로 판단",
    description=(
        "사용자 입력을 분석하여 적절한 처리 경로로 전달합니다. "
        "지식 반영·지식 조회·품질 점검 요청 여부를 확인할 수 있습니다."
    ),
)
def route(req: RouteRequest) -> Dict[str, Any]:
    selected_route = detect_route(req.user_text)
    return call_knowledge_route(
        route=selected_route,
        user_text=req.user_text,
        files=req.files,
        force=req.force,
    )
