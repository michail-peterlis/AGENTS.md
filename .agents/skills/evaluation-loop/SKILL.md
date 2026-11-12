# Skill: Evaluation Loop

Load for artifact evaluation and authorized correction after a failed review, at any
contract tier. This is the normal build/evaluate/revise discipline, not a separate
mode or permission gate. Scale records to the task; a first-pass success needs no
artificial extra round. Not for mere status or commit preparation.

## Inputs

- The [task contract](../../policies/task-contracts.md): approved criteria, required
  evidence, negative criteria, constraints, authorized deviations and relevant limits.
- Inspectable artifact and baseline/reference, named by their
  [identity](../../policies/evidence-and-provenance.md), plus neutral verification commands.
- Assigned editor, required independent review gates, actual capabilities and the
  next authorized action. For a staged job, load
  [staged execution](../../policies/staged-execution.md).

## Workflow

1. Establish the inspectable standard before the first pass, proportionate to the
   tier. It may be a specification, executable checks or a reference artifact.
   Confirm subjective comparison conditions; blind A/B suits some preference tests,
   not every correctness/security review. Change an approved standard or deviation
   explicitly, never lower the bar silently to make a revision pass.
2. Build or revise within assigned ownership. Keep the actual output inspectable;
   retain the last supported checkpoint and its criterion results, not duplicate
   product trees. A partial checkpoint is not fully verified. No reset, deletion or
   production rollback is authorized by checkpoint retention.
3. Run cheap applicable executable checks first where practical. Classify failures
   at the product, fixture, specification or environment layer before acting. A
   failing required check blocks acceptance; preference cannot override it. Useful
   read-only critique may diagnose the blocker or cover independent scope alongside
   it. Do not invent a universal ranking of graders.
4. Where the contract requires independent review, each criticism round uses a fresh,
   genuinely separate critic context. Select the goal, approved standard, relevant
   constraints/deviations, artifact identity and neutral run instructions from the
   existing [handoff](../../templates/HANDOFF.md). Do not forward builder persuasion,
   implementation history or earlier verdicts. A critic opening the whole record itself
   selects only those neutral inputs and treats author claims as REPORTED, not verified
   results. If already exposed to history/verdicts, report that context limitation;
   do not pretend the history was erased or claim a clean context.
   The critic inspects actual output, not the author's summary; reports criterion
   pass/fail/insufficient evidence, concrete gaps and priority; and does not invent
   objections to seem demanding. A comparison may tie or be inconclusive, not a win
   unless the standard says so.
5. Consolidate findings in existing review/task records with stable IDs, criterion
   or safety basis, evidence, impact/priority and resolution condition. Retain material
   safety/integrity risks even if omitted from the acceptance list; escalate necessary
   scope changes. Preserve disagreements and evidence-backed rebuttals. Unrelated
   aesthetic preferences need not force another round.
6. Route corrections to assigned editors; critics do not acquire product-write
   authority. Record correction, rebuttal or authorized deviation against each finding
   and the revised identity; carry unresolved findings across handoffs. Where the
   contract requires independent review, independently verify closure on the changed
   artifact and use a fresh critic for the next judgment, not the prior critic's memory.
   Otherwise re-run failed checks and verify remaining required criterion evidence;
   this is a self-check, not independent acceptance. Protect previously verified
   criteria and report regressions, measured gaps and oscillation, not just counts of
   new PASS results.
7. Report each round through the configured authorized transport/progress record,
   linking actual outputs and the next owner/action. If only an end-of-job report is
   visible, state that limitation; do not imply a live watcher or gain publishing
   rights merely to report progress. Required gates stay pending until verified on
   the applicable identity; [consensus](../../policies/review-and-status.md), task
   acceptance and publication remain separate decisions.

## Continue, hand off or escalate

Honor existing user/project/job limits without asking again. Without a supplied
limit, state that work continues until the standard is met or the user stops it;
there is no invented cap, extra opt-in or automatic pause before round two. Continue
only within already granted role, write scope, stage and effective restrictions.

Diagnose ineffective repetition and change approach within scope. Neither a round
with no new PASS nor a fixed round count proves a stall. An automatic stall cutoff
needs agreed semantics and a user-approved threshold. If useful progress requires
an external decision/capability, or no useful safe approach is available, report
BLOCKED/INCOMPLETE with evidence rather than claim success. Preserve the best-supported
checkpoint, open findings and next authorized action on interruption or budget exit.

If review belongs to a later stage, return REVIEW PENDING for that stage; do not
launch it or review your own work. Context separation is not statistical independence
of errors; a different model/provider or role label proves neither. Record actual
separation/capability; unavailable independent review remains unverified.

A local loop return never adds a stop cause for live peers. They retain the
[coordination working loop](../../policies/multi-agent-coordination.md). Delegates
remain parent-managed under the [workflow](../multi-agent-workflow/SKILL.md).
