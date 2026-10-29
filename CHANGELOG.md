# Changelog

All notable public changes to Enterprise Agents are documented here.

This project uses semantic versioning for the governance contract. Behavioral changes may be breaking even when they are Markdown/configuration-only.

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
