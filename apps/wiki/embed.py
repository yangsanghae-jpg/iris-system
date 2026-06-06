"""V2.6 Phase 5.4 — Ollama 임베딩 + 텍스트 정규화.

Ollama /api/embeddings 호출, nomic-embed-text (768-dim).

V2.5.3 §17 (M5 발견): nomic-embed-text는 컨텍스트 길이 한계가 있어
~2,500 char 이상 입력 시 HTTP 500. EMBED_MAX_CHARS로 안전 truncation.
M5 reference 630건 ingest 중 발견 — `ref:catalog:ch1_drivers_catalog`
4,996 chars 청크가 실패. M2 시드 5건에서는 미발견.
"""
from __future__ import annotations

import os

import requests

OLLAMA_EMBED_URL = os.environ.get(
    "OLLAMA_EMBED_URL",
    "http://127.0.0.1:11434/api/embeddings",
)
EMBED_MODEL = os.environ.get("IRIS_EMBED_MODEL", "nomic-embed-text")
EMBED_DIM = 768   # nomic-embed-text

# V2.5.3 §17: 안전 truncation (env override 가능)
# nomic-embed-text context length ≈ 2048 tokens, 토큰 밀집 JSON은 ~2500 chars에서 한계
EMBED_MAX_CHARS = int(os.environ.get("IRIS_EMBED_MAX_CHARS", "2500"))


def _truncate(text: str) -> str:
    """안전 마진 — 토큰 밀집 텍스트(JSON 등)도 context length 안에 들어가도록."""
    if not text:
        return ""
    if len(text) <= EMBED_MAX_CHARS:
        return text
    return text[:EMBED_MAX_CHARS]


def embed(text: str, *, timeout: int = 30) -> list[float]:
    """단일 텍스트 → 768-dim 임베딩."""
    if not text or not text.strip():
        return [0.0] * EMBED_DIM
    body = _truncate(text)
    r = requests.post(
        OLLAMA_EMBED_URL,
        json={"model": EMBED_MODEL, "prompt": body},
        timeout=timeout,
    )
    r.raise_for_status()
    data = r.json()
    vec = data.get("embedding")
    if not vec or len(vec) != EMBED_DIM:
        raise RuntimeError(f"Unexpected embedding response: dim={len(vec) if vec else 0}")
    return vec


def embed_batch(texts: list[str], *, timeout: int = 60) -> list[list[float]]:
    """N개 → N벡터. Ollama는 batch API 없으므로 순차 호출."""
    return [embed(t, timeout=timeout) for t in texts]
