# Review and completion

- Finding classes: `CONFIRMED DEFECT`, `REQUIRED`, `ACCEPTED`, `OPTIONAL IMPROVEMENT`, `DEFERRED`, `OUT OF SCOPE`, `UNRESOLVED`, `BLOCKED`, `SUPERSEDED`. Each needs evidence and a resolution condition.
- On rework keep finding IDs stable; record the correction, an evidence-backed rebuttal, or an authorized deviation, with the revised identity; carry open findings across handoffs. Keep material safety and integrity findings even if no criterion names them.
- Verdicts: `ACCEPT`, `HOLD` (state the finding), `AMEND` (acceptable after a stated change), each on one artifact identity (`.agents/policies/evidence-and-provenance.md`), gate, and scope.
- Record each artifact's authors by session with all their roles. An author cannot review it by switching roles or ACCEPT their own work; no session gives a verdict for another.
- Before review, name the required gates, their scope, and each independent reviewing session. Agent consensus: every required gate has an ACCEPT from its reviewer on the same identity. Missing gates stay pending; no reviewers is not consensus.
- A change needs fresh review of the gates it affects; a reviewer may reaffirm an unchanged scope on the new identity, nobody else for it.
- Process exit, output, passing check, verdict, and human approval are separate outcomes; none supplies another. A failing required check or missing required evidence stays open; preference cannot turn it into acceptance. A budget or cancellation exit or a partial checkpoint is not success.
- Consensus is not task acceptance: only the completion authority records `ACCEPTED`. Report agreement as gate, scope, reviewer session and role, and verdict record. Silence is never acceptance.
- Before completion confirm: criteria, negative tests, validation, regressions, compatibility, docs, evidence, limits, safety, independent review, classified findings, close-out, authority decision.
- Close-out: list everything the task created that is not the deliverable (files, copies, logs, installed packages, running processes), each with keep or remove. Remove on the user's approval; say what you could not remove.
- "Finish" does not waive gates. Hand-patched generated output keeps regeneration `REQUIRED`.
