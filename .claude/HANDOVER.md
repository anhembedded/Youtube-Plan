---
description: Handover for the next AI session on Sagittarius RAG. Read first when you continue earlier work: context, where the project stands, what to do next, the rules that bind, and the traps already met.
---

# Handover

Snapshot written on **2026-10-25**. It points to the sources instead of copying them, so it stays short. If a source disagrees with this page, the source wins. At the end of a session, update the "Where we are" and "Next" sections.

## 1. The project in one paragraph

Sagittarius RAG is a RAG tool for a team of an outsource company working for a client, over a knowledge base (KB) of `.md` files that an AI generated from the project's source code and nobody has verified. It also delivers a method that keeps the KB good input for the RAG, and an update path so other members can add, verify and update the KB. It is an internal **proposal project**: no budget, no deadline, a team of two (Nathan Tran, the sub-project lead, and Hai, the project lead who approves). The team has no RAG experience.
Start with [CLAUDE.md](../CLAUDE.md), then the index [Docs/README.md](../Docs/README.md). Background on the team and the client: [project-context.md](rules/project-context.md).

## 2. Where we are

| Item | State |
|------|-------|
| Phase | Clarify is drafted and waiting for Hai's approval (Gate 1). Discover (Gate 2) is set up but **not started** |
| Documents | [Clarify](../Docs/Project-Management/Initiation-phase/Clarify/Clarify.md) and [Approach](../Docs/Project-Management/Initiation-phase/Approach.md) are drafts. [Stakeholders](../Docs/Project-Management/Stakeholders.md), [Vocabulary](../Docs/VOCABULARY/README.md), the [Discover](../Docs/Project-Management/Discover/Discover.md) files and [tracking](../Docs/Project-Management/Discover/tracking.md) exist |
| Discover | Skeleton with items DS01 to DS50, a first solution landscape (SL01 to SL23, traps TR01 to TR18, sources SRC01 to SRC29) written from public sources. Every Finding is empty, every status is Not started |
| Open questions | 23 of 24 are open ([register](../Docs/README.md#5-open-questions-register)). Only **Q02 is answered** |
| Guard | `python scripts/check_docs.py` reports 0 new findings, 3 known exceptions |
| Git | Last commit `5d47958`. The Discover split, the solution landscape, tracking and the guard changes are **not committed** |

Facts settled by the owner, so do not reopen them: a RAG is the chosen solution (approved by Hai); KB content **may not go to external services**, only local models or the enterprise LLM already in use (Q02); the client provides Copilot 365 and Copilot in VS Code, and Claude may be approved (Q23, unconfirmed); the RAG runs on a Windows client remote PC where installs need a grant; the team owns the KB, not the client; v1 handles `.md` only.

## 3. What to do next

1. **Do not start Discover by reading the KB with an AI assistant.** Until Q23 and the policy are answered, KB content must not reach any AI service, including you (TR18). Work from descriptions, counts the user gives, and invented samples.
2. **Help the user get Gate 1 passed.** Hai must approve Clarify and Approach and answer the Gate 1 questions: Q03, Q06, Q07, Q11, Q15, Q16, Q19, Q20, and confirm G4. The plan with the message to Hai is in the previous session's notes; the content is in the register. Record an approval only when the user says Hai gave it.
3. **Start Discover with the RAG orientation** ([rag-and-flow.md](../Docs/Project-Management/Discover/rag-and-flow.md)) and, in parallel, send the questions only others can answer: Q01, Q12, Q13, Q22, Q23, Q24. Update [tracking.md](../Docs/Project-Management/Discover/tracking.md) as items change (Waiting once a question is sent).
4. Verify the solution landscape against **official** pages for every shortlisted row; most sources now are vendor blogs.
5. Commit when the user asks. Do not push.

## 4. Rules that bind

- **Two layers.** `Docs/` is for the people on the project and holds no AI process. How the AI works lives in `.claude/`. The guard enforces it.
- **Read before writing any document:** [document-rules.md](rules/document-rules.md). Key points: permanent IDs with the prefix table, trace both ways, name the phase on every deferred item (`TODO → Discover phase`, `→ De-risk phase`, `→ Plan phase`), no SMART table, tables of at most five columns, mask sensitive names, At a glance at the top and a Next step at the end of each phase document.
- **Procedure and facts for managing the project:** the `Project-Manager` skill and its [framework.md](skills/Project-Manager/framework.md). Use it for plans, triage, status, approvals and consistency.
- **Autonomy:** [CONSTITUTION.md](CONSTITUTION.md). Choosing a provider or stack, sending KB content out, changing scope or acceptance criteria, and setting `verified` are the user's decisions. Present options and a recommendation, then wait.
- **Never invent** facts, names, dates or approvals. Write `TODO` with its phase, or `Unknown`.
- **Naming.** The client app name is masked (use the mask in the documents). Never write the real client, application, site or data-field names, or real paths, in any document.
- **Terms.** Project terms live in the project vocabulary, AI-layer terms in [ai-glossary.md](rules/ai-glossary.md). "Sponsor" and "project owner" are retired: the role is Hai.

## 5. How the user works

- Writes in Vietnamese, without diacritics at times. Answer in Vietnamese; documents are in English.
- When the user says "chỉ trả lời, không code" or asks for an opinion, **answer only and change nothing**. Ask before restructuring.
- Prefers short, concrete answers with a table where it helps, a stated conclusion first, and an honest account of gaps and mistakes.
- Edits the documents directly while you work. **Read a file again before editing it** if the tool says it changed on disk.
- Pushes back on content that sits at the wrong level (for example Discover detail inside the charter) and on terms used loosely. Check where a thing belongs before adding it.

## 6. Traps already met

- **The shell and editing.** Windows with Git Bash and PowerShell. Several files use CRLF line endings; read and write them in a way that keeps them. In a Python heredoc a string like `"\b"` becomes a backspace character; use the edit tool or raw strings for regular expressions.
- **Guard exit status.** Piping the guard into `tail` hides its exit code. Check for `FAIL` lines, not the pipe's status. A commit was once made over a failing guard this way.
- **Tables.** Row insertion by search strings is fragile; confirm the anchor is unique, and do not search for `---` inside a table separator.
- **Do not quote** the failure statistics in the vendor articles ("80%", "40 to 60%", "60%"): no original source was found.
- **Gate versus phase.** A phase is a stretch of work; a gate is the checkpoint at its end. The documents name a gate and its phase together on purpose.

## 7. Loose ends

- The guard's allowlist has 3 exceptions: wide registers (acceptance criteria, decision log, question register) are over five columns. They are recorded with reasons in `scripts/docs_check_allowlist.json`.
- The Constitution and Approach were updated once to replace "sponsor" with the project lead, with the user's approval.
- A3 (the "update daily" idea) is kept as an assumption; the real choice is decision D06.
- G4 (define the verification process, the team does the verifying) is agreed in principle; Hai still has to confirm.
- No decision records exist yet in `Docs/Decisions/`. The planned ones are D01 to D07 in the decision log.
