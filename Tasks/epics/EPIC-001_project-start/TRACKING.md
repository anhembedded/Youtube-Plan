# EPIC-001 — Tracking

- **Epic:** [README](README.md)
- **Status:** 🟡 In progress
- **Target completion:** None — no deadline yet (Clarify C4, Q-008)
- **Renders:** GitHub Markdown, VS Code Mermaid preview, or mermaid.live.

---

## 1. Schedule (Gantt)

Durations of B, C and D are not estimated yet. Their bars show order only and are set when each task is sliced.

```mermaid
gantt
    title EPIC-001 - Start the project, Gates 1 to 4
    dateFormat  YYYY-MM-DD
    axisFormat  %d/%m
    todayMarker stroke-width:2px,stroke:#d33,opacity:0.6

    section Gate 1 Clarify
    EPIC-001A Clarify (end not estimated) :active,  a, 2026-10-29, 3d
    Gate 1 approval                       :milestone, g1, after a, 0d

    section Gate 2 Discover
    EPIC-001B Discover (not estimated)    :         b, after g1, 1d
    Gate 2                                :milestone, g2, after b, 0d

    section Gate 3 De-risk
    EPIC-001C De-risk (not estimated)     :         c, after g2, 1d
    Gate 3                                :milestone, g3, after c, 0d

    section Gate 4 Plan
    EPIC-001D Plan (not estimated)        :         d, after g3, 1d
    Gate 4                                :milestone, g4, after d, 0d
```

---

## 2. Task matrix

| Id | Task | Branch / PR | Risk | Status | Target / Merged |
| :--- | :--- | :--- | :-: | :--- | :--- |
| [EPIC-001A](incomplete/EPIC-001A_clarify.md) | Clarify — project charter approved | `claude/great-albattani-6cukhy` | 🟡 | 🟡 Active | — |
| EPIC-001B | Discover | — | 🔴 | 🔵 Planned | — |
| EPIC-001C | De-risk | — | 🔴 | 🔵 Planned | — |
| EPIC-001D | Plan | — | 🟡 | 🔵 Planned | — |

---

## 3. Log

| Date | Item | Event and outcome |
| :--- | :--- | :--- |
| 2026-10-29 | Scaffold | Epic created; EPIC-001A started with Clarify v0.1. |
| 2026-10-29 | EPIC-001A | Two rounds of questions answered; Clarify v0.2 written; waiting for both owners' approval. |
| 2026-10-30 | EPIC-001A | Clarify v0.3: P3 and G7 (how a channel grows); assumption log and source register added to the index. |

---

## 4. Blockers and dependencies

| Blocker or dependency | Tasks affected | Resolution / owner | Status |
| :--- | :--- | :--- | :--- |
| Answers to Q-001 to Q-009 | EPIC-001A | The owner | ✅ Resolved: answered or carried forward, 2026-10-29 |
| Both owners approve Clarify §7; how the partner records it (Q-010) | EPIC-001A | The owner and the partner | 🟡 Open |
