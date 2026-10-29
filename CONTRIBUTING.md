# Contributing to Enterprise Agents

Thank you for helping improve Enterprise Agents.

This project is an opinionated governance framework built around the `AGENTS.md` convention. Contributions should preserve compatibility with the root AGENTS.md pattern and avoid assuming that every agent platform automatically discovers `.agents/*`.

## Contribution categories

Use one of these categories in issues and pull requests:

- `ROLE` — responsibilities, authority, and limits for a type of agent.
- `POLICY` — reusable cross-cutting engineering rule.
- `SKILL` — just-in-time workflow for a specific task pattern; must be project-independent.
- `TEMPLATE` — reusable task, review, handoff, or nested-instruction template.
- `COMPAT` — compatibility notes for agent platforms or harnesses.
- `DOC` — documentation-only improvement.
- `BUG` — contradiction, ambiguity, broken link, or incorrect rule.

## Proposal questions

Every nontrivial proposal should answer:

1. What problem does this solve?
2. Why should this be reusable across projects?
3. Why does it belong at this layer?
4. What existing rule overlaps with it?
5. Does it increase always-loaded context?
6. What failure or undesirable behavior does it prevent?
7. Is this tool-independent or specific to a particular agent platform?

## Root context budget

The root `AGENTS.md` has a context budget. New root rules must justify why every agent should always load them.

Default placement:

```text
Universal invariant       → AGENTS.md
Role responsibility       → .agents/roles/
Cross-cutting rule        → .agents/policies/
Occasional workflow       → .agents/skills/
Component-specific rule   → nested AGENTS.md
One task                  → task/plan
```

Prefer adding or refining role, policy, skill, template, or nested instructions instead of expanding the root file.

## Harness independence

Roles, policies, skills, and templates must not name or depend on a specific agent
harness, model, or tool. State the required outcome and a fallback for harnesses that
lack the capability. Harness-specific notes belong in `COMPAT` issues or project
extensions.

When changing coordination, review, or privacy rules, re-check the
[manual review scenarios](docs/review-scenarios.md).

## Pull requests

A pull request should include:

- the change category;
- the problem being solved;
- why the chosen layer is correct;
- context impact, especially for root `AGENTS.md` changes;
- compatibility impact;
- evidence or examples where useful;
- a substantive addition to `CHANGELOG.md` for every pull request targeting `main`, normally under `[Unreleased]`; the PR workflow checks for added non-whitespace text, not its heading.

Repository automation includes the workflows in `.github/workflows/` and the optional local pre-commit hook (`.githooks/pre-commit`). Do not add other tooling, scripts, or package dependencies unless explicitly discussed and accepted first.

To enable local shell validation and automatic patch-version incrementing on each commit:

```sh
git config core.hooksPath .githooks
```

The hook validates shell scripts, ensures staged Markdown files do not contain CRLF line endings, and increments the patch version in `VERSION` upon each commit execution. Note that `VERSION` is updated locally by this hook; the Release workflow automatically defaults to releasing `v<VERSION>` from this file if no manual version override is provided on dispatch. Concurrent branches that commit will each bump their local `VERSION`.

## Issues vs discussions

- Use Discussions for design questions, governance tradeoffs, compatibility experiences, and community examples.
- Use Issues for concrete actionable changes.
- Use Pull Requests for proposed implementation.

## Versioning

Public releases use semantic versioning for the governance contract. Behavioral changes may be breaking even when they are Markdown-only.

Do not rewrite released history or remove provenance for released decisions.

Release packages contain tracked kit files only; never include `.agents/workspace/`
content.

## Releases

Releases are built by the manually started **Release** workflow, run from `main`. It
packages the committed `AGENTS.md` and `.agents/` of one commit with `git archive`,
adds the license notice as `.agents/LICENSE`, and attaches a `.sha256` file.

1. Move the `[Unreleased]` entries in `CHANGELOG.md` under `## [vX.Y.Z] - YYYY-MM-DD`
   and push to `main`.
2. Ensure the `lite` branch contains the edition you want to release.
3. Run the Release workflow with `version: vX.Y.Z` (or leave empty to automatically release `v<VERSION>` from `VERSION`). It creates the tag and the release, and packages both `agents-kit-vX.Y.Z.zip`
   and `agents-kit-lite-vX.Y.Z.zip` together with their `.sha256` files.

### The `lite` branch

`lite` holds only `AGENTS.md` and `.agents/` (including `.agents/.gitignore`),
condensed for small context windows. Condensing may shorten wording and merge files,
but must not drop safety or acceptance rules. End each `lite` commit message with a
`Derived-from: <main commit>` line for provenance. The release workflow packages the checked-out `lite` commit without validating that trailer, main ancestry, or source freshness.

Create `lite` once, without shared history, in its own folder so untracked files of
your `main` checkout cannot be added to it:

```sh
git worktree add --orphan -b lite ../agents-lite
```

Protect `main` with a branch ruleset (Settings → Rules → Rulesets → New branch ruleset,
targeting the default branch) that enables **Require linear history** and **Block
force pushes**. Together with the unrelated histories, this blocks ordinary pull
requests and merge commits from `lite` into `main`. It does not stop copying,
cherry-picking, or squashing `lite` content into `main`, or anyone allowed to bypass
the ruleset.
