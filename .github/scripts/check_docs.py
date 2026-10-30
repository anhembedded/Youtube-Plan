#!/usr/bin/env python3
"""Mechanical checks for the project documents (Docs/, Tasks/, .claude/).

Enforces the rules that can be checked without judgement: links and anchors,
IDs cited but never defined, the assumption log and the source register,
the document map and the board, project documents free of AI-process words,
and no secrets. Exit code 1 lists every finding; 0 means all checks passed.
Rules: .claude/rules/document-rules.md; checks: .claude/skills/Project-Manager/framework.md §5.

Usage: python3 .github/scripts/check_docs.py [--extract-mermaid DIR]
"""
import argparse
import glob
import os
import re
import sys
import urllib.parse

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
INDEX = "Docs/README.md"
CLARIFY = "Docs/Project-Management/Initiation-phase/Clarify/Clarify.md"
APPROACH = "Docs/Project-Management/Initiation-phase/Approach.md"
BOARD = "Tasks/README.md"
FENCE = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")

findings = []


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def md_files(*patterns):
    out = []
    for p in patterns:
        out += [os.path.relpath(f, ROOT) for f in glob.glob(os.path.join(ROOT, p), recursive=True)]
    return sorted(set(out))


def fail(path, message):
    findings.append(f"{path}: {message}")


def table_ids(text, pattern):
    """IDs defined as the first cell of a table row."""
    return set(re.findall(r"^\|\s*(" + pattern + r")\s*\|", text, re.M))


