---
description: The format of a standalone task (Tasks/backlog/TASK-nnn_slug.md) or an epic child task (incomplete/EPIC-nnnA_slug.md). Copy it, fill every brace, delete this front matter and instructional comments.
---

# {task id} — {the outcome, not the activity}

<!-- TASK-nnn for a standalone task, EPIC-nnnA for an epic child. Choose one value for status, risk and size. Remove optional fields that do not apply. Done through .claude/skills/execute-task/SKILL.md. -->
**Status:** {🔵 Backlog / 🟡 In progress / ✅ Done (YYYY-MM-DD) / ❌ Cancelled (YYYY-MM-DD; reason)}
**Priority:** {optional, standalone only: P1 / P2 / P3}
**Board:** {standalone only: the one line Tasks/README.md shows — the outcome while open, the result once Done. An epic child has none: its epic README row is its board.}
**Source:** {who asked, when — the owner's words quoted once, then translated}
**Risk:** {🟢 / 🟡 / 🔴} — {what could go wrong, one line}
**Size:** {S / M / L} — {why, one line}
**Epic (optional):** {link to the parent epic README}
**Gate (optional):** {the project gate this task serves: Clarify / Discover / De-risk / Plan / Implement / Validate}
**Depends on:** {task or decision links and what must be ready, or None}

---

## 1. Context and problem
{The real situation with evidence: a link, a quoted source with the date checked, the owner's answer. Why now.}

## 2. Acceptance criteria
- [ ] {An observable outcome: a document section filled, a decision recorded, a number measured.}
- [ ] {A boundary or failure outcome; omit if not applicable.}

## 3. Approach
{How the task will be done and why; the options considered for any non-obvious choice. A choice that needs the owner (Constitution §2, Tier C) is listed here as waiting.}

## 4. Output
| File or place | Change |
| :--- | :--- |
| {path, or an outside place such as the YouTube channel, by name} | {what, and why} |

## 5. Verification
{Each acceptance criterion with how it is checked and the expected result. Record checks not yet done as Not done.}

## Notes (written when done)
{What was found, the decisions taken, the evidence for each criterion with its date, and the real delivery state.}

## Resume (optional; while unfinished)
{The last verified result, the unchecked criteria, any blocker and what releases it, and the next action. Remove once resolved.}
