# Policy: Review and Status

Use precise classifications.

## Finding classifications

- **CONFIRMED DEFECT** — implementation is demonstrably incorrect.
- **REQUIRED** — must be resolved before scoped completion.
- **ACCEPTED** — satisfies the applicable contract.
- **OPTIONAL IMPROVEMENT** — useful but not required.
- **DEFERRED** — valid work intentionally postponed with justification.
- **OUT OF SCOPE** — unrelated to the active task.
- **UNRESOLVED** — evidence is insufficient.
- **BLOCKED** — progress depends on an external decision/resource.
- **SUPERSEDED** — replaced by newer authoritative direction.

Every finding should state evidence and resolution conditions. In a review/correction
cycle, retain stable finding IDs, criterion or safety basis, impact/priority and owning
editor. Record correction, evidence-backed rebuttal or authorized deviation and the
revised identity; independently verify closure and carry open findings across handoffs.
Material safety/integrity findings are not discarded because a criterion omitted them.

## Role verdicts

A role's verdict always names an artifact identity and the scope it covers, including
the approved standard and relevant verification inputs under
[evidence freshness](evidence-and-provenance.md):

- **ACCEPT** — this role finds the artifact satisfies its contract;
- **HOLD** — this role blocks it; state the finding;
- **AMEND** — acceptable after a stated change.

Record each artifact's authors by session, including all roles they held. An author
cannot independently review that artifact by switching roles; no session gives a
verdict for another session.

Before review, name the required gates, each gate's scope and independent reviewing
session. A session may cover several gates only where the contract permits it; role
labels alone do not establish independence. Authors may clarify findings, not ACCEPT
their own work.

**Agent consensus** means every required review gate has an ACCEPT from its assigned
independent reviewer on the same artifact identity. Specialist ACCEPTs cover their
stated gate, not unrelated parts of the artifact. Missing gates or reviewers remain
pending; an empty set of reviewers is not consensus. Changes require fresh review of
affected gates. Reviewers may explicitly reaffirm unchanged scopes on the new identity
without rerunning unrelated checks; a coordinator cannot reaffirm on their behalf.

A process exit, produced report, passing check, reviewer verdict and human approval
are distinct outcomes, especially in [staged jobs](staged-execution.md). None supplies
the others. A failing required check or insufficient required evidence remains open;
model preference cannot turn it into acceptance.

Consensus is not task acceptance: only the designated completion authority records a
task as ACCEPTED. Report it as gate, scope, reviewer session/role, and verdict record.

Do not invent compound statuses; use the status vocabulary in the root `AGENTS.md`.

Silence is never acceptance.
