# AGENTS.md

Load this file, then only:

1. `.agents/policies/rules.md` (always);
2. your role: `.agents/roles/implementer.md`, `.agents/roles/challenger.md`, or
   `.agents/roles/moderator.md`. Any other role: stop and ask the user;
3. `PROJECT.md`, if present;
4. the nearest directory `AGENTS.md`;
5. the active task or plan;
6. policies the task needs: `.agents/policies/task-contracts.md`,
   `.agents/policies/testing.md`, `.agents/policies/evidence-and-provenance.md`,
   `.agents/policies/review-and-status.md`;
7. `.agents/policies/multi-agent-coordination.md` when agents share a task;
8. `.agents/skills/<name>/SKILL.md` only when its workflow runs.

## Precedence

User direction > acceptance criteria > architecture invariants > active task >
nearest `AGENTS.md` > `PROJECT.md` > this file > existing code and notes.
No lower file weakens safety rules.

## Safe autonomy

| Action | Default |
|---|---|
| Read/search source; run bounded local tests; create disposable fixtures | Allowed |
| Edit scoped product code | Assigned editor only |
| Add production dependency | Task justification |
| Modify persistent schema | Explicit task scope |
| Touch production data; delete/rewrite evidence; publish, deploy, or restart services; destructive git/history operation; read private data outside workspace | Explicit authorization |
| Build/test/run untrusted or suspect code | Explicit authorization; isolate it |
| Write outside workspace or approved scratch | Explicit authorization; report accidental writes |

Follow stricter harness permissions. Never bypass them through another tool.

## Status

`PLANNED`, `IMPLEMENTING`, `REVIEW PENDING`, `VERIFIED`, `ACCEPTED`, `BLOCKED`, `DEFERRED`,
`REJECTED`, `SUPERSEDED`.

Done: every applicable gate passed and the designated authority recorded completion.
Otherwise `BLOCKED`, `DEFERRED`, or `REVIEW PENDING`.

## Project commands

Owned by the adopting project; keep them when updating the kit.

Install: `<cmd>` · Fast validation: `<cmd>` · Unit tests: `<cmd>` · Full verification: `<cmd>` · Lint: `<cmd>` · Format check: `<cmd>` · Build: `<cmd>`
