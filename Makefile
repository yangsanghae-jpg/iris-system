.PHONY: ingest-reference reindex-fts stats clean-reference \
        migrate-v2.6 migrate-v2.6-status migrate-v2.6-down migrate-v2.6-dry \
        eval eval-baseline test

PYTHON ?= python3
ROOT := $(shell pwd)

ingest-reference:
	$(PYTHON) apps/ingest/reference_diagnosis.py

reindex-fts:
	@sqlite3 knowledge/_index.db "DELETE FROM documents_fts; \
		INSERT INTO documents_fts (rowid, title, body) \
		SELECT d.rowid, COALESCE(d.title,''), COALESCE(GROUP_CONCAT(c.text, char(10)),'') \
		FROM documents d LEFT JOIN chunks c ON c.doc_id=d.doc_id GROUP BY d.doc_id;"

stats:
	@sqlite3 knowledge/_index.db "SELECT lane, area, COUNT(*) FROM documents GROUP BY 1,2 ORDER BY 3 DESC"

clean-reference:
	@sqlite3 knowledge/_index.db "DELETE FROM documents WHERE lane='reference';"

# --- V2.5.1 Phase 1 — Schema 마이그레이션 ---

migrate-v2.6-status:
	$(PYTHON) -m apps.ingest.migrate status

migrate-v2.6-dry:
	$(PYTHON) -m apps.ingest.migrate up --dry-run

migrate-v2.6:
	$(PYTHON) -m apps.ingest.migrate up

migrate-v2.6-down:
	@echo "사용: make migrate-v2.6-down TO=000"
	@test -n "$(TO)" || (echo "[ERROR] TO=<version> 필요"; exit 2)
	$(PYTHON) -m apps.ingest.migrate down --to $(TO)

# --- V2.6 Phase 4 — Golden Q&A 평가 하네스 ---

eval:
	@mkdir -p eval_runs
	@ts=$$(date -u +%Y-%m-%d_%H%M); \
	out=eval_runs/$$ts/run.json; \
	mkdir -p eval_runs/$$ts; \
	$(PYTHON) -m apps.eval.run_golden --out $$out

eval-baseline:
	@mkdir -p eval_runs
	@ts=$$(date -u +%Y-%m-%d_%H%M); \
	out=eval_runs/baseline_$$ts.json; \
	$(PYTHON) -m apps.eval.run_golden --out $$out

# --- 회귀 테스트 ---

test:
	$(PYTHON) -m pytest tests/ -v
