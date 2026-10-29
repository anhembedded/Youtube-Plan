---
description: The format of an epic's README.md under Tasks/epics/EPIC-nnn_slug/ (.claude/skills/create-epic/SKILL.md). Copy it, fill every brace, delete this front matter.
---

# EPIC-{nnn} — {the outcome}

<!-- Choose one status. Remove optional fields and instructional comments when copying. -->
- **Status:** {🔵 Planned / 🟡 Phase n in progress / ✅ Done (YYYY-MM-DD) / ❌ Cancelled (YYYY-MM-DD; reason)}
- **Origin:** {PRO-nnn, the Plan document, or the owner's words quoted once and translated}
- **North star:** {the project document under `Docs/` this epic delivers, or its `charter/README.md`; the epic summarises it and does not repeat it}
- **Phases:** {one entry per optional phase, written or skipped with the reason (create-epic §4), e.g. `Charter: skipped — project Clarify covers it · Discover: written · De-risk: skipped — no costly assumption`}
- **Tracking:** the epic's `TRACKING.md` (required; its Gantt is refreshed whenever a child changes state)
- **Decisions (optional):** {decisions/D-{nnn}_{slug}.md — one line per record}
- **Dependencies:** {other epic or task links and prerequisites, or None}

---

## 1. Decisions already made
{Numbered, one line each, pointing at the decision record.}

## 2. Goals — measurable
| Metric | Today (measured {date}) | When the epic is done |
| :--- | :-: | :-: |
| {…} | {…} | {e.g. target, until the owner confirms it} |

## 3. Child tasks, ordered by risk
<!-- This table is the epic's Kanban: it is rendered in chat before any child starts or resumes. Refresh each status from evidence. -->
| Id | Task | Depends on | Risk | Status |
| :--- | :--- | :--- | :-: | :--- |
| {EPIC-nnnA, linked to its task file} | {…} | {task ids or None} | {🟢 / 🟡 / 🔴} | {Planned / In progress / Done / Cancelled} |

## 4. Phase exit criteria
| Phase | Required outcome | Evidence required to close |
| :--- | :--- | :--- |
| {phase} | {observable result and target, linked to the goals above} | {document, measurement or the owner's check; Not done until verified} |

## 5. Out of scope
{What this epic deliberately does not do, and where that lives instead.}

## Notes (newest first)
- **{YYYY-MM-DD}** — {what changed and why, one line; the pull request}
