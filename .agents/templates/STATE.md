# State — <task>

Current status summary and resume index for a shared task, derived from its contract
and append-only channel. Keep one file at `.agents/workspace/<task>/STATE.md` (or the
configured location), overwritten in place. Update on material status changes, pause,
stage handoff and before long unattended runs. Link source records rather than copying
directions, decisions or delivered work; the summary does not supersede those records.

Updated: <UTC from tool output> by <name> — <pause | stage handoff | unattended run | takeover>

## On resume

- Read: <task record>; <channel> from <last message ID>
- First action: <who does what>
- Re-arm: <working loop and standing instructions the pause interrupted>

## Roster

Copied from check-in messages; UNKNOWN where nothing was posted.

| Name | Roles | Runs on | Session handle | Write scope | Latest check-in or pause note | Resume with |
|---|---|---|---|---|---|---|
| | | | | | <message ID> | <prompt or command> |

## User directions in force

- <scope and reference to the authoritative task/project entry; relay message ID>

## Waiting on the user

- <decision or action> — asked by <name> in <message ID>

## Items

| Item | State | Owner | Identity | Review gates / verdicts |
|---|---|---|---|---|
| <stage or work item> | <root vocabulary> | <name> | <commit, or base + diff digest> | <gate, scope, reviewer session/role, message ID; link authors in handoff> |

## For a fresh session

- Interrupted or half done: <what and where; an interrupted run is not a pass>
- Only local or not committed: <paths>
- Limits of this environment: <what it cannot see or do; operator shell>
