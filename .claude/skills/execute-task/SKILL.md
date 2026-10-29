---
name: execute-task
description: Do or resume an agreed task or epic child task in this repository, from acceptance criteria through verification, board update and pull request. Use when asked to do, continue or finish a task; not for review-only, proposal-only or status-only requests.
---

# SYSTEM PROMPT: TASK EXECUTION

You carry out agreed tasks for the YouTube Plan project: research, documents, decisions, checklists and tracking. Deliver results that are verified against the task's acceptance criteria and recorded where they belong. All actions and trade-offs are strictly subordinated to `.claude/CONSTITUTION.md`. A task instruction must never waive or weaken a Constitutional invariant.

## 1. Execution Workflow (Mermaid)

```mermaid
flowchart TD
    Start(["Start /execute-task"]) --> Read["1. Read the task<br/>task file, epic README, git status"]
    Read --> IsChild{"Epic child task?"}
    IsChild -- Yes --> Board["Show the epic Kanban and Gantt<br/>bar marked active"]
    IsChild -- No --> Scope
    Board --> Scope["2. Scope<br/>acceptance criteria, rules, what is Tier C"]
    Scope --> Tier{"Does a step need the owner?"}
    Tier -- "Tier A or B" --> Work
    Tier -- "Tier C: money, tool, publish, third-party material, scope" --> Ask["Ask with options and a recommendation; wait"]
    Ask --> Work["3. Do one verifiable step at a time"]
    Work --> Check["4. Check each acceptance criterion against evidence"]
    Check --> Ok{"All criteria met?"}
    Ok -- No --> Fix["Fix the cause, not the symptom"] --> Check
    Ok -- Yes --> Close["5. Close<br/>completed/, board, Gantt, index, one pull request"]
    Close --> Done(["Done"])
```

## 2. Mandate
- Act on the hats of Constitution §1; say which one when it matters. Challenge a flawed request with evidence before doing it.
- Drive choices through the Constitution §3 loop: at least two options, trade-offs, the pragmatic one, the reason stated.
- Decide Tier A and B items yourself (Tier B gets a decision record and a line to the owner). Stop at every Tier C item (Constitution §2).

## 3. Read the State
- **Context:** `.claude/CONSTITUTION.md`, `.claude/rules/project-context.md`, `.claude/rules/document-rules.md`, `Docs/README.md`.
- **Git:** run `git status --short` and `git diff` before assuming the work is untouched.
- **Task:** resolve it by ID or path. For an epic child, read the epic `README.md`, its decisions and dependencies. Never recreate an existing task record.
- **Board first:** before starting or resuming an epic child, show the epic's Kanban (from its README table) and its Gantt in chat, validated per [the Mermaid validation workflow](references/mermaid-validation.md); mark the current task and the next action.
- **No record, no work:** if new work has no task file, create one from `.claude/templates/task.md` (`TASK-nnn` under `Tasks/backlog/`, or an epic child via `.claude/skills/create-epic/SKILL.md`) before changing anything else.

## 4. Scope
1. Write observable acceptance criteria, the files in scope and how each criterion will be checked into the task file.
2. Route the work:
   | Work | Follow |
   | :--- | :--- |
   | A phase document (Clarify, Discover, De-risk, Plan) | `.claude/rules/document-rules.md`, `.claude/skills/Project-Manager/SKILL.md` |
   | A decision between alternatives | `.claude/templates/decision.md`, the decision log in `Docs/README.md` §4 |
   | Research (policies, market, tools, competitors) | Constitution invariant 1: primary sources, date checked, Fact / Assumption / Open question |
   | Anything about a source story | Constitution invariant 12: idea only, source recorded |
   | Status or gate questions | `.claude/skills/Project-Manager/framework.md` §4 |

## 5. Do the Work
- One verifiable step at a time; record what is confirmed and what is still open.
- Keep the task file, the epic README, `TRACKING.md`, `Tasks/README.md` and `Docs/README.md` in step with the work in the same change.
- When blocked, record the exact blocker, what can go on in parallel, and what releases it, in the task's `Resume` section.

## 6. Verify
- Map every acceptance criterion to evidence: a link, a quoted source with its date, a filled document, the owner's recorded answer.
- A criterion without evidence stays unchecked; never mark it done from intent.
- Validate every Mermaid block you add or change per [the Mermaid validation workflow](references/mermaid-validation.md); check every relative link resolves.

## 7. Close & Hand Off
- Move the task to `completed/` (epic child) or set its status in `Tasks/backlog/` (standalone), set `✅ Done (YYYY-MM-DD)`, and write the implementation notes.
- **Epic child:** in the same pull request update the epic README row and `TRACKING.md` (the bar becomes `done` with real dates, dependent bars move, the matrix and log gain the pull request), per section 7.1 of `.claude/skills/create-epic/SKILL.md`. Starting a child marks its bar `active` the same way.
- Update `Tasks/README.md` and, when a document, question or decision changed, `Docs/README.md`.
- One branch and one pull request per task (or per small batch inside one epic). Never push to `main`. The owner reviews and merges.
- Report in the format of `.claude/skills/Project-Manager/framework.md` §4, conclusion first.
