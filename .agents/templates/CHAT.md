# Chat — <task>

Copy to `.agents/workspace/<task>/chat.md`, or to the location `PROJECT.md` names.
Rules: `.agents/policies/multi-agent-coordination.md` (path from the repository root).
This channel preserves check-ins, relayed directions, decisions and verdicts. The
task record owns the contract and scoped directions; the state file
(`.agents/templates/STATE.md`) indexes current status and links the source records.

## Messages

- **<name> (<role>) · <prefix>-001 · <UTC time>**
  > Check-in: roles <roles>; session handle <handle | UNKNOWN>; write scope <paths>;
  > runs on <as known>.

- **<name> (<role>) · <prefix>-002 · <UTC time> · re <ID>**
  > <One result, question, proposal, or decision. Link files; do not paste them.>
  > Identity: <commit | base revision, diff digest, and the command that printed it>
  > Verdict: <ACCEPT | HOLD | AMEND> — <gate and scope; reviewer session/role>
  > Next: <who> — <what>

## Writing guidance

- Header: your name and role, an ID with your own prefix, UTC time, and the message
  you answer when there is one. No status words in the header.
- Body: about eight lines. The `Identity`, `Verdict`, and `Next` lines appear only
  when they apply. One identity per verdict; link required release/data manifests
  rather than generating per-file hash lists solely for review bookkeeping.
- Write the message to `<prefix>-msg.md` in the task folder and append it with the
  helper. Fill times, hashes, and counts by command substitution, for example
  `"$(date -u +%Y-%m-%dT%H:%M:%SZ)"`, never by typing them.
- Relayed user directions: quote verbatim, name the receiving session, mark RELAYED
  and any redaction.
- Record discussion and outcomes, not private reasoning. Keep objections when you
  link a long reply as a separate file.
- Prefix every quoted line with `>` so examples do not look like new participants.
