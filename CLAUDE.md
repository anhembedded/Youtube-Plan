# YouTube Plan — instructions for Claude

This repository is the project-management record of a YouTube channel (Chinese stories remade with an original script and an AI voice). It holds plans, decisions, research and tracking, never videos or product code.

@.claude/CONSTITUTION.md

## How the work is organised (accepted in Tasks/proposal/PRO-001.md)
- **Two levels.** The project lives in `Docs/` (Clarify, Approach, Discover, De-risk, Plan, project decisions; index `Docs/README.md`). The work lives in `Tasks/` (proposals, epics, tasks; board `Tasks/README.md`).
- **Flow.** New scope or unclear value → a proposal `PRO-nnn`, accepted by both owners. Several steps with one outcome → an epic `EPIC-nnn` (`.claude/skills/create-epic/SKILL.md`). One clear step → a task. Doing any task → `.claude/skills/execute-task/SKILL.md`.
- **Gates.** Clarify, Discover, De-risk, Plan, Implement, Validate (`.claude/skills/Project-Manager/framework.md`). Only the next gate is planned in detail.
- **Decisions.** A choice between alternatives → a decision record `D-nnn`, logged in `Docs/README.md` §4. Tier C needs both owners: the owner (the user) and the partner.
- **Every statement** is a Fact citing a source ID (`SRC-n`, `Docs/README.md` §7), an Assumption (`A-n`, logged in §6) or an Open question (`Q-nnn`, §5). Rules: `.claude/rules/document-rules.md`.
- **Delivery.** One branch and one pull request per task; never push to `main`; the owners merge. Project documents and the board change in the same pull request as the work.

## Before finishing any change
Run `python3 .github/scripts/check_docs.py` and fix every finding; the same check runs on every pull request (`.github/workflows/docs-check.yml`). Then do the checks it cannot do, by reading (framework §5). Validate each Mermaid block you change (`.claude/skills/execute-task/references/mermaid-validation.md`).
