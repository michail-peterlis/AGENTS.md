# PROJECT.md — Enterprise Agents

## Purpose

Maintain a comprehensive, adoptable governance kit for disciplined multi-agent
software engineering. The deliverable is reusable Markdown instructions for roles,
policies, skills and workflows—not an agent runtime or orchestration service.

## Structure

- `AGENTS.md`: universal rules and progressive-loading entry point.
- `.agents/roles/`: role responsibilities and boundaries.
- `.agents/policies/`: cross-cutting engineering rules.
- `.agents/skills/`: just-in-time workflows and supporting helpers.
- `.agents/templates/`: reusable project, task, review and handoff records.
- `.agents/workspace/`: task-specific working records, not reusable kit content.
- `docs/`: explanations, examples and review scenarios.
- `tools/`: repository-maintenance tools, not part of the reusable agent kit.
- `tests/`: regression tests for this repository's checker and agent workflow helpers.
- `README.md`: adoption, usage and update instructions.
- `CONTRIBUTING.md`: contribution, validation, versioning and release procedures.

## Design Principles

- Keep the kit harness-independent; do not assume automatic discovery of `.agents/`.
- Keep always-loaded instructions small; load detailed guidance only when relevant.
- Support explicit ownership, independent review, evidence preservation and safe
  production boundaries without imposing unnecessary process on small tasks.
- Keep reusable instructions generic. Use synthetic examples rather than private
  conversation content or adopter-project details.
- Treat behavioral changes to the governance contract as compatibility changes,
  even when the implementation is Markdown-only.

## Maintenance

- Preserve adopter-owned project context, local instructions and task workspaces
  when documenting kit updates.
- Record changes in `CHANGELOG.md` without rewriting released history.
- Existing commit hooks validate shell syntax and Markdown line endings and bump
  the patch version in `VERSION`; follow `CONTRIBUTING.md` for the workflow.
- The `lite` edition is maintained on a separate branch; changes here do not
  automatically update it.

## Standing User Decisions

- ".agents should be clean an only contain agents stuff." — 2026-11-11 — Project-wide:
  keep maintainer tooling and tests outside `.agents/`; retain reusable agent-facing
  instructions and workflow helpers there.
