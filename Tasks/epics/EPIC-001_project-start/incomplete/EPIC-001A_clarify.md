# EPIC-001A — Clarify: the project charter is approved (Gate 1)

**Status:** 🟡 In progress
**Source:** the owner, 2026-10-29: *"we will do this Clarify phase"*, with the plan approved the same day
**Risk:** 🟡 — the owner's answers may leave budget, time or the end of the project undefined
**Size:** M — four documents and up to two rounds of questions
**Epic:** [EPIC-001](../README.md)
**Gate:** Clarify
**Depends on:** None

---

## 1. Context and problem
The working process is accepted ([PRO-001](../../../proposal/PRO-001.md)), but no project document exists. Clarify settles why, what, scope, constraints and done before any research or production starts.

## 2. Acceptance criteria
- [x] Clarify covers why, what, scope, constraints and done; every item has an ID and is traced both ways, or is marked "not addressed".
- [x] Every owner question (Q-001 to Q-009) is answered, or is carried forward as an Open question for the owners after two rounds.
- [x] Every item tagged for a later phase is listed in the open-question register or the Clarify grey areas, under its phase.
- [x] Budget, time and the end of the project are stated, or recorded as "none" or "owners to decide".
- [x] Approach (gates, exit criteria, risks), Stakeholders, Vocabulary and the index exist and agree with Clarify.
- [ ] Both owners' approval of Clarify §7 is recorded with their words and the date (Clarify C7).

## 3. Approach
1. Draft v0.1 from confirmed facts only; register every unknown as a question. *(done)*
2. Round 1 of questions: Q-001 to Q-004 (people, budget, time, success and end). Round 2: the partner's role, Q-006 to Q-008. *(done, 2026-10-29; Q-005 and Q-009 carried forward by the stop rule)*
3. Write v0.2 with the answers; update Approach, Stakeholders and the index. *(done)*
4. Both owners review and approve; record the approvals, close this task, update the Gantt.

## 4. Output
| File or place | Change |
| :--- | :--- |
| `Docs/Project-Management/Initiation-phase/Clarify/Clarify.md` | The charter |
| `Docs/Project-Management/Initiation-phase/Approach.md` | Gates, exit criteria, risk register |
| `Docs/Project-Management/Stakeholders.md` | Who is involved |
| `Docs/VOCABULARY/README.md` | Project terms |
| `Docs/README.md` | Index, approvals, decision log, question register |
| `Tasks/README.md`, this epic's README and TRACKING | Board and Gantt |

## 5. Verification
| Criterion | Check | Result |
| :--- | :--- | :--- |
| 1 | Read the trace P → O → DL → AC in Clarify §6.1 | Done 2026-10-29: P1, P3 → O1 → DL1 → AC1; P1 → O2 → DL2 → AC3; P2 → O3 → DL3 → AC4; AC2 withdrawn with its reason |
| 2–4 | Compare the register with Clarify, item by item | Done 2026-10-29: Q-001, Q-004, Q-006, Q-007 closed; Q-002, Q-003, Q-008 "owners to decide" by the Plan gate; Q-005, Q-009, Q-010 open with their gate |
| 5 | Every relative link resolves; the Gantt renders | Done 2026-10-29 (link and anchor check; Mermaid CLI 11.17.0) |
| 6 | The approvals table has both owners' words and date | Not done: waiting for the owner and the partner |

## Resume
- **Last verified:** Clarify v0.3 written on 2026-10-30 (v0.2 on 2026-10-29 from two rounds of answers).
- **Next action:** the owner and the partner review [Clarify v0.3](../../../../Docs/Project-Management/Initiation-phase/Clarify/Clarify.md) and approve §7; the owners answer Q-010 (how the partner records approval).
