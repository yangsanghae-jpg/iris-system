#!/bin/bash
set -e

WIKI_PORT="${WIKI_PORT:-18081}"
ROUTER_PORT="${ROUTER_PORT:-18080}"
WIKI_BASE="http://127.0.0.1:${WIKI_PORT}"
ROUTER_BASE="http://127.0.0.1:${ROUTER_PORT}"

echo "== 1) Wiki health (${WIKI_BASE}/health) =="
curl -sf "${WIKI_BASE}/health"
echo
echo

echo "== 2) Router health (${ROUTER_BASE}/health) =="
curl -sf "${ROUTER_BASE}/health"
echo
echo

echo "== A) ingest via Router (files + force) =="
A=$(curl -s -X POST "${ROUTER_BASE}/route" \
  -H "Content-Type: application/json" \
  -d '{"user_text":"이 문서를 지식베이스에 반영해","files":["mes.txt"],"force":false}')
echo "$A"
echo "$A" | python3 -c "
import json, sys
d = json.load(sys.stdin)
assert d['route'] == 'knowledge_ingest', d
assert d['ok'] is True, d
assert d['source'] == 'wiki', d
assert 'result' in d and d['result'] is not None, d
r = d['result']
assert ('processed_count' in r) or ('skipped_count' in r), r
print('A: ok')
"
echo

echo "== B) query via Router (answer + candidates) =="
B=$(curl -s -X POST "${ROUTER_BASE}/route" \
  -H "Content-Type: application/json" \
  -d '{"user_text":"위키에서 MES 설명 찾아봐"}')
echo "$B"
echo "$B" | python3 -c "
import json, sys
d = json.load(sys.stdin)
assert d['route'] == 'knowledge_query', d
assert d['ok'] is True, d
assert d['source'] == 'wiki', d
res = d['result']
assert 'answer' in res and 'candidates' in res, res
print('B: ok')
"
echo

echo "== C) lint via Router (summary + issues) =="
C=$(curl -s -X POST "${ROUTER_BASE}/route" \
  -H "Content-Type: application/json" \
  -d '{"user_text":"위키 중복 문서 점검해"}')
echo "$C"
echo "$C" | python3 -c "
import json, sys
d = json.load(sys.stdin)
assert d['route'] == 'knowledge_lint', d
assert d['ok'] is True, d
assert d['source'] == 'wiki', d
res = d['result']
assert 'summary' in res and 'issues' in res, res
assert 'issue_count' in res['summary'], res['summary']
assert res['summary'].get('quality_gate') in ('pass', 'warning', 'block'), res['summary']
assert 'policy_checks' in res, res
pc = res['policy_checks']
for k in ('broken_links_priority', 'duplicate_review_needed', 'orphan_review_needed',
          'weak_pages_review_needed', 'merge_allowed'):
    assert k in pc, pc
print('C: ok')
"
echo

echo "== D) chat fallback (no Wiki call) =="
D=$(curl -s -X POST "${ROUTER_BASE}/route" \
  -H "Content-Type: application/json" \
  -d '{"user_text":"MES가 뭐야?"}')
echo "$D"
echo "$D" | python3 -c "
import json, sys
d = json.load(sys.stdin)
assert d['route'] == 'chat', d
assert d['ok'] is True, d
assert d['source'] == 'router', d
assert d['result'].get('message'), d
print('D: ok')
"
echo

echo "E2E router→wiki checks passed (ROUTER_PORT=${ROUTER_PORT}, WIKI_PORT=${WIKI_PORT})."
