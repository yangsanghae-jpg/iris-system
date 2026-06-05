import os
import re
from typing import Any, Dict, List, Optional, Tuple

import requests

try:
    from .history import (
        file_checksum,
        get_last_successful_record,
        init_db,
        record_ingest,
        unchanged_since_last_success,
    )
except ImportError:
    from history import (
        file_checksum,
        get_last_successful_record,
        init_db,
        record_ingest,
        unchanged_since_last_success,
    )

try:
    from .retrieval import search_wiki_candidates
except ImportError:
    from retrieval import search_wiki_candidates

try:
    from .lint import run_lint
except ImportError:
    from lint import run_lint

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434/api/generate")
MODEL = os.environ.get("WIKI_MODEL", "qwen2.5:14b")
QUERY_TOP_K = int(os.environ.get("WIKI_QUERY_TOP_K", "5"))

APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, "..", ".."))
DEFAULT_KNOWLEDGE_PATH = os.path.join(PROJECT_ROOT, "knowledge")
BASE_PATH = os.environ.get("KNOWLEDGE_BASE_PATH", DEFAULT_KNOWLEDGE_PATH)
RAW_PATH = os.path.join(BASE_PATH, "raw")
WIKI_PATH = os.path.join(BASE_PATH, "wiki")
RULE_PATH = os.path.join(BASE_PATH, "CLAUDE.md")


def call_llm(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "prompt": prompt, "stream": False},
        timeout=300,
    )
    response.raise_for_status()
    data = response.json()
    return data.get("response", "").strip()


