# Changelog

All notable public changes to Enterprise Agents are documented here.

This project uses semantic versioning for the governance contract. Behavioral changes may be breaking even when they are Markdown/configuration-only.

## [Unreleased]

### Added

- Repository-local `tools/check_kit.py` and stdlib-only regression tests in `tests/`: run `python3 -B -I tools/check_kit.py` for Markdown references, policy routing, line endings, shell syntax, channel-helper failure paths and concurrency. Maintainer tooling stays outside the reusable `.agents/` kit; instructions live in `CONTRIBUTING.md`. No CI or hooks are changed.
- `.agents/templates/LAUNCH.md`: start prompt the coordinator writes for each session.
- `.agents/templates/STATE.md`: one state file per task (roster, user directions in force, what waits on the user, items) that answers "status" and is the checkpoint for pause, resume, and takeover.
- `.agents/policies/operator-commands.md`: how to hand commands to a user who commits or runs things outside the agent's environment. It replaces the implementer's "Commands for the operator" list.
- `.agents/skills/multi-agent-workflow/scripts/read.sh`: prints the complete lines of the channel not yet seen, and the two values the next read and wait need.
- Root `AGENTS.md`: the coordination policy applies to peer sessions sharing a channel, not to subagents a session starts itself; stay in the working loop; re-read role, task record, and directions after a context loss; a request to explain, discuss, or plan authorizes no product edits; no abstraction, file, option, or document without a named need; designs are proposals until accepted; short plain reports. Explicit authorization is now required to delete files version control cannot restore, to bypass project hooks or checks, and to change kit files.
- Close-out step in `completion.md`; "Artifact identity" in `evidence-and-provenance.md`; "What is already there" in `repository-safety.md`; "Hooks, gates, and release checks" in the release skill; maturity, version-control workflow, and "who commits" fields in the PROJECT template.
- README: running several sessions on one task; several repositories in one folder.
- `docs/review-scenarios.md`: scenarios S13–S27.

### Changed

- `.agents/policies/multi-agent-coordination.md` rewritten around a working loop: act, use the gap, wait with backoff (about 15 seconds to 5 minutes), read what is new. Waiting has no default limit; a timeout, a silent or blocking peer, or agreement on one item is not a reason to stop. Stop causes are a closed list: STOP from the coordinator, the user (directly or relayed), something only the user can give, or a failing channel. One shared chat, appended through the helper; the sole-writer arrangement remains only as the fallback without a shell. Each agent posts its own check-in and pause note; the roster is copied from check-ins. Agreement is reported as gate, scope, reviewer session/role, and verdict message ID; channel discovery requires a confirmed task, not the newest file. T0 and T1 items get one author, one reviewer, and a short verdict.
- `review-and-status.md`: artifact authors are identified by session, across roles; agent consensus requires ACCEPT on every assigned independent review gate, with specialist scopes and no empty consensus or role-switched self-review.
- Artifact identity is a commit, or the base revision plus one digest of the diff with the command that printed it; no staged tree copies or redundant review manifests. Required release/package manifests and data-integrity hashes remain supported.
- Templates: CHAT has a lighter header (name, ID, time), no participants block, and values filled by command substitution; TASK drops the idle-wait budget and the participants line; REVIEW and HANDOFF gain "Exercised as a user" and "User-visible changes"; PROJECT holds lasting project facts and conventions only, with no active-task pointer; HUMAN-QUESTIONS puts the recommended option first. The task owns the contract and scoped directions, the channel preserves events and decisions, and STATE is a derived current index rather than a competing authority.
- `task-contracts.md`: the deliverable is stated in one sentence and checked against the repository; tiers follow the change, not the environment; T2 asks for agent consensus instead of agreement of all assigned roles; lasting user preferences are recorded in `PROJECT.md` in the same turn; the HUMAN-PREVIEW gate covers bulk changes to shipped user-facing assets and options a fix would add. `PLANS.md`: prefer an early runnable slice, but allow bounded contract, migration and security prerequisites within the authorized task.
- `testing.md`: maturity reduces ceremony, not risk-based coverage; faulty assertions can be corrected against the approved contract, never merely weakened to pass. Reviewer command validation uses authorized environments, dry runs or source inspection without executing restricted operations just to check instructions; required unverified runtime gates remain pending. Added checks are tested on the real workflow or labelled UNTESTED.
- Roles: moderator (start prompts, relays edits to the assigned editor, status from the state file, takeover; its adjudication order and completion checks now point to the root file and `completion.md`), challenger (exercises the deliverable as its user, visual evidence; finding classes now point to `review-and-status.md`), implementer, security, repository-manager, release, architect, documentation.
- Skills: the workflow skill separates peers from delegates, gives the loop commands, and requires delegate briefs to carry the working directory, the only writable paths, and resource limits, with the tree checked after a delegate returns; the security-audit skill puts safe defaults in code first.
- Helpers: `wait.sh` accepts the one-token checksum printed by `read.sh` as well as quoted `cksum` output, and rejects a malformed checksum (exit 64); `append.sh` validates its arguments, refuses a missing folder at once, repairs a missing final newline in the channel, and ends each message with a blank line.
- `read.sh` now rejects overflowing cursors and propagates read failures without advancing the cursor; rotation resets are explicit. `append.sh` rejects symlink inputs/channels and hard-linked channels to prevent self-input and lock bypass through aliases. Normal CLI argument order and success output remain unchanged.
- Instruction precedence cannot grant restricted permissions; instructions embedded in task data cannot expand authority. Documentation, experiments, production-safety and tool-authority policies have explicit loading paths from relevant roles and skills.
- Review scenarios S1, S2, and S10 updated for the new waiting and channel rules.

