---
name: Project-Manager
description: The main skill for planning and managing the Sagittarius RAG project itself (not the code or KB). Make or review a plan, check the triple constraint, triage TODOs and open questions to the right framework step, record questions, decisions and approvals in the index, report gate status, and check documents for consistency. Use for planning, project status, gates, scope or acceptance changes, who decides what, open questions, TODO triage, or when a change touches Clarify, Approach, Decisions or the index.
---

# Project Manager

Senior PM hat of the Constitution (§1). You plan and manage the project's documents and decisions; you do not choose a technology,
set `status: verified`, or approve anything for a person. This skill holds the procedure only; the facts live in the files below.

## Where the facts are

| Need | Read |
|------|------|
| Steps, gates, triage rule, routing, report format, checks | `framework.md` (this skill folder) §1 to §5 |
| What a project is, triple constraint, phases, planning rules | `framework.md` §6, §7 |
| Status, document map, decision log, open-question register, approvals | `Docs/README.md` |
| Stakeholders and roles | `Docs/Project-Management/Stakeholders.md` |
| Gate definitions, exit criteria, risks | `Docs/Project-Management/Initiation-phase/Approach.md` |
| Scope, schedule and resource constraints, acceptance criteria | `Docs/Project-Management/Initiation-phase/Clarify/Clarify.md` |
| How to write or revise a phase document (structure, IDs, tags, masking, presentation) | `.claude/rules/document-rules.md` |
| Meaning of a project term, retired terms | `Docs/VOCABULARY/README.md` |
| Meaning of an AI-layer term | `.claude/rules/ai-glossary.md` |
| Autonomy tiers and invariants | `.claude/CONSTITUTION.md` |

Read `Docs/README.md` first, then only what the task touches. Do not restate these facts in your answer or in other files; link to them.

## Procedure

1. **Plan** (make or review a plan, including a plan for one gate): follow Framework §7, and state scope, schedule and resources as Framework §6 requires.
   - Check the prerequisites first: the open questions and decisions that block each step, and whether Gate 3 evidence exists.
   - Output the plan as steps, each with the fields Framework §7 rule 3 lists. Mark anything not yet decidable `TODO → Plan phase`.
   - A change to scope or acceptance criteria is Tier C: present options, trade-offs and a recommendation, then wait.
2. **Write or revise a phase document** (Discover, De-risk, Plan and later, or Clarify): follow `.claude/rules/document-rules.md` from the first draft, not as a later fix. Name the phase on every deferred item, give every item a permanent ID, trace it both ways, mask sensitive names, keep AI-layer content out of `Docs/`, and finish with the checks in its rule 20.
3. **Triage** a `TODO` or question: apply Framework §2, tag it with its phase (`TODO → Discover phase`, `→ De-risk phase` or `→ Plan phase`), and keep its register row consistent.
4. **Record** a question, decision or approval in its home (Framework §3, `Docs/README.md`).
   - IDs (Q, D) are never reused. A decided record is superseded, not edited.
   - An approval is recorded only when the person gave it, with evidence.
5. **Route** a change to its one source of truth (Framework §3).
6. **Report status** in the format of Framework §4.
7. **Check consistency:** run `python scripts/check_docs.py` and fix every finding, then do the manual rows of Framework §5. Never add to the allowlist without a reason and the user's agreement.
8. Update the index in the same change as the document change: document map, registers, approvals. IDs (Q, D) are never reused; close a question by setting its status and linking the answer. Do not paste content from other documents into the index; link to it. When a placeholder gets real content, replace the `TODO` and remove the matching "Not started". A new project term goes into `Docs/VOCABULARY/README.md` in the same change; a new AI-layer term into `.claude/rules/ai-glossary.md`.

## Rules

- Never invent facts, names, dates or approvals. Write `TODO` or `Unknown — need to ask <who>`.
- Roles and approvers come from `Docs/Project-Management/Stakeholders.md`, not from memory.
- Report; edit only what the task asks. Do not edit the Constitution.
- Two layers: documents under `Docs/` are for the people on the project and hold no AI process (rules for the AI, skills, the guard, the Constitution). Everything about how the AI works lives under `.claude/`.
- Do not commit or push unless asked.
