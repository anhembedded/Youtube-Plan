# Project Framework — how this project is run

The steps the project follows and the rules for moving work between them. It applies the owner's project-management framework
(Clarify, Discover, De-risk, Plan, Implement, Validate) to the YouTube Plan project. Gate definitions and exit criteria will live in
`Docs/Project-Management/Initiation-phase/Approach.md` (not written yet); this file adds only the mapping and the working rules.
Terms are defined in `Docs/VOCABULARY/README.md`. Status, registers and approvals are in `Docs/README.md` (both not written yet).

Source of the framework: [Docs/Project-Process](../../../Docs/Project-Process/Thinking%20New%20project.md).

## 1. Steps and gates

| Gate | Step | Question it answers | Who or what answers it | Evidence of passing |
|------|------|---------------------|------------------------|---------------------|
| 1 | Clarify | Why, what, scope, constraints, done? | The owner | Approach §5, Gate 1 |
| 2 | Discover | What is true out there? | Research: YouTube policies, competitor channels, niche and language data, tool prices, the owner's real time | Approach §5, Gate 2 |
| 3 | De-risk | Which assumption could sink the project, and does it hold? | A time-boxed spike, e.g. a pilot video from story to upload | Approach §5, Gate 3 |
| 4 | Plan | Who does what, in what order? | The owner, from Gate 3 evidence | Approach §5, Gate 4 |
| 5 | Implement | Does each increment work? | Measurement against the quality checklist and channel analytics | Approach §5, Gate 5 |
| 6 | Validate | Did we meet the acceptance criteria? | Results against Clarify §6 | Approach §5, Gate 6 |

A gate is passed only when its exit criterion is met and the evidence is linked in the index. Merged work does not pass a gate.

## 2. Triage a `TODO` or an open question

Ask where the answer comes from.

| The answer is in... | Phase | Tag |
|---------------------|------|-----|
| a person with authority (the owner) | Clarify | none |
| research or a measurement: policies, competitor channels, market data, tool prices | Discover | `TODO → Discover phase` |
| something that must be tried to know (e.g. make a pilot video) | De-risk | `TODO → De-risk phase` |
| ownership, order, effort | Plan | `TODO → Plan phase` |

- An untagged `TODO` is decided at Clarify. A tagged one is not decided there.
- A question in the register (`Docs/README.md` §5) is listed under the gate where it is needed, and agrees with the tag in the document.
- If a tagged item is something the owner could simply answer now (budget, hours per week), untag it and ask.

## 3. Where a change goes

Each rule, spec or definition lives in one place (Constitution invariant 2).

| Change in... | Update |
|--------------|--------|
| scope, constraints, acceptance criteria, stakeholders | `Docs/Project-Management/Initiation-phase/Clarify/Clarify.md` |
| method, gates, risks | `Docs/Project-Management/Initiation-phase/Approach.md` |
| a choice between alternatives | `Docs/Decisions/` (from `_template.md`) |
| a word or its meaning | `Docs/VOCABULARY/README.md` |
| status, registers, approvals | `Docs/README.md` |

Changing scope or acceptance criteria, spending money, choosing a tool or provider, publishing, and using third-party material are
Tier C (Constitution §2): they need the owner's approval, recorded in the approvals table.

## 4. Status report

Lead with the conclusion. Then, as a table:

| Item | Content |
|------|---------|
| Where we are | Current gate and step |
| Blocking | Open questions that stop the next gate, and who can answer each |
| Done since the last report | Questions closed, decisions made, approvals given |
| Risks | New or changed, from Approach §7 |
| Next | The next step and who must act |

State uncertainty early. Give dates only where one exists; see the constraints in Clarify §5.1.

## 5. Consistency checks

Do these by reading. Report each finding as a table row (location, issue, fix).

| Check | Looks for |
|-------|-----------|
| Single source | A rule, spec or definition copied into a second document |
| Retired terms | Any term listed in Vocabulary §4 still in use |
| Vocabulary | A term used in documents but missing from Vocabulary |
| Tags | An untagged `TODO` that cannot be decided at Clarify; a tagged one that can be answered now |
| Labels | A statement that is not a Fact (with source), an Assumption (with a way to validate) or an Open question (with an owner) |
| Index drift | A document missing from the map, a decision missing from the log, a register row that disagrees with its source |
| Traceability | A pain (P#) with no objective, constraint or gate addressing it and not marked "not addressed"; an objective (O#) that cites no pain; a deliverable (DL#) that serves no objective; a constraint (C#) whose "Affects" cell is empty or cites an ID that does not exist; a Q or D whose link to a C# does not agree in both directions |
| Document rules | A rule in [Document rules](../../rules/document-rules.md) broken: no At a glance block, a tag without its phase, a SMART table, a table wider than five columns, a secret or personal data, an ID prefix that collides |
| Links | A link to a file or heading that does not exist |
| Triple constraint | A plan or scope change that does not state its effect on scope, schedule and resources (§6) |
| End condition | A gate or step with neither a time-box nor a stop rule (§6) |

## 6. What a project is, and the triple constraint

A project is work with a clear goal, a clear end and limited resources. Three parts shape it (the triple constraint):

| Part | Question | Where it is stated for this project |
|------|----------|-------------------------------------|
| Scope | What will the project deliver? | Clarify §3, §4 |
| Schedule | When will it be finished? | Clarify §5.1 (constraints) |
| Resources | What is needed: money, people, equipment, tools? | Clarify §5.1, Stakeholders |

Rules:
1. **Change one, review the others.** A change to scope, schedule or resources states its effect on the other two. A change of scope or acceptance criteria is Tier C.
2. **Every plan states all three.** If a part does not exist, say so and cite where that is recorded; do not leave it blank.
3. **The end tells whether the project succeeded.** If there is no end date, success is measured by the acceptance criteria (Clarify §6) and gate evidence. Without a date there is a risk of never finishing, so every gate and spike needs a time-box or an explicit stop rule.
4. **Resources limit the product.** Fit the scope to the resources; do not plan the scope first and hope the resources appear. Resources include the owner's time per week, the money for tools, and the accounts and hardware available, not only money.

The four phases of a project and where they sit here (PMBOK 6 names in brackets):

| Phase | What happens | Gates |
|-------|--------------|-------|
| 1. Starting the project (Initiating) | Define the goal and get approval to begin | 1 |
| 2. Organizing and preparing (Planning) | Research, test the riskiest assumptions with a pilot, plan, gather tools | 2, 3, 4 |
| 3. Carrying out the work (Executing, Monitoring and Controlling) | Publish in increments and check results against the analytics and the checklist | 5, 6 |
| 4. Closing the project (Closing) | Confirm the acceptance criteria, review lessons learned, decide what runs next (e.g. steady operation of the channel) | after 6 |

## 7. Planning rules

1. **No estimate without evidence.** Do not commit to a tool, schedule or budget before the uncertainty behind it is reduced. Before Gate 3, plan only the next gate and mark the rest `TODO → Plan phase`.
2. **Plan from the open questions.** List the register questions (`Docs/README.md` §5) and decisions that block each step; a step blocked by an open Tier C item is not ready to start.
3. **Each step states:** goal, output, exit criterion, time-box or stop rule, owner, and what blocks it (Q and D IDs).
4. **Sequence by risk, not by ease.** Do first the step whose answer is most likely to change a major decision (e.g. whether remade AI-voice story videos can be monetized at all).
5. **Close the plan.** Include what closing needs: acceptance against Clarify §6, lessons learned, and what happens after the project ends.
6. **Where the plan is kept:** TODO (decide when the first plan is made, then add it to the document map).
