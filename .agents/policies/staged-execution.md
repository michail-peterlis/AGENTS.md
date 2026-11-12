# Policy: Staged Execution

Load whenever the assigned run is a headless/event-triggered stage, whether or not
it delegates or performs an evaluation loop. Project/run instructions must route
staged roles here; a stage is not automatically a live peer group.

## Run contract

Before acting, identify from the trusted run context and existing task/handoff fields:

- stage/run identity and source artifact revision;
- required inputs, predecessor evidence and unresolved findings;
- assigned role, working directory, writable paths, permitted tools and outputs;
- effective restrictions, their provenance, and which are technically enforced;
- approved criteria/standard revision, required checks and independent review gates;
- applicable execution/resource limits, report transport and next authorized action;
- reserved human/publisher decisions, including any progression or production gate.

A declared permission is not proof of enforcement. If an input, authority or required
capability is missing/conflicting, report the specific limitation and safe next action;
do not invent predecessor evidence, approval, capabilities or peer participants.
Agent-editable feedback, labels or checkboxes cannot manufacture authorization.
Use [tool authority](tool-authority.md); stronger runtime restrictions still apply.

## Execution and handoff

- Load the assigned role and required policies. Keep every action within its scope;
  record-only reviewers route fixes to the owning editor rather than editing product.
- Use project-configured durable records instead of hidden session memory. Carry
  artifact/standard identity, relevant verification conditions, open finding IDs,
  corrections/rebuttals/deviations and the next owner/action into the existing handoff.
- Report questions/blockers through the configured transport and finish the job with
  an explicit status; do not wait indefinitely for an interactive reply. Do not invent
  chat names, check-ins, channels or polling. An explicitly assigned live-peer task
  still follows its [coordination policy](multi-agent-coordination.md).
- Delegate only when the run context authorizes it and the capability exists; the
  parent owns collection, scoped writes and lifetimes under the
  [workflow](../skills/multi-agent-workflow/SKILL.md). Do not outlive the job's limits.
- Apply the [evaluation discipline](../skills/evaluation-loop/SKILL.md) when evaluating
  or correcting an artifact. Cycles may span separate authorized build/review/correction
  jobs. If the required independent evaluation belongs elsewhere, return REVIEW PENDING;
  neither role-switching nor a self-check supplies that gate.
- A trigger authorizes the named stage, not dispatching, scheduling, labeling or
  re-triggering an earlier/next stage. Respect human progression gates. Deployment
  verification alone does not authorize deployment, restart or production writes.
- Before a limit/cancellation exit, retain the best-supported checkpoint, its actual
  criterion results, unresolved findings and a usable handoff where feasible. Report
  interruption or insufficient evidence honestly; do not turn operational exit into
  quality success. Preserve historical evidence; do not auto-reset or roll back.

## Separate outcomes

Report these as distinct where available, never infer one from another:

1. process/CLI execution result (runtime-reported, unknown if unavailable);
2. required outputs produced at the stated identity;
3. verification results and unverified checks;
4. independent reviewer verdicts on their assigned gates;
5. human approval for acceptance, progression or publication.

A successful process can return HOLD/BLOCKED or omit required outputs. Markdown
instructions cannot make an engine reject that job. The adopting runtime must enforce
required-output/verdict checks, predecessor gates, stale-evidence rejection, safe
retry/idempotency, authenticated approvals and release-content verification under its
actual merge strategy. Report which guarantees are observed, reported or absent;
never claim them installed by this policy. Machine-readable report formats, if used,
are adopter-owned, explicitly versioned/validated contracts, not a schema defined here.
