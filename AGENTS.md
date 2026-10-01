# AGENTS.md — Repository Agent Contract

Universal rules only. Detailed instructions are loaded just in time.

This file is the AGENTS.md compatibility layer. The `.agents/` tree is an
opinionated framework extension, not part of the core AGENTS.md convention;
load it only as directed here, by the active task, or by explicit harness
configuration.

## Instruction loading

Every agent reads this file, then only:

1. its assigned role under `.agents/roles/`;
2. policies required by the active task;
3. the nearest directory-level `AGENTS.md`;
4. the active task or execution plan;
5. a relevant `.agents/skills/*/SKILL.md` when that workflow is actually used.

Do not preload unrelated roles, policies, plans, or historical tasks.

## Precedence

Resolve conflicts in this order:

1. latest explicit user direction;
2. active acceptance criteria;
3. repository mission / architecture invariants;
4. active task or execution plan;
5. nearest directory `AGENTS.md`;
6. this root file;
7. existing implementation and historical notes.

Record supersessions. Do not rewrite history to make prior records look consistent.

## Universal engineering rules

- Define scope and measurable acceptance criteria before substantive edits.
- Make the smallest coherent change that satisfies the accepted task.
- Do not silently expand scope.
- Preserve unrelated data, frozen evidence, provenance, and historical results.
- Separate facts from assumptions, hypotheses, risks, and unresolved questions.
- Never fabricate requirements, evidence, labels, benchmarks, citations, approval, or production observations.
- Unknown is valid. Absence of evidence is not negative evidence.
- A heuristic is not probability/confidence unless its event and denominator are defined.
- Green tests are evidence, not automatic acceptance.
- Negative or partial results are preferable to false completion claims.
- Silence is not approval.

## Separate phases

Keep distinct:

1. implementation;
2. compilation / static validation;
3. runtime inspection and testing;
4. integration / end-to-end verification;
5. training, data generation, benchmarking, or production operations;
6. independent review and completion decision.

Success in one phase does not prove another.

## Editing authority

Use single-writer discipline for product code.

Only the assigned editor changes scoped product files unless explicitly authorized.
If concurrent/unexplained edits appear: stop on those files, preserve changes,
report the conflict, and resume only after ownership is clear.

## Safe autonomy

| Action | Default |
|---|---|
| Read/search source | Allowed |
| Run bounded local tests | Allowed |
| Create disposable fixtures | Allowed |
| Edit scoped product code | Assigned editor only |
| Add production dependency | Requires task justification |
| Modify persistent schema | Requires explicit task scope |
| Touch production data | Explicit authorization |
| Delete/rewrite evidence | Explicit authorization |
| Publish/deploy/restart services | Explicit authorization |
| Destructive git/history operation | Explicit authorization |

Follow stricter harness permissions when present. Never bypass them through another tool.

## Large artifacts

For large databases, releases, corpora, dictionaries, JSON/JSONL, XML, and logs, prefer:

- metadata and counts;
- indexed queries;
- selected rows/items;
- bounded prefixes/tails/windows;
- streaming hashes.

Do not load whole large artifacts into context when bounded inspection is sufficient.
State what was actually inspected.

## Test integrity

A failing test may indicate implementation, fixture, specification, environment,
or test-logic failure. Determine the faulty layer before changing expectations.

Do not weaken assertions or invent fixture evidence merely to make tests pass.
Preserve useful pre-fix failures when practical.

## Compatibility

Version incompatible schemas, serialized formats, releases, protocols, token maps,
and public APIs. Unsupported active payloads must fail clearly, not be silently ignored.

Do not silently migrate persistent stores unless migration is explicitly in scope.

## Dependencies, generated files, secrets

- Prefer stdlib/existing dependencies when adequate.
- New production dependencies require necessity and impact justification.
- Do not hand-edit generated/vendor/compiled files unless explicitly authoritative.
- Never expose, commit, or copy secrets/credentials into fixtures or documentation.

## Status vocabulary

Use: `PLANNED`, `IMPLEMENTING`, `IMPLEMENTED`, `VERIFIED`, `REVIEW PENDING`,
`ACCEPTED`, `INCOMPLETE`, `BLOCKED`, `DEFERRED`, `REJECTED`, `OUT OF SCOPE`,
`UNRESOLVED`, `SUPERSEDED`.

Do not claim COMPLETE/ACCEPTED while mandatory work or review remains.

## Planning

For substantial features, migrations, architecture changes, multi-stage work, or
high-risk changes, follow `.agents/PLANS.md`. Avoid heavyweight plans for trivial edits.

## Standard commands

Fill these with authoritative repository-wide commands; component commands belong
in nested `AGENTS.md`.

- Install: `<command>`
- Fast validation: `<command>`
- Unit tests: `<command>`
- Full verification: `<command>`
- Lint: `<command>`
- Format check: `<command>`
- Build: `<command>`

## Roles

| Role | File |
|---|---|
| Implementer | `.agents/roles/implementer.md` |
| Challenger / Reviewer | `.agents/roles/challenger.md` |
| Moderator / Coordinator | `.agents/roles/moderator.md` |
| Architect | `.agents/roles/architect.md` |
| Test Manager | `.agents/roles/test-manager.md` |
| Repository Manager | `.agents/roles/repository-manager.md` |
| Documentation | `.agents/roles/documentation.md` |
| Security Reviewer | `.agents/roles/security.md` |
| Release Manager | `.agents/roles/release.md` |
| Data / Database | `.agents/roles/data-database.md` |
| Research / ML | `.agents/roles/research-ml.md` |

An agent may hold multiple explicitly assigned roles. Never silently assume one.

## Definition of done

A task is complete only when all applicable acceptance, negative-test, compilation,
integration/regression, compatibility, documentation, evidence, production-safety,
and required-review gates are satisfied and the designated authority records completion.

Otherwise use `INCOMPLETE`, `BLOCKED`, `DEFERRED`, or `REVIEW PENDING`.