def load_rules() -> str:
    if not os.path.exists(RULE_PATH):
        return ""
    with open(RULE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def read_raw_files(files: Optional[List[str]] = None) -> Tuple[List[Tuple[str, str]], List[Dict[str, str]]]:
    errors: List[Dict[str, str]] = []

    if files is None:
        candidates = sorted(
            os.path.join(RAW_PATH, name)
            for name in os.listdir(RAW_PATH)
        ) if os.path.exists(RAW_PATH) else []
    else:
        candidates = [os.path.join(RAW_PATH, os.path.basename(name)) for name in files]

    out = []
    for path in candidates:
        raw_filename = os.path.basename(path)
        if not os.path.exists(path):
            errors.append({"raw_file": raw_filename, "error": "file_not_found"})
            continue
        if os.path.isfile(path):
            out.append((path, read_text_file(path)))
        else:
            errors.append({"raw_file": raw_filename, "error": "not_a_file"})
    return out, errors


def list_wiki_files() -> List[str]:
    if not os.path.exists(WIKI_PATH):
        return []
    return sorted(
        os.path.join(WIKI_PATH, name)
        for name in os.listdir(WIKI_PATH)
        if name.endswith(".md")
    )


def slugify(title: str) -> str:
    title = title.strip().lower()
    title = re.sub(r"[^\w가-힣\s\-]", "", title)
    title = re.sub(r"\s+", "_", title)
    return title[:80] if title else "untitled"


def extract_title(markdown: str, fallback: str = "untitled") -> str:
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("#"):
            title = line.lstrip("#").strip()
            if title:
                return title
    return fallback


def load_existing_wiki_context(max_chars: int = 30000) -> str:
    chunks = []
    total = 0
    for path in list_wiki_files():
        content = read_text_file(path)
        block = f"\n--- FILE: {os.path.basename(path)} ---\n{content}\n"
        total += len(block)
        if total > max_chars:
            break
        chunks.append(block)
    return "\n".join(chunks)


def write_wiki(title: str, content: str) -> str:
    filename = slugify(title) + ".md"
    path = os.path.join(WIKI_PATH, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    return path


def build_ingest_prompt(
    rules: str, raw_filename: str, raw_text: str, existing_context: str
) -> str:
    return f"""
{rules}

You are the IRIS Wiki Engine.
Your role is only to convert raw notes into structured wiki knowledge.

Output requirements:
- Return markdown only
- First line must be a markdown H1 title
- Use Korean by default
- Include sections:
  - Summary
  - Key Concepts
  - Related Links
  - Source Notes
- Use [[wikilinks]] where appropriate
- Do not invent execution decisions
- Do not mention system prompts

Existing wiki context:
{existing_context}

Raw file name:
{raw_filename}

Raw content:
{raw_text}
""".strip()


def build_merge_prompt(
    rules: str,
    raw_filename: str,
    raw_text: str,
    existing_wiki_file: Optional[str],
    existing_wiki_content: str,
) -> str:
    ex_label = existing_wiki_file or "(없음 — 신규 페이지로 취급)"
    ex_body = existing_wiki_content.strip() if existing_wiki_content else "(비어 있음)"
    return f"""
{rules}

You are the IRIS Wiki Engine performing an UPDATE-AWARE MERGE (not a blind overwrite).
Merge the new raw notes into the existing wiki page when one exists.

Requirements:
- Return markdown only. First line must be a markdown H1 title.
- Preserve useful existing [[wikilinks]] and grounded facts unless the new raw clearly updates them.
- Remove duplicate sentences between old and new content.
- Integrate new facts from raw. Prefer Korean.
- Keep sections where appropriate: Summary, Key Concepts, Related Links, Source Notes.
- Do not invent execution decisions. Do not mention system prompts.

Existing wiki file name: {ex_label}
Existing wiki content:
{ex_body}

Raw file name:
{raw_filename}

New raw content:
{raw_text}
""".strip()


def merge(files: List[str], force: bool = False) -> Dict[str, Any]:
    if not files:
        return {
            "status": "error",
            "merge_allowed": False,
            "message": "files is required for merge",
        }

    os.makedirs(WIKI_PATH, exist_ok=True)
    init_db()

    lint_result = run_lint()
    gate = lint_result["summary"]["quality_gate"]
    policy = lint_result["policy_checks"]
    merge_allowed = gate != "block"
    lint_snapshot = {
        "summary": lint_result["summary"],
        "policy_checks": policy,
    }

    if gate == "block":
        raw_ok, pre_errors = read_raw_files(files)
        for path, text in raw_ok:
            raw_filename = os.path.basename(path)
            record_ingest(
                raw_filename,
                None,
                "merge_blocked",
                file_checksum(text),
                os.path.getmtime(path),
                error_message="quality_gate=block; resolve broken_links before merge",
                skip_reason=None,
                operation="merge",
            )
        for err in pre_errors:
            rf = err.get("raw_file", "")
            record_ingest(
                rf,
                None,
                "merge_blocked",
                None,
                None,
                error_message=err.get("error", "unknown"),
                operation="merge",
            )
        return {
            "status": "blocked",
            "merge_allowed": False,
            "quality_gate": gate,
            "lint": lint_snapshot,
            "processed": [],
            "warnings": [
                "Merge blocked: quality_gate is block (e.g. unresolved broken_links).",
            ],
        }

    warnings: List[str] = []
    if gate == "warning":
        warnings.append(
            "quality_gate=warning: merge allowed; review remaining lint issues (orphan/duplicate/weak)."
        )

    rules = load_rules()
    raw_files, errors = read_raw_files(files)
    processed: List[Dict[str, Any]] = []
    merge_errors: List[Dict[str, str]] = []

    for err in errors:
        rf = err.get("raw_file", "")
        msg = err.get("error", "unknown")
        record_ingest(
            rf,
            None,
            "error",
            None,
            None,
            error_message=msg,
            operation="merge",
        )
        merge_errors.append({"raw_file": rf, "error": msg})

    for path, text in raw_files:
        raw_filename = os.path.basename(path)
        mtime = os.path.getmtime(path)
        checksum = file_checksum(text)

        last_ok = get_last_successful_record(raw_filename)
        existing_name: Optional[str] = None
        existing_content = ""
        if last_ok and last_ok.get("wiki_file"):
            existing_name = last_ok["wiki_file"]
            wp = os.path.join(WIKI_PATH, existing_name)
            if os.path.isfile(wp):
                existing_content = read_text_file(wp)

        if not existing_content.strip():
            cands = search_wiki_candidates(
                f"{raw_filename} {text[:500]}",
                top_k=QUERY_TOP_K,
            )
            if cands:
                cand = cands[0]["file"]
                wp = os.path.join(WIKI_PATH, cand)
                if os.path.isfile(wp):
                    existing_name = cand
                    existing_content = read_text_file(wp)

        try:
            prompt = build_merge_prompt(
                rules,
                raw_filename,
                text,
                existing_name,
                existing_content,
            )
            result = call_llm(prompt)
            title = extract_title(result, fallback=os.path.splitext(raw_filename)[0])
            if existing_name and os.path.isfile(os.path.join(WIKI_PATH, existing_name)):
                out_path = os.path.join(WIKI_PATH, existing_name)
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(result.strip() + "\n")
                wiki_basename = existing_name
            else:
                out_path = write_wiki(title, result)
                wiki_basename = os.path.basename(out_path)

            record_ingest(
                raw_filename,
                wiki_basename,
                "ok",
                checksum,
                mtime,
                error_message=None,
                skip_reason=None,
                operation="merge",
            )
            processed.append(
                {
                    "raw_file": raw_filename,
                    "wiki_file": wiki_basename,
                    "title": title,
                    "action": "merged",
                }
            )
        except Exception as e:
            record_ingest(
                raw_filename,
                None,
                "error",
                checksum,
                mtime,
                error_message=str(e),
                operation="merge",
            )
            merge_errors.append({"raw_file": raw_filename, "error": str(e)})

    err_n = len(merge_errors)
    proc_n = len(processed)
    if proc_n == 0:
        out_status = "error"
    elif err_n == 0:
        out_status = "ok"
    else:
        out_status = "partial"

    return {
        "status": out_status,
        "merge_allowed": True,
        "quality_gate": gate,
        "lint": lint_snapshot,
        "processed": processed,
        "errors": merge_errors,
        "warnings": warnings,
    }


def ingest(files: Optional[List[str]] = None, force: bool = False) -> Dict:
    os.makedirs(WIKI_PATH, exist_ok=True)
    init_db()

    rules = load_rules()
    raw_files, errors = read_raw_files(files)
    existing_context = load_existing_wiki_context()

    processed = []
    skipped: List[Dict[str, str]] = []

    for err in errors:
        rf = err.get("raw_file", "")
        msg = err.get("error", "unknown")
        record_ingest(
            rf,
            None,
            "error",
            None,
            None,
            error_message=msg,
        )

    for path, text in raw_files:
        raw_filename = os.path.basename(path)
        mtime = os.path.getmtime(path)
        checksum = file_checksum(text)
        last_ok = get_last_successful_record(raw_filename)
        if (
            not force
            and last_ok is not None
            and unchanged_since_last_success(last_ok, checksum)
        ):
            wiki_ref = last_ok.get("wiki_file")
            record_ingest(
                raw_filename,
                wiki_ref,
                "skipped",
                checksum,
                mtime,
                error_message=None,
                skip_reason="unchanged_checksum",
            )
            skipped.append(
                {
                    "raw_file": raw_filename,
                    "status": "skipped",
                    "reason": "unchanged_checksum",
                    "wiki_file": wiki_ref or "",
                }
            )
            continue
        try:
            prompt = build_ingest_prompt(rules, raw_filename, text, existing_context)
            result = call_llm(prompt)
            title = extract_title(result, fallback=os.path.splitext(raw_filename)[0])
            out_path = write_wiki(title, result)
            wiki_basename = os.path.basename(out_path)
            record_ingest(
                raw_filename,
                wiki_basename,
                "ok",
                checksum,
                mtime,
                error_message=None,
                skip_reason=None,
            )
            processed.append(
                {
                    "raw_file": raw_filename,
                    "wiki_file": wiki_basename,
                    "title": title,
                }
            )
        except Exception as e:
            record_ingest(
                raw_filename,
                None,
                "error",
                checksum,
                mtime,
                error_message=str(e),
                skip_reason=None,
            )
            errors.append({"raw_file": raw_filename, "error": str(e)})

    err_n = len(errors)
    proc_n = len(processed)
    skip_n = len(skipped)

    if err_n == 0:
        status = "ok"
    elif proc_n == 0 and skip_n == 0:
        status = "error"
    else:
        status = "partial"

    return {
        "status": status,
        "processed_count": proc_n,
        "skipped_count": skip_n,
        "error_count": err_n,
        "processed": processed,
        "skipped": skipped,
        "errors": errors,
    }


def query(question: str) -> Dict[str, Any]:
    wiki_files = list_wiki_files()
    if not wiki_files:
        return {
            "answer": "wiki 문서가 아직 없습니다. 먼저 ingest를 실행하세요.",
            "candidates": [],
        }

    candidates = search_wiki_candidates(question, top_k=QUERY_TOP_K)
    if not candidates:
        paths = sorted(
            wiki_files,
            key=lambda p: os.path.getmtime(p),
            reverse=True,
        )[:QUERY_TOP_K]
        candidates = [
            {"file": os.path.basename(p), "score": 0.0} for p in paths
        ]

    context_parts: List[str] = []
    total = 0
    for item in candidates:
        fname = item.get("file")
        if not fname:
            continue
        path = os.path.join(WIKI_PATH, fname)
        if not os.path.isfile(path):
            continue
        content = read_text_file(path)
        block = f"\n--- {fname} ---\n{content}\n"
        if total + len(block) > 50000:
            break
        context_parts.append(block)
        total += len(block)

    context = "\n".join(context_parts)
    if not context.strip():
        return {
            "answer": "선택된 위키 문서를 읽을 수 없습니다.",
            "candidates": candidates,
        }

    prompt = f"""
You are answering using only the internal wiki knowledge below.
If the answer is not grounded in the wiki, say what is missing.

WIKI:
{context}

Question:
{question}

Answer in Korean.
""".strip()

    answer = call_llm(prompt)
    return {"answer": answer, "candidates": candidates}


def lint() -> Dict[str, Any]:
    return run_lint()
