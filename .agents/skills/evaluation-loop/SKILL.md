# Skill: Evaluation Loop

Load to evaluate an artifact or correct it after a failed review, at any tier. This is
the normal build, evaluate, revise discipline: no separate mode, no permission gate,
no extra round after a first-pass success.

1. Before the first pass, fix an inspectable standard proportionate to the tier
   (specification, executable checks, or reference artifact). Change it explicitly;
   never lower the bar silently.
2. Build or revise within your ownership. Keep the last supported checkpoint with its
   criterion results; a partial checkpoint is not verified, and keeping one authorizes
   no reset, deletion, or rollback.
3. Run cheap executable checks first. Classify a failure (product, fixture,
   specification, environment) before acting. A failing required check blocks
   acceptance; preference cannot override it.
4. Where the contract requires independent review, each round uses a fresh, separate
   critic context with neutral inputs only: goal, approved standard, constraints and
   deviations, artifact identity, run instructions; not builder persuasion, history,
   or earlier verdicts. A critic that opens the whole record takes only those inputs,
   treats author claims as REPORTED, and says so if already exposed to history. It
   inspects the actual output, reports each criterion as pass, fail, or insufficient
   evidence, and invents no objections. A comparison may be inconclusive.
5. Record findings as in `.agents/policies/review-and-status.md`; escalate scope
   changes. Unrelated preferences force no further round.
6. Corrections go to the assigned editor; critics gain no write authority. Where
   independent review is required, verify closure independently on the changed
   artifact; the next judgment comes from a fresh critic, not the earlier critic's
   memory. Otherwise re-run the failed checks: a self-check, not independent
   acceptance. Protect verified criteria; report regressions and oscillation, not
   only new passes.
7. Report each round with outputs and next owner through the authorized record;
   reporting grants no publishing rights. Gates stay pending until verified on the
   current identity.

Continuing:

- Honor limits the user, project, or job set. Without one, work continues until the
  standard is met or the user stops it: no invented cap, opt-in, or pause before
  round two. Stay within your granted role, scope, and stage.
- No progress: diagnose and change approach. Neither a round without a new pass nor
  a round count proves a stall; an automatic cutoff needs a user-approved threshold.
- If progress needs an outside decision or capability, or no safe approach is left,
  report `BLOCKED` or `INCOMPLETE` with evidence, never success; keep the
  best-supported checkpoint, open findings, and next authorized action.
- Review that belongs to a later stage: return `REVIEW PENDING`; do not launch it or
  review your own work. A different model, provider, or role label is not
  independence; call unavailable independent review unverified.
- A finished loop is no stop cause for live peers.
