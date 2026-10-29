# Clarify — the project charter

## At a glance
| Item | Content |
| :--- | :--- |
| Problem | The owner wants an income from a YouTube channel and has not yet decided what to publish, in which language or format, or with which tools. |
| Objective | A channel that earns money with Chinese stories remade with an original script and an AI voice, produced by a repeatable workflow the owner can sustain (§2.2). |
| Not done | Re-uploading or lightly editing other people's videos; storing videos in this repository (§4). |
| Limits | Remake, never copy (C1); budget, time and deadline are still to be set by the owner (C2–C4). |
| Done when | The acceptance criteria in §6.1 are met; their targets are still to be set by the owner (Q-004). |
| Waiting for | The owner's answers to Q-001 to Q-009 ([register](../../../README.md#5-open-question-register)). |
| Next | Discover (Gate 2), after the owner approves this charter (§7). |

| Field | Value |
| :--- | :--- |
| Version | 0.1 (Draft) |
| Origin | The owner, 2026-10-29: *"I want to make money by creating a youtube channel, the content i want to post is AI story copy from some social media on China."* Refined the same day: the stories are remade with the owner's own script and an AI voice, not copied (answer "(c)"). |

**Revision history**

| Version | Date | Author | Description |
| :--- | :--- | :--- | :--- |
| 0.1 | 2026-10-29 | Assistant, for the owner | First draft from the owner's confirmed answers; open items registered as Q-001 to Q-009 |

**How to read this document.** Every statement is a **Fact** (with its source), an **Assumption** (with how it will be checked) or an **Open question** (with who answers). A `TODO` with no phase is decided now, in Clarify, by the owner. A `TODO → Discover phase`, `→ De-risk phase` or `→ Plan phase` is answered later, in that phase. Targets marked *e.g.* are examples until the owner confirms them.

---

## 1. Problem

### 1.1 Background
The owner wants to start a YouTube channel to earn money. The content is stories found on Chinese social media, remade in the owner's own words and voiced by an AI voice (Fact, the owner, 2026-10-29). This repository manages the project: plans, decisions, research and tracking. It holds no videos (Fact, the owner, 2026-10-29). How the work is organised is set out in [PRO-001](../../../../Tasks/proposal/PRO-001.md).

### 1.2 Pains
| ID | Pain | Evidence |
| :--- | :--- | :--- |
| P1 | The owner has no income from YouTube and wants one. | Fact, the owner, 2026-10-29 |
| P2 | The owner has not decided the story genre, the language and audience, or the video format, so there is nothing concrete to produce yet. | Fact, the owner, 2026-10-29: "Not decided" to each |

## 2. Objectives

### 2.1 Requirement versus solution
The requirement is **income from a YouTube channel built on remade Chinese stories**. The genre, language, format, tools and income streams are candidate solutions. They are examined in Discover and De-risk; none is chosen here (§4).

### 2.2 Objectives
| ID | Objective (outcome) | Measure and target | Addresses |
| :--- | :--- | :--- | :--- |
| O1 | The channel earns money. | Income per month, in USD. Target: `TODO` — the owner (Q-004). | P1 |
| O2 | Videos are produced by a repeatable workflow that fits the owner's time and budget. | Hours and cost per video. Target: within C2 and C3; real values `TODO → De-risk phase` (pilot video). | P1 |
| O3 | Genre, language, format and tools are chosen on evidence, not guessed. | Number of the grey areas G1–G4 settled by an accepted decision record. Target: 4 of 4 before production starts. | P2 |

## 3. Deliverables
| ID | Deliverable | Objective |
| :--- | :--- | :--- |
| DL1 | A YouTube channel, set up and publishing, with a monetization status. | O1 |
| DL2 | A written production workflow (story → script → voice → visuals → edit → upload) with a checklist per video. | O2 |
| DL3 | Decision records for genre, language and audience, format, and tools. | O3 |

## 4. Scope and grey areas
**In scope:**
- Choosing the channel's genre, language, audience, format and tools, on evidence.
- Setting up the channel and the production workflow.
- Producing and publishing videos until the acceptance criteria are met.
- Managing the project in this repository.

