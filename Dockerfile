FROM python:3.11-slim

# 컨테이너 시그널 핸들링 + 최소 빌드 도구
RUN apt-get update && apt-get install -y --no-install-recommends \
    tini curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 의존성을 코드보다 먼저 — 캐시 활용
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# 코드. .dockerignore가 .venv / __pycache__ / .nosync 제외
COPY apps/ /app/apps/
COPY knowledge/ /app/knowledge/

# storage는 compose에서 ~/iris-local/storage를 마운트
# knowledge/_index.db는 compose에서 knowledge/.nosync 마운트로 덮음

# K5 Phase 0.5: 두 서비스가 같은 이미지를 공유, command만 다름
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    OLLAMA_URL=http://host.docker.internal:11434/api/generate \
    WIKI_MODEL=qwen3:30b \
    KNOWLEDGE_BASE_PATH=/app/knowledge \
    STORAGE_PATH=/app/storage \
    WIKI_BASE_URL=http://iris-k5-wiki:18081

ENTRYPOINT ["/usr/bin/tini", "--"]

# 기본은 wiki. router는 compose에서 command 오버라이드.
CMD ["uvicorn", "apps.wiki.server:app", "--host", "0.0.0.0", "--port", "18081"]