### Removed

- "Wait budget", "bounded wait", and `by <time>` wording, and the statement that an idle session in a turn-based harness needs the user to resume it.
- The stop cause "cannot continue safely", which was used to hand back on a silent peer; a failing channel and a need only the user can meet remain stop causes.
- Reading the channel under the lock or from snapshots, and the rule against inferring completeness from time, size, or checksum; `read.sh` shows complete lines only.
- The two example names in the coordination policy.
- `.gitignore` entry for local analysis inputs.

### Notes

- Derived from an analysis of 106 recorded sessions (66 main, 40 delegated) run with v0.1.0 to v0.3.5 in three agent harnesses.
- Behavioral change for adopters: agents in multi-agent tasks no longer stop on a wait timeout or a silent peer; coordination records change shape (`STATE.md`, lighter chat header); verdicts no longer call for hash manifests.
- The helpers were exercised with one shell acting as `sh`; other POSIX shells were not tested.

## [v0.3.5] - 2026-10-29

### Removed

- Release workflow: removed the `lite` provenance, main-ancestry, and source-freshness gate. Both editions are still packaged, and their commit identities remain in the release notes.

## [v0.3.3] - 2026-10-29

### Added

- Release workflow (`.github/workflows/release.yml`): automatically defaults to releasing `v<VERSION>` from `VERSION` if manual dispatch version input is left empty.
- PR validation workflow (`.github/workflows/validate-pr.yml`): uses explicit PR base and head commit SHAs from event payload and portable whitespace matching.

### Changed

- Release workflow (`.github/workflows/release.yml`): trailer parser tolerates leading whitespace for `Derived-from:` trailers.

## [v0.3.2] - 2026-10-29

### Added

- PR validation workflow (`.github/workflows/validate-pr.yml`): validates substantive `CHANGELOG.md` additions and checks shell script syntax for pull requests targeting `main`.
- Native patch-only version bumping hook (`.githooks/pre-commit`) and root `VERSION` file, with canonical SemVer 2.0 validation, dirty working tree protection, and per-commit-execution patch incrementing.
- Updated `CONTRIBUTING.md` with pull request changelog requirements, hook installation instructions, and release workflow updates.

### Changed

- Release workflow (`.github/workflows/release.yml`): releases are now strictly dual-edition, packaging both `agents-kit-$VERSION` and `agents-kit-lite-$VERSION` together; requires a `lite` `Derived-from` trailer naming a `main` ancestor whose `AGENTS.md`/`.agents/` tree matches the released `main` commit; fails when the versioned changelog section is missing (no fallback).

### Removed

- Release workflow (`.github/workflows/release.yml`): removed the `source` manual dispatch input (`main` vs `lite`).


## [v0.3.0] - 2026-10-28

### Added

- Root `AGENTS.md` Instruction Loading item 7 enforces out-of-the-box playful name selection and channel check-in before other work.
- In-turn bounded polling protocol and moderator consensus closure rule in `.agents/policies/multi-agent-coordination.md`.
- File-based coordination helpers under `.agents/skills/multi-agent-workflow/scripts/`:
  - `wait.sh`: POSIX `sh` bounded checksum waiter with canonical decimal validation and dynamic sleep.
  - `append.sh`: POSIX `sh` atomic directory-lock appender with ~30s timeout and automatic trap cleanup.
- Explicit `- **Writes:**` (assigned file paths) and `- **Does not:**` (boundaries/non-goals) sections in all 11 role files under `.agents/roles/*.md`.

### Changed