**Out of scope:**
- Re-uploading, translating or lightly editing someone else's video (C1).
- Storing videos, audio or project files of the videos in this repository (C6); they live in the owner's own storage.
- Running the channel after the project ends; that is ongoing operation. Where the project ends is Q-004.

| ID | Grey area (open choice) | Candidates | Settled by |
| :--- | :--- | :--- | :--- |
| G1 | Story genre | e.g. folk tales and history, family drama, horror and mystery, romance and fantasy | `TODO → Discover phase, then De-risk phase` |
| G2 | Video language and target audience | e.g. English, Vietnamese, Chinese, several | `TODO → Discover phase` |
| G3 | Video format | Long videos, Shorts, or both | `TODO → Discover phase, then De-risk phase` |
| G4 | Tools for script, voice, visuals and editing | To be listed in Discover | `TODO → Discover phase, then De-risk phase` |
| G5 | Source platforms for stories | e.g. Douyin, Bilibili, Kuaishou, Xiaohongshu, Weibo | `TODO → Discover phase` |
| G6 | Income streams | Ads (Partner Program), sponsorship, affiliate links, other platforms | `TODO → Discover phase` |

## 5. Constraints and assumptions

### 5.1 Constraints
| ID | Constraint | Source | Affects |
| :--- | :--- | :--- | :--- |
| C1 | **Remake, never copy.** A source story is used only as an idea. The script is original, the voice is an AI voice, and the source's footage, images, voice, music and text are not reused. The source of every story is recorded. | Fact, the owner, 2026-10-29 (answer "(c)") | O2, DL2, G5, A1, A2, R-1, R-2 |
| C2 | Budget per month for tools. | `TODO` — the owner (Q-002) | O2, G4, R-4 |
| C3 | The owner's time per week. | `TODO` — the owner (Q-003) | O2, A3, R-3 |
| C4 | Deadline for the project. | `TODO` — the owner (Q-008) | O1, AC1, AC2 |
| C5 | YouTube's rules for monetization: reused content, inauthentic content and disclosure of AI-made content. | YouTube policy pages; content `TODO → Discover phase` (read them and record the date checked) | O1, DL1, A1, R-1, R-6 |
| C6 | This repository holds project management only; no videos. | Fact, the owner, 2026-10-29 | DL2 |

### 5.2 Assumptions
| ID | Assumption | How it is verified | Status |
| :--- | :--- | :--- | :--- |
| A1 | Videos of remade stories with an original script and an AI voice can be accepted for monetization. | Discover: read the policies (C5). De-risk: the outcome of a real review. | Open |
| A2 | Using a story as an idea only, and remaking it under C1, does not lead to copyright claims. | Discover: platform and copyright rules. Later: claims received on published videos. | Open |
| A3 | One video can be produced within the owner's weekly time (C3). | De-risk: a pilot video, with hours and cost recorded. | Open |
| A4 | The owner can understand the source stories, by reading Chinese or through translation. | The owner (Q-006). | Open |

## 6. Acceptance

### 6.1 Acceptance criteria
| ID | Criterion | Metric | Target | How measured |
| :--- | :--- | :--- | :--- | :--- |
| AC1 | The channel is monetized. | Monetization status | e.g. accepted into the YouTube Partner Program; by when: `TODO` — the owner (Q-004, Q-008) | YouTube Studio |
| AC2 | The channel earns the target income. | Income per month, USD | `TODO` — the owner (Q-004) | YouTube Studio, payout reports |
| AC3 | One video can be produced end to end within the limits. | Hours and cost per video | Within C2 and C3 | The production log of the pilot video and later videos |
| AC4 | The channel's main choices are made on evidence. | G1–G4 settled by accepted decision records | 4 of 4 | Decision log in the [index](../../../README.md#4-decision-log) |

**Trace.** P1 → O1 → DL1 → AC1, AC2. P1 → O2 → DL2 → AC3. P2 → O3 → DL3 → AC4.

## 7. Approval
Approval of the scope and constraints, to proceed to Discover. It is not a choice of genre, language, format or tool.

| Name | Role | Decision | Date |
| :--- | :--- | :--- | :--- |
| The owner | Owner | Pending | Pending |

**Next:** after approval, Discover (Gate 2) researches G1–G6, C5, A1 and A2. It is planned as the next task of [EPIC-001](../../../../Tasks/epics/EPIC-001_project-start/README.md).
