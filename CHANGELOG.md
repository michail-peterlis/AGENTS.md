# Changelog

All notable public changes to Enterprise Agents are documented here.

This project uses semantic versioning for the governance contract. Behavioral changes may be breaking even when they are Markdown/configuration-only.

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
