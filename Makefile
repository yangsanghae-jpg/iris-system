.PHONY: ingest-reference reindex-fts stats clean-reference

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
