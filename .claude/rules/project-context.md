---
description: Informal background on the team, the client and why the project exists, so the AI understands the situation. Not the charter.
---

# Project Context

Informal background so that an AI assistant understands the situation. It is **not** the project charter.
Scope, constraints, assumptions, open questions and acceptance criteria live in
[Clarify](../../Docs/Project-Management/Initiation-phase/Clarify/Clarify.md) and [Approach](../../Docs/Project-Management/Initiation-phase/Approach.md). If this file conflicts with them, they win.
State only what the owner confirmed; do not fill gaps with assumptions.

## Who and where

- Our team is **F_MAGGG_TEAM**, an outsource team working for the client **MAGGG_COMP** on the project **MAGG_PROJ**.
- We work on the client's PCs (remote PC, Windows). Any app we install needs to be granted first.
- The KB and the RAG are owned by our team, not by the client.

## Why this sub-project exists

- The project lead thinks onboarding is too slow and that a searchable Knowledge Base (KB) would help.
- The project lead chose a RAG as the solution, and had AI read the source code to generate many `.md` files about end-user use cases of the app.
- Nobody has reviewed those files for correctness.
- The project lead assigned me (Nathan Tran) to lead the sub-project that builds the RAG. The project lead is the only other person on it.
- This is a **proposal project**, not a client requirement: no budget, no deadline.
- Onboarding is the motivation, but this sub-project does not measure or own it. We provide the RAG capability and do not care what people use it for.

## Working reality (not for the charter)

- Reviewing the KB is not an official task. The project lead cannot assign it, the domain is large and needs many developers and testers, and I do not know whether members would agree to do it.
- Today people find knowledge by asking colleagues, or in Confluence and guide documents. No single source is the true one.
- The client provides Copilot 365 and GitHub Copilot Enterprise. I do not yet know whether our own tool may call them.
- Expected number of users: roughly 10 to 100.

## Still to ask

Tracked in the open-question register (`Docs/README.md` §5), Clarify §5.1 and Grey area G1. Most important: may our tool use the client's Copilot services or any other external LLM, who reviews the KB, how many `.md` files exist now, and how the client grants app installs.