- Compressed root `AGENTS.md` from 187 to 84 lines (-55%) while retaining all 17 universal engineering rules, safe-autonomy permission table, precedence order, project commands, and
Definition of Done gates.
- Refined multi-agent liveness and completeness requirements in `.agents/policies/multi-agent-coordination.md` to require awaited roles to return a verdict before handoff and enforce
shared-lock message snapshots.
- Updated `.agents/skills/multi-agent-workflow/SKILL.md` with instructions and usage examples for `scripts/wait.sh` and `scripts/append.sh`.

### Notes

- Fully backward-compatible with v0.2.0 task templates and policies.
- Resolves passive agent stall in turn-based runtimes without requiring external background daemons or IPC infrastructure.


## [v0.2.0] - 2026-10-27

### Added

- `.agents/policies/multi-agent-coordination.md`: coordinator and completion authority, append-only human-readable channel, relayed human directions, agent consensus, liveness, and handoff status.
- `.agents/skills/multi-agent-workflow/SKILL.md`: optional generic procedure for delegation and independent review.
- Templates: `HUMAN-QUESTIONS.md`, `CHAT.md`, `SKILL.md` for project-specific skills, and `PROJECT.md` (replaces `PROJECT.example.md`).
- Root rules on scaling process to risk, scope of user directions, agent-proposed thresholds, tool-sourced values, and disputed facts; safe-autonomy rows for untrusted code and access outside the workspace.
- Root loads the optional project extension `PROJECT.md` when present; it cannot weaken root safety rules.
- README guidance on harness independence, using the kit with existing agents, what to copy, merging into an existing `AGENTS.md`, and updating the kit.
- `docs/review-scenarios.md`: manual review scenarios for maintainers.
- `.agents/workspace/` for local coordination records, kept out of version control by `.agents/.gitignore` and created on first use; outcomes that must outlast a task get a tracked record with the user's approval.
- `.gitignore` for local analysis inputs.
- Root rule against agent, model, or vendor attribution in commits, pull requests, and other published text; an agent with a git identity assigned by the project may appear only in git metadata, as that identity.
- Playful agent names as speaker labels in multi-agent coordination messages.
- Release workflow (`.github/workflows/release.yml`): packages the committed `AGENTS.md` and `.agents/` of one commit plus the license notice, with a `.sha256` file; an optional minimal edition is packaged from the `lite` branch, and CONTRIBUTING describes a `main` ruleset to set up against merging it.

### Changed

- Reviewer evidence tagging (OBSERVED/REPORTED) and acceptance requirements in `challenger.md` and `REVIEW.md`.
- Contract tiers (T0–T2), user-direction scope, and a HUMAN-PREVIEW gate in `task-contracts.md` and `PLANS.md`.
- Evidence policy scoped to designated data and results; prefer version control over redundant copies.
- Engagement sections for all roles; added duties for implementer, architect, moderator, repository-manager, security, and documentation; testing, versioning, completion, and review-and-status policies.
- TASK, HANDOFF, and REVIEW templates gain tier, stage, artifact identity, ownership, and pending-decision fields.
- Root "Standard commands" is now "Project commands", owned by the adopting project and kept across kit updates.
- Wording specific to the framework's original project generalized in root `AGENTS.md`, `PLANS.md`, and the evidence, versioning, data, and research files.
- README adoption levels replaced by one copy set; `examples/` moved to `docs/examples/`.
- Coordination policy, CHAT and HUMAN-QUESTIONS templates, PROJECT template, and README point coordination files to `.agents/workspace/`.
- `CONTRIBUTING.md`: harness independence, project-independent skills, review scenarios, workspace exclusion from releases, and the release process with `lite` branch conventions and the `main` ruleset.
- README: release packages and project-skill guidance.

### Removed

- `PROJECT.example.md` (now `.agents/templates/PROJECT.md`).
- `MANIFEST.json`; Git history identifies file contents, and release checksums belong with release packages.
- `CODE_OF_CONDUCT.md`.
- `.agents/README.md`; its guidance is in `README.md` and the policy files.

### Notes

- Derived from an analysis of multi-agent and single-agent sessions run with v0.1.0.
- Breaking for v0.1.0 adopters: `PROJECT.example.md` and `examples/` moved, the root commands section was renamed, and `MANIFEST.json` was removed.

## [v0.1.0] - 2026-10-01

### Added

- Initial public Enterprise Agents governance framework.
- Root `AGENTS.md` compatibility layer with progressive context loading.
- Role, policy, skill, and template structure under `.agents/`.
- Example nested `AGENTS.md` files for backend, database, and ML components.
- Contribution, security, code of conduct, issue template, and pull request template documentation.

### Notes

- `.agents/*` is an opinionated framework extension and is not part of the core AGENTS.md specification.
- No executable tooling or package dependencies are included in this release.
