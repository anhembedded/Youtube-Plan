---
description: The format of a decision record (ADR, Nygard 2011) — Docs/Decisions/D-nnn_slug.md for a project-wide choice or an epic's decisions/D-nnn_slug.md. One global D-nnn sequence, every record in the decision log of Docs/README.md §4. Copy it, fill every brace, delete this front matter.
---

# D-{nnn} — {the decision as one sentence}

<!-- Choose one status. A decided record is never edited: a change of mind is a new record that supersedes it. Remove optional fields and instructional comments when copying. -->
**Scope:** {Project, or EPIC-nnn linked to its README}
**Date:** {YYYY-MM-DD}
**Status:** {Proposed / Accepted / Rejected / Superseded}
**Decided by:** {Pending, or the owner (quoted once, then translated), or the assistant under Constitution §2 Tier B}
**Supersedes / superseded by (optional):** {link to the other record}
**Answers (optional):** {Q-nnn, G…}

| Label | Meaning |
| :--- | :--- |
| ✅ Fact | confirmed from a named source, with the date checked |
| 🔵 Proposed | an option awaiting a decision |
| 🟢 Owner decision | decided by the owner; quoted, then translated |
| 🤖 Assistant decision | Tier B: inside approved scope, decided and recorded by the assistant, reported to the owner |
| ❓ Open | blocks the named phase until answered |

## 1. Context
{The forces: the problem, the constraints (C…), the evidence, what was tried.}

## 2. Options
| Option | Benefit | Cost and risk | Evidence |
| :--- | :--- | :--- | :--- |
| {A} | {…} | {…} | {source and date} |
| {B} | {…} | {…} | {…} |

## 3. Decision
{The option chosen, why its trade-offs fit, and what it commits the project to (scope, schedule, resources).}

## 3a. Constitution check (assistant decisions only)
<!-- Required when Decided by is the assistant; delete otherwise. Any ❌ means the decision goes to the owner. -->
| Invariant (`.claude/CONSTITUTION.md` §5) | Passes? | Evidence |
| :--- | :--- | :--- |
| 1 Evidence over assertion | {✅ / ❌} | {…} |
| 2 One source of truth | {✅ / ❌} | {…} |
| 6 Smallest end-to-end first | {✅ / ❌} | {…} |
| 8 Human gates never bypassed (not Tier C) | {✅ / ❌} | {…} |
| 12 Remake, never copy | {✅ / ❌ / not touched, because …} | {…} |
| Reversible; no money, account, publishing or third-party material | {✅ / ❌} | {how it is undone} |

## 4. Consequences
{What changes, which one document is updated (Clarify, Approach, Plan or an epic), and what is now harder.}

## 5. Open questions
| ID | Question | Blocks | Asked on |
| :--- | :--- | :--- | :--- |
| Q-{nnn} | {…, also in Docs/README.md §5} | {phase} | {date} |
