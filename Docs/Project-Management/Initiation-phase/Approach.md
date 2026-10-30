# Approach — how the project is run

## At a glance
| Item | Content |
| :--- | :--- |
| Method | Six gates: Clarify, Discover, De-risk, Plan, Implement, Validate. Evidence before commitment; one pilot video before any batch. |
| Where we are | Gate 1, Clarify, in progress. |
| Biggest risk | R-1: the channel is refused for monetization because its videos count as reused or inauthentic content. |
| Next | Both owners approve [Clarify](Clarify/Clarify.md); then Discover. |

| Field | Value |
| :--- | :--- |
| Version | 0.3 (Draft, for approval) |
| Date | 2026-10-29 |
| Change from 0.1 | Two approvers (§3); Gate 1 needs both; R-5 no longer tied to an income target; R-7 and R-8 added |
| Change from 0.2 | R-1, R-6 and R-7 restated from YouTube's official pages, checked 2026-10-30 (Clarify C5) |

---

## 1. Principles
1. **No commitment before evidence.** No tool, budget split or schedule is fixed before the uncertainty behind it is reduced. Before Gate 3, only the next gate is planned in detail.
2. **Riskiest assumption first.** Work is ordered by Impact × Uncertainty (§7), not by what is easiest.
3. **Smallest end to end first.** One pilot video, from story to upload, before any batch, series, second language or second channel.
4. **Facts are labelled.** Every statement is a Fact (with source and date), an Assumption (with how it is checked) or an Open question (with who answers).
5. **Remake, never copy** ([Clarify C1](Clarify/Clarify.md#51-constraints)).

The method behind the gates is in [Project-Process](../../Project-Process/Thinking%20New%20project.md).

## 2. How the work is organised
The repository layout, the IDs, the decision process and the flow from idea to epic to task are in [PRO-001](../../../Tasks/proposal/PRO-001.md). Project documents live in `Docs/`; the work is tracked in `Tasks/`, on the [board](../../../Tasks/README.md).

## 3. Who decides
**The owners** (the owner and the partner) decide together anything that spends money, picks a tool or provider, creates an account, publishes, uses someone else's material, or changes scope, acceptance criteria, budget or deadline; each such decision needs both approvals ([Clarify C7](Clarify/Clarify.md#51-constraints)). Every other choice is recorded in a decision record and reported to the owners. Approvals are recorded in the [index](../../README.md#3-approvals). Stakeholders are in [Stakeholders](../Stakeholders.md).

## 4. Life cycle
Incremental. Gates 1–4 are tracked as [EPIC-001](../../../Tasks/epics/EPIC-001_project-start/README.md). Gate 4 (Plan) writes the epic roadmap for Gates 5 and 6 (`TODO → Plan phase`).

## 5. Gates and exit criteria
A gate is passed only when its exit criterion is met and the evidence is linked in the [index](../../README.md). Merged work alone does not pass a gate.

| Gate | Step | Exit criterion | Evidence | Time-box or stop rule |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Clarify | Clarify covers why, what, scope, constraints and done; every owner question is answered or carried as an Open question; both owners approve Clarify §7. | Clarify §7 and the approvals table | Two rounds of questions to the owner (done 2026-10-29); what is still open is carried forward |
| 2 | Discover | Every `TODO → Discover phase` item has a finding with sources and dates, or is passed to De-risk. | The Discover document | `TODO → Plan phase` (set when EPIC-001B is sliced) |
| 3 | De-risk | Every high-priority risk in §7 has a spike verdict, or an accepted response. | The De-risk document and spike files | Each spike has its own time-box |
| 4 | Plan | Milestones and an epic roadmap exist, with scope, schedule and resources stated, from the Gate 3 evidence. | The Plan document | `TODO → Plan phase` |
| 5 | Implement | Each epic of the roadmap meets its exit criteria. | Epic README and tracking files | Set per epic |
| 6 | Validate | The acceptance criteria of [Clarify §6.1](Clarify/Clarify.md#61-acceptance-criteria) are met. | Measurements against each criterion | `TODO → Plan phase` |

## 6. Reporting
Each status report leads with the conclusion. It then covers where we are (gate and step), what blocks the next gate and who can unblock it, what was done since the last report, new or changed risks, and the next step and who must act.

## 7. Risk register
Priority = Impact × Uncertainty. Every risk is an Assumption until a spike or a measurement closes it.

| ID | Risk statement | Impact | Uncertainty | Priority | Response | Action | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R-1 | If YouTube judges the videos as readings of material the channel did not create, or as mass-produced template content (Clarify C5 b, c), monetization is refused, so O1 fails. | High | High | 🔥 Very high | Mitigate | Discover: how far a remake must depart from its source, from cases and guidance; De-risk: the pilot checked against C5 b and c (A1) | Open |
| R-2 | If source creators or platforms file copyright claims, videos are blocked or the channel gets strikes. | High | High | 🔥 Very high | Mitigate | Discover: copyright and platform rules (A2); keep C1 on every video | Open |
| R-3 | If one video takes more hours than the owners have (C3), the channel cannot publish regularly. | High | High | 🔥 Very high | Mitigate | De-risk: a pilot video with hours recorded (A3) | Open |
| R-4 | If the tools cost more than the budget (C2), the workflow must change. | Medium | High | 🟠 High | Mitigate | Discover: tool prices with dates; De-risk: real cost of the pilot | Open |
| R-5 | If the chosen language and audience pay little per view, the monetized channel earns little for the same work (P1). | High | Medium | 🟠 High | Mitigate | Discover: revenue per 1,000 views by language and country, with sources | Open |
| R-6 | If YouTube's rules on AI-made content change, a working channel can lose monetization. The rules did change twice in 15 months (2025-07-15, 2027-02-01; Clarify C5). | High | High | 🔥 Very high | Accept, and monitor | Re-check C5 at every gate and record the date checked | Open |
| R-7 | If a new channel cannot reach the threshold for new applicants (8,000 watch hours in 365 days or 20 million Shorts views in 90 days, from 2027-02-01; Clarify C5 a), AC1 is not met. | High | High | 🔥 Very high | Mitigate | Discover: what growth such channels reach and in how long; De-risk: the pilot's numbers (A5) | Open |
| R-8 | If machine translation loses the meaning of a Chinese story, the remake is weak or wrong. | Medium | High | 🟠 High | Mitigate | Discover: compare translation tools on sample stories (A4); De-risk: check the pilot story | Open |

**Next:** after both owners approve Clarify, Discover takes R-1, R-2, R-7, R-4, R-5 and R-8 first.
