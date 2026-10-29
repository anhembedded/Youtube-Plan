---
description: Terms for the AI layer of the YouTube Plan project (governance, process, enforcement). Project terms are in Docs/VOCABULARY/README.md.
---

# AI glossary

Terms that matter to how the AI works on this project, kept out of the project documents on purpose: the people on the project do not need them (Constitution invariant 11).
Project terms (niche, gates, roles, YouTube metrics) are defined in [Vocabulary](../../Docs/VOCABULARY/README.md). Define a term once; add new AI-layer terms here in the same change.

| Term | Definition | Owner | Defined in | Not to be confused with |
| :--- | :--- | :--- | :--- | :--- |
| **`TODO → Discover phase` / `→ De-risk phase` / `→ Plan phase`** | A tag on a `TODO` meaning its answer belongs to that later phase and is not decided in the Clarify phase. An untagged `TODO` is decided in Clarify. The phase is always named in full; the reader is never left to guess. Rules: [Document rules](document-rules.md) §3. | — | [Document rules](document-rules.md) §3 | `Unknown — need to ask <who>`, which names a person to ask |
| **Triple constraint** | The three parts that shape every project: scope (what is delivered), schedule (when it ends) and resources (money, people, equipment, materials). Changing one usually changes the others. | the owner | [Framework §6](../skills/Project-Manager/framework.md) | the acceptance criteria, which say when the scope is met |
| **Project phases** (four) | Starting, organizing and preparing, carrying out the work, closing. Initiating, Planning, Executing / Monitoring and Controlling, and Closing in PMBOK 6. Mapped to the gates in Framework §6. | the owner | [Framework §6](../skills/Project-Manager/framework.md) | the six gates, which sit inside these phases |
| **Constitution** | The supreme rules: hats, autonomy tiers, rule precedence and invariants. Changes need the user's approval. | the user | [CONSTITUTION.md](../CONSTITUTION.md) | `CLAUDE.md`, which it outranks. The user's word: *"hiến pháp"* |
| **Invariant** | A numbered rule in the Constitution (§5) that every decision must satisfy. | the user | [CONSTITUTION.md](../CONSTITUTION.md) | a guideline |
| **Hat** | A role the AI picks for a task: Senior PM, Channel Strategist, Producer, QA / Policy reviewer. It says which hat it uses when that affects the answer. | — | Constitution §1 | a person |
| **Autonomy tier (A, B, C)** | A: decide alone. B: decide, record, inform. C: hard stop, ask with options (spending money, choosing a tool or provider, publishing, using third-party material, changing scope or acceptance criteria). | the user | Constitution §2 | priority |
| **Human gate** | A decision only the owners may make (every Tier C item), with both approvals: the owner's and the partner's. Recorded in the approvals table of `Docs/README.md` §3. | the owners | Constitution invariant 8 | a review by the AI |
| **Fact / Assumption / Open question** | The three labels for a statement. Fact has a source; an assumption is temporary and has a way to validate it; an open question has a person who can answer. | — | Constitution invariant 1 | opinion |
| **`TODO` / `Unknown — need to ask <who>`** | How an unfilled item is written. Never a silent blank, never a guess. | — | [Document rules](document-rules.md) §3 | a placeholder with an invented value |
| **Source of truth** (one) | Each rule, spec or definition lives in one document; others link to it. A change of scope or acceptance criteria goes to Clarify, a change of method, gates or risks to Approach, a choice between alternatives to `Docs/Decisions/`. | — | Constitution invariant 2 | a copy |
| **Two-layer artifacts** | Documents for human readers (Clarify, Approach and later phases) and files for the AI (Constitution, `CLAUDE.md`, skills, rules, which are imperative and checkable). | — | Constitution invariant 11 | — |
| **Seam / Variant** | A seam is the extension point built on the first case (e.g. a script template that a second language could reuse). A variant is a second implementation nobody has asked for yet: built only when a real case arrives. | — | Constitution invariant 6 | — |
| **Ratchet** | A quality bar that can only rise: never lower the acceptance criteria or the quality checklist without the owner's approval. | — | Constitution invariant 7 | a target |
| **Remake, never copy** | A source story is used only as an idea; script, voice and visuals are original, and the source is recorded. | the owner | Constitution invariant 12 | translating or re-uploading a source video |
| **Skill** (`Project-Manager`, `create-epic`, `execute-task`, `create-skill`) | A packaged checklist the AI follows for one kind of task. Invoking one binds the AI to its full checklist. | — | `.claude/skills/<name>/SKILL.md` | a tool or a script |
