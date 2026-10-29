---
description: Terms for the AI layer of Sagittarius RAG (governance, process, enforcement). Project terms are in Docs/VOCABULARY/README.md.
---

# AI glossary

Terms that matter to how the AI works on this project, kept out of the project documents on purpose: the people on the project do not need them (Constitution invariant 11).
Project terms (RAG, KB, gates, roles) are defined in `Docs/VOCABULARY/README.md`. Define a term once; add new AI-layer terms here in the same change.

| Term | Definition | Owner | Defined in | Not to be confused with |
| :--- | :--- | :--- | :--- | :--- |
| **`TODO → Discover phase` / `→ De-risk phase` / `→ Plan phase`** | A tag on a `TODO` meaning its answer belongs to that later phase and is not decided in the Clarify phase. An untagged `TODO` is decided in Clarify. The phase is always named in full; the reader is never left to guess. Rules: [Document rules](document-rules.md) §3. | — | [Clarify, "How to read"](../../Docs/Project-Management/Initiation-phase/Clarify/Clarify.md) | `Unknown — need to ask <who>`, which names a person to ask |
| **Triple constraint** | The three parts that shape every project: scope (what is delivered), schedule (when it ends) and resources (money, people, equipment, materials). Changing one usually changes the others. | Nathan Tran | [Framework §6](../skills/Project-Manager/framework.md) | the acceptance criteria, which say when the scope is met |
| **Project phases** (four) | Starting, organizing and preparing, carrying out the work, closing. Initiating, Planning, Executing / Monitoring and Controlling, and Closing in PMBOK 6. Mapped to the gates in Framework §6. | Nathan Tran | [Framework §6](../skills/Project-Manager/framework.md) | the six gates, which sit inside these phases |
| **Constitution** | The supreme rules: hats, autonomy tiers, rule precedence and invariants. Changes need the user's approval. | the user | [CONSTITUTION.md](../CONSTITUTION.md) | `CLAUDE.md`, which it outranks. The user's word: *"hiến pháp"* |
| **Invariant** | A numbered rule in the Constitution (§5) that every decision must satisfy. | the user | [CONSTITUTION.md](../CONSTITUTION.md) | a guideline |
| **Hat** | A role the AI picks for a task: Senior PM, Solution Architect, RAG/ML engineer, QA / KB editor. It says which hat it uses when that affects the answer. | — | Constitution §1 | a person |
| **Autonomy tier (A, B, C)** | A: decide alone. B: decide, record, inform. C: hard stop, ask with options (sending KB content out, choosing a provider or stack, setting `verified`, changing scope or acceptance criteria). | the user | Constitution §2 | priority |
| **Human gate** | A decision only a person may make (privacy approval, `verified` status, every Tier C item). Recorded in `Docs/README.md` §6. | Hai | Constitution invariant 8 | a review by the AI |
| **Fact / Assumption / Open question** | The three labels for a statement. Fact has a source; an assumption is temporary and has a way to validate it; an open question has a person who can answer. | — | Constitution invariant 1 | opinion |
| **`TODO` / `Unknown — need to ask <who>`** | How an unfilled item is written. Never a silent blank, never a guess. | — | `CLAUDE.md`, Clarify "How to read" | a placeholder with an invented value |
| **Source of truth** (one) | Each rule, spec or definition lives in one document; others link to it. A change of scope or acceptance criteria goes to Clarify, a change of method, gates or risks to Approach, a choice between alternatives to `Docs/Decisions/`. | — | Constitution invariant 2 | a copy |
| **Two-layer artifacts** | Documents for human readers (Clarify, Approach) and files for the AI (Constitution, `CLAUDE.md`, skills, decision records, which are imperative and checkable). | — | Constitution invariant 11 | — |
| **Seam / Variant** | A seam is the extension point built on the first case. A variant is a second implementation nobody has asked for yet: built only when a real case arrives. | — | Constitution invariant 6 | — |
| **Ratchet** | A quality bar that can only rise: never weaken the test set or the baseline. | — | Constitution invariant 7 | a target |
| **Guard** (`scripts/check_docs.py`) | A script that fails when a mechanical documentation rule is broken: IDs, traceability, phase tags, masked names, links, index and more. It enforces rules; it does not judge quality. | Nathan Tran | [Framework §5](../skills/Project-Manager/framework.md) | a unit test of behaviour |
| **Allowlist ratchet** | The list of known violations (`scripts/docs_check_allowlist.json`), each with a reason. The guard fails on any new violation and on any listed one that no longer occurs, so the list can only shrink. | Nathan Tran | `scripts/check_docs.py` | a permanent exemption list |
| **Skill** (`kb-authoring`, `kb-review`, `rag-eval`) | A packaged checklist the AI follows for one kind of task: writing KB files, reviewing them, evaluating retrieval. Invoking one binds the AI to its full checklist. | — | `CLAUDE.md` Skills | a tool or a script |
