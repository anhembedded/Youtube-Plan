---
description: Rules the AI follows when writing or revising project documents under Docs/. Agent-facing; the project documents themselves do not contain them.
---

# Document rules — how project documents are written

Apply these rules when writing or revising any project document (Clarify, Discover, De-risk, Plan and later phases), so each one is right from the first draft.
They come from the review of [Clarify](../../Docs/Project-Management/Initiation-phase/Clarify/Clarify.md). Phases and gates are in [Framework](../skills/Project-Manager/framework.md); terms are in [Vocabulary](../../Docs/VOCABULARY/README.md).
A reader must not need the context of the conversation to understand a document: say it in the document.

## 1. Structure and level

0. **Two layers.** Documents under `Docs/` are for the people on the project: they describe the project, never how the AI works. Rules for the AI, skills, the guard, the Constitution and AI-only terms live under `.claude/`. The guard fails on AI-layer words in `Docs/`. Background written for the AI, such as the project context, lives in `.claude/rules/project-context.md`.

1. **Lead with the conclusion.** Put an "At a glance" block at the top: problem, objective, what is not done, limits, done when, waiting for, next. The summary the framework asks for at the end of a phase goes at the top, not the bottom.
2. **One level of abstraction per document.** A charter states why, what, scope, constraints and done. It does not hold candidate solutions, design, worked examples or survey data.
3. **Move detail out and leave a link.** Examples go to their own file, survey data to the Discover document, candidate solutions to a decision record (`Docs/Decisions/`). Leave a one- or two-line summary and a link where the content was.
4. **End with the next phase.** Every document says what comes next and who must approve.

## 2. Items and traceability

5. **Every item has a permanent ID,** never reused or renumbered. Prefixes are unique:

| Prefix | Item | Home |
|--------|------|------|
| P | Pain | Clarify §1.2 |
| O | Objective | Clarify §2.2 |
| DL | Deliverable | Clarify §3 |
| G | Grey area | Clarify §4 |
| C | Constraint | Clarify §5.1 |
| A | Assumption | Clarify §5.2 |
| AC | Acceptance criterion | Clarify §6.1 |
| R | Risk | Approach §7 |
| SH | Stakeholder | Stakeholders |
| DS | Discover item | Discover files |
| SL | Solution candidate | Discover, solution landscape |
| TR | Trap (a way the project fails) | Discover, solution landscape |
| SRC | Source | Discover, solution landscape |
| Q | Open question | [Docs/README.md](../../Docs/README.md) §5 |
| D | Decision | [Docs/README.md](../../Docs/README.md) §4 and `Docs/Decisions/` |

   Add a prefix here before using a new one. Check that it collides with none (DL was chosen because D means decision).
6. **Trace both ways.** Pain to objective to deliverable to acceptance criterion; a constraint lists what it affects, and the question or decision names the constraint back. Report a pain that nothing addresses as "not addressed", not as covered.
7. **An item with no link is suspect.** An objective that cites no pain, a constraint that affects nothing, or a deliverable that serves no objective is removed or explained.

## 3. Honesty about what is known

8. **Label every statement** as a Fact (with its source, e.g. "from the owner"), an Assumption (with a way to validate it) or an Open question (with a person who can answer).
9. **Name the phase of every deferred item.** Write `TODO → Discover phase`, `TODO → De-risk phase` or `TODO → Plan phase`, and both when needed (`TODO → Discover phase, then De-risk phase`). Say what is to be found out. An untagged `TODO` is decided in Clarify by Hai or the client. Do not leave the phase for the reader to guess.
10. **Every tagged item is picked up** in the document of its phase (for Discover, [Discover](../../Docs/Project-Management/Discover/Discover.md)) and, if it is a question, in the register.
11. **Targets are examples until confirmed.** Mark them `e.g.` and tag the phase that sets them. Do not invent numbers or dates. If a deadline or budget does not exist, say so and cite where it is recorded.
12. **A requirement states an outcome, not a solution.** Candidate solutions are options in a decision record, not part of an objective.

## 4. Presentation

13. **No SMART table.** State each objective as an outcome with a measure and a target, plus what it addresses and depends on. Do not force Specific, Measurable, Achievable, Relevant and Time-bound columns.
14. **Tables have at most five columns.** Prose that makes a cell long goes below the table. Registers (acceptance criteria, decision log, open-question register) may be wider because each column is a traced field; they are recorded in the guard's allowlist with the reason.
15. **One name per thing.** Use the spelling in Vocabulary, and define a new term there in the same change. Do not use a term listed as retired.
16. **Mask sensitive names.** Names of the client, the application, sites, data fields and real paths are written as placeholders (`<app>`, `Site A`, `Field 1`) or the masks in Vocabulary. This includes example questions and file paths. Never put a real name in a document.
17. **Write for a reader without the context.** Define a term at first use or link it, avoid shorthand that only the team knows, and use the same words as the headings.

## 5. Keeping documents consistent

18. **One source of truth.** A rule, spec or definition lives in one place; others link ([Framework §3](../skills/Project-Manager/framework.md)).
19. **Update the index in the same change** ([Docs/README.md](../../Docs/README.md)): document map, registers, approvals.
20. **Check before finishing:** run `python scripts/check_docs.py` and fix every finding (links, IDs, traceability, phase tags, masked names and more; see [Framework §5](../skills/Project-Manager/framework.md)). Do the checks the script cannot do by reading. A new exception goes in the allowlist with a reason, never silently.
