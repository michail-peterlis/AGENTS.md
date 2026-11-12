# Chat: <task>

Rules: `.agents/policies/multi-agent-coordination.md`. Append with `append.sh`; fill times, hashes, and counts by command substitution, e.g. `"$(date -u +%Y-%m-%dT%H:%M:%SZ)"`.

- **<name> (<role>) · <prefix>-001 · <UTC time>**
  > Check-in: roles <roles>; session handle <handle | UNKNOWN>; write scope <paths>.

- **<name> (<role>) · <prefix>-002 · <UTC time> · re <ID>**
  > <one result, question, or decision; link files>
  > Identity: <commit | base revision, diff digest, and its command>
  > Verdict: <ACCEPT | HOLD | AMEND> — <gate and scope>
  > Next: <who> — <what>

`Identity`, `Verdict`, `Next` only when they apply. User directions: verbatim, with the receiving session, marked RELAYED.
