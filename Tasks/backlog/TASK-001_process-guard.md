# TASK-001 — Every session follows the process, and a broken rule is caught automatically

**Status:** ✅ Done (2026-10-30)
**Board:** `CLAUDE.md` loads the rules in every session; a check runs on every pull request and fails when a documentation rule is broken.
**Source:** the owner, 2026-10-30: *"PRO-001, có được hệ thống AI nhận thức không? Nếu một lúc nào đó làm trái quy trình thì AI có nhận thức được không?"* — is PRO-001 known in every session, and is a breach of the process noticed? Then *"oki ní, làm đi"* — go ahead with both proposals.
**Risk:** 🟢 — a check that is too strict can block a correct pull request; it lists each finding, and known exceptions carry a reason
**Size:** S — one instruction file, one check script, one workflow
**Depends on:** [PRO-001](../proposal/PRO-001.md)

---

## 1. Context and problem
Only the rules folder was loaded in every session; the main rules and the process of PRO-001 were read only when a procedure pointed to them. Every consistency check was done by reading, so a missing log entry or a broken link could be merged unnoticed.

## 2. Acceptance criteria
- [x] Every session loads the main rules and a summary of PRO-001.
- [x] A check runs on every pull request and fails on a broken link or anchor, an ID cited but not defined, an assumption missing from the log, a source missing from the register, a document or epic missing from the index or board, process words in project documents, personal data or secrets, or a diagram that does not render.
- [x] The check passes on the current documents and fails on each planted violation.

## 3. Approach
An instruction file at the root of the repository that loads the rules; a small check script with no dependencies; a GitHub workflow that runs it and renders every diagram.

## 4. Output
| File or place | Change |
| :--- | :--- |
| `CLAUDE.md` | New: loads the rules, summarises the process |
| `.github/scripts/check_docs.py` | New: the checks |
| `.github/workflows/docs-check.yml` | New: runs them on every pull request and on `main` |
| Rules and procedures under `.claude/` | Point to the check before finishing a change |

## 5. Verification
| Criterion | Check | Result |
| :--- | :--- | :--- |
| 1 | `CLAUDE.md` exists at the root and loads the rules file | Done 2026-10-30 |
| 2 | 11 violations planted in a copy of the repository (broken link, broken anchor, R-, Q-, D-, SRC- IDs not defined, assumption not logged, document not in the map, epic not on the board, process word, e-mail address) | Done 2026-10-30: all 11 reported, exit code 1 |
| 3 | The check on the real documents; the workflow's diagram step run locally | Done 2026-10-30: "OK: 46 Markdown files checked"; 12 of 12 diagrams render. The first run on GitHub is recorded in the pull request |

## Notes
The first run found a real exception: PRO-001 describes the repository's own process, including the rules folder, so it is listed as a known exception with its reason. Discussed in chat on 2026-10-30.
