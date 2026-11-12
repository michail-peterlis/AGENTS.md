# Staged execution

Load when your run is one headless or event-triggered stage. A stage is not a live peer group.

- First take from the trusted run context and the task or handoff: stage and source revision; required inputs, predecessor evidence, open findings; your role, writable paths, permitted tools and outputs; restrictions and which are technically enforced; criteria, required checks, review gates; limits, report transport, next authorized action; decisions reserved for a human or publisher.
- Missing or conflicting input, authority, or capability: report it and the safe next action. Never invent predecessor evidence, approval, capabilities, or peers.
- Stay within your role and scope. A record-only reviewer routes fixes to the owning editor.
- Use the configured durable records, not session memory. The handoff carries artifact and standard identity, verification conditions, open finding IDs, corrections or rebuttals, and the next owner.
- Report questions and blockers through the configured transport and end with an explicit status; do not wait for an interactive reply. Invent no chat names, check-ins, channels, or polling. Delegate only if the run context authorizes it, within the job's limits.
- Evaluation and rework: `.agents/skills/evaluation-loop/SKILL.md`. Independent review that belongs to another stage: return `REVIEW PENDING`; a role switch or self-check does not supply it.
- The trigger authorizes the named stage only: no dispatching, scheduling, labeling, or re-triggering another stage. Respect human gates. Verifying a deployment authorizes no deployment, restart, or production write.
- Before a limit or cancellation exit, keep the best-supported checkpoint, its criterion results, open findings, and a usable handoff. An operational exit is not quality success. No automatic reset or rollback.
- Report separately, never inferring one from another: process result; required outputs at the stated identity; verification results and unverified checks; reviewer verdicts; human approval.
- These instructions cannot make a runtime reject a job: the adopting runtime must enforce required outputs and verdicts, predecessor gates, stale-evidence rejection, safe retries, and authenticated approvals. Say which guarantees you observed, which were reported, and which are absent.
