"""V2.6 Phase 5.4 — Ollama 임베딩 + 텍스트 정규화.

Ollama /api/embeddings 호출, nomic-embed-text (768-dim).
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


def embed(text: str, *, timeout: int = 30) -> list[float]:
    """단일 텍스트 → 768-dim 임베딩."""
    if not text or not text.strip():
        return [0.0] * EMBED_DIM
    r = requests.post(
        OLLAMA_EMBED_URL,
        json={"model": EMBED_MODEL, "prompt": text},
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
