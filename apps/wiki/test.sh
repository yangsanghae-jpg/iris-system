#!/bin/bash
set -e

echo "== health =="
curl -s http://127.0.0.1:18081/health
echo
echo

echo "== ingest =="
curl -s -X POST http://127.0.0.1:18081/wiki/ingest
echo
echo

echo "== query =="
curl -s -X POST http://127.0.0.1:18081/wiki/query \
  -H "Content-Type: application/json" \
  -d '{"question":"MES가 무엇인지 위키 기준으로 설명해줘"}'
echo
echo

echo "== lint (structured: orphan / broken / duplicate / weak) =="
LINT_JSON=$(curl -s http://127.0.0.1:18081/wiki/lint)
echo "$LINT_JSON"
echo
echo "$LINT_JSON" | python3 -c "import json,sys; d=json.load(sys.stdin); \
  assert 'summary' in d and 'issues' in d and 'policy_checks' in d; \
  assert d['summary'].get('quality_gate') in ('pass','warning','block'); \
  pc=d['policy_checks']; \
  assert 'merge_allowed' in pc and 'broken_links_priority' in pc; \
  i=d['issues']; \
  assert 'orphan_pages' in i and 'broken_links' in i and 'duplicate_candidates' in i and 'weak_pages' in i; \
  names=','.join(x['file'] for x in i['orphan_pages']); \
  assert 'z_lint_orphan.md' in names; \
  bl=' '.join(x['link'] for x in i['broken_links']); \
  assert 'missing_target__lint_xyz_001' in bl; \
  print('lint structure + fixture checks: ok')"
echo
echo

echo "== history (after ingest) =="
curl -s "http://127.0.0.1:18081/wiki/history?limit=10"
echo
echo

echo "== ingest missing file (history should record error) =="
curl -s -X POST http://127.0.0.1:18081/wiki/ingest \
  -H "Content-Type: application/json" \
  -d '{"files":["__nonexistent__.txt"]}'
echo
echo

echo "== history (recent, includes error row) =="
curl -s "http://127.0.0.1:18081/wiki/history?limit=10"
echo
echo

echo "== ingest mes.txt first time (or force reprocess) =="
curl -s -X POST http://127.0.0.1:18081/wiki/ingest \
  -H "Content-Type: application/json" \
  -d '{"files":["mes.txt"],"force":true}'
echo
echo

echo "== ingest mes.txt again without force (expect skipped) =="
curl -s -X POST http://127.0.0.1:18081/wiki/ingest \
  -H "Content-Type: application/json" \
  -d '{"files":["mes.txt"],"force":false}'
echo
echo

echo "== ingest mes.txt with force true (expect processed, not skipped) =="
curl -s -X POST http://127.0.0.1:18081/wiki/ingest \
  -H "Content-Type: application/json" \
  -d '{"files":["mes.txt"],"force":true}'
echo
echo

echo "== history (check skipped + ok rows) =="
curl -s "http://127.0.0.1:18081/wiki/history?limit=15"
echo