def anchors(path):
    text = FENCE.sub("", read(path))
    out = set()
    for heading in re.findall(r"^#+\s+(.*?)\s*$", text, re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")
        out.add(slug)
    return out


def check_links(files):
    for f in files:
        text = FENCE.sub("", read(f))
        for target, anchor in re.findall(r"\]\(([^)#\s]*)(#[^)\s]*)?\)", text):
            if target.startswith(("http://", "https://", "mailto:")) or "{" in target:
                continue
            dest = os.path.normpath(os.path.join(os.path.dirname(f), urllib.parse.unquote(target))) if target else f
            if not os.path.exists(os.path.join(ROOT, dest)):
                fail(f, f"broken link -> {target}")
            elif anchor and dest.endswith(".md") and anchor[1:] not in anchors(dest):
                fail(f, f"broken anchor -> {target}{anchor}")


def check_project_ids(project_files):
    """Clarify, risk, question, decision and source IDs cited must be defined in their home."""
    clarify = read(CLARIFY) if os.path.exists(os.path.join(ROOT, CLARIFY)) else ""
    index = read(INDEX) if os.path.exists(os.path.join(ROOT, INDEX)) else ""
    approach = read(APPROACH) if os.path.exists(os.path.join(ROOT, APPROACH)) else ""
    homes = {
        "Clarify": (table_ids(clarify, r"(?:P|O|DL|G|C|A|AC)\d+"), r"(?<![\w-])((?:P|O|DL|G|C|A|AC)\d+)(?![\w-])"),
        "Approach §7": (table_ids(approach, r"R-\d+"), r"(?<![\w-])(R-\d+)(?![\w-])"),
        "the question register": (table_ids(index, r"Q-\d{3}"), r"(?<![\w-])(Q-\d{3})(?![\w-])"),
        "the decision log": (table_ids(index, r"D-\d{3}"), r"(?<![\w-])(D-\d{3})(?![\w-])"),
        "the source register": (table_ids(index, r"SRC-\d+"), r"(?<![\w-])(SRC-\d+)(?![\w-])"),
    }
    for f in project_files:
        # IDs of an epic's own documents are cited with the epic ("EPIC-002 AC1"); skip those.
        text = re.sub(r"EPIC-\d{3}[A-Z]?\d*\s+(?:[A-Z]+-?\d+)", "", FENCE.sub("", read(f)))
        for home, (defined, pattern) in homes.items():
            for cited in sorted(set(re.findall(pattern, text)) - defined):
                fail(f, f"{cited} is cited but not defined in {home}")


def check_assumption_log():
    if not os.path.exists(os.path.join(ROOT, INDEX)):
        return
    log = read(INDEX).split("## 6. Assumption log", 1)
    logged = table_ids(log[1], r"(?:EPIC-\d{3}\s+)?A\d+") if len(log) == 2 else set()
    raised = set()
    for f in md_files("Docs/Project-Management/**/*.md"):
        section = re.search(r"### 5\.2 Assumptions(.*?)(?:\n## |\Z)", read(f), re.S)
        if section:
            raised |= table_ids(section.group(1), r"A\d+")
    for a in sorted(raised - logged):
        fail(INDEX, f"assumption {a} is missing from the assumption log (§6)")
    for a in sorted(logged - raised):
        fail(INDEX, f"assumption log row {a} has no assumption in a project document")


def check_maps():
    index = read(INDEX)
    for f in md_files("Docs/Project-Management/**/*.md", "Docs/Decisions/**/*.md", "Docs/VOCABULARY/*.md"):
        rel = os.path.relpath(f, "Docs").replace(" ", "%20")
        if f"({rel})" not in index and f"({rel}#" not in index:
            fail(INDEX, f"document map or decision log does not link {f}")
    board = read(BOARD)
    for epic in sorted(glob.glob(os.path.join(ROOT, "Tasks/epics/EPIC-*/README.md"))):
        rel = os.path.relpath(epic, os.path.join(ROOT, "Tasks"))
        if f"({rel})" not in board:
            fail(BOARD, f"board does not list {os.path.relpath(epic, ROOT)}")
    for pro in sorted(glob.glob(os.path.join(ROOT, "Tasks/proposal/PRO-*.md")) + glob.glob(os.path.join(ROOT, "Tasks/backlog/TASK-*.md"))):
        rel = os.path.relpath(pro, os.path.join(ROOT, "Tasks"))
        if f"({rel})" not in board:
            fail(BOARD, f"board does not list {os.path.relpath(pro, ROOT)}")


AI_WORDS = re.compile(r"\b(constitution|tier [abc]|skills?|hats?|invariant)\b", re.I)

# Known exceptions, each with its reason. This list may only shrink: a listed file
# that no longer needs its exception is itself a finding.
TWO_LAYER_ALLOWLIST = {
    "Tasks/proposal/PRO-001.md": "its subject is the repository's own process, including the AI rules folder; kept as accepted history",
}


def check_two_layers(project_files):
    for f in TWO_LAYER_ALLOWLIST:
        if f in project_files and not AI_WORDS.search(INLINE_CODE.sub("", FENCE.sub("", read(f)))):
            fail(f, "no longer needs its two-layer allowlist entry; remove it")
    for f in project_files:
        if f in TWO_LAYER_ALLOWLIST:
            continue
        text = INLINE_CODE.sub("", FENCE.sub("", read(f)))
        for n, line in enumerate(text.splitlines(), 1):
            m = AI_WORDS.search(line)
            if m:
                fail(f, f"line {n}: AI-process word '{m.group(0)}' in a project document")


SECRETS = re.compile(r"[\w.+-]+@[A-Za-z][\w-]*(?:\.[\w-]+)*\.[A-Za-z]{2,}\b|\b(?:sk|ghp|gho|xox[abp])[-_][A-Za-z0-9]{16,}|AKIA[0-9A-Z]{16}")


def check_secrets(files):
    for f in files:
        for n, line in enumerate(read(f).splitlines(), 1):
            m = SECRETS.search(line)
            if m and not m.group(0).endswith("@anthropic.com"):
                fail(f, f"line {n}: looks like personal data or a secret: {m.group(0)[:12]}…")


def extract_mermaid(files, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    count = 0
    for f in files:
        for i, block in enumerate(re.findall(r"```mermaid\n(.*?)```", read(f), re.S)):
            name = re.sub(r"[^\w]+", "_", f) + f"_{i}.mmd"
            with open(os.path.join(out_dir, name), "w", encoding="utf-8") as out:
                out.write(block)
            count += 1
    print(f"extracted {count} Mermaid blocks to {out_dir}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--extract-mermaid", metavar="DIR", help="also write every Mermaid block to DIR for rendering")
    args = parser.parse_args()

    all_md = md_files("Docs/**/*.md", "Tasks/**/*.md", ".claude/**/*.md", "*.md")
    # Project documents: written for people; the method notes in Project-Process are generic reference.
    project = [f for f in md_files("Docs/**/*.md", "Tasks/**/*.md") if not f.startswith("Docs/Project-Process/")]

    check_links(all_md)
    check_project_ids([f for f in project if not f.startswith("Tasks/proposal/")])
    check_assumption_log()
    check_maps()
    check_two_layers(project)
    check_secrets(all_md)
    if args.extract_mermaid:
        extract_mermaid(all_md, args.extract_mermaid)

    if findings:
        print(f"FAILED: {len(findings)} finding(s)")
        for line in findings:
            print("  " + line)
        return 1
    print(f"OK: {len(all_md)} Markdown files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
