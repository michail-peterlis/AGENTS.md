# Contributing to Enterprise Agents

Thank you for helping improve Enterprise Agents.

This project is an opinionated governance framework built around the `AGENTS.md` convention. Contributions should preserve compatibility with the root AGENTS.md pattern and avoid assuming that every agent platform automatically discovers `.agents/*`.

## Contribution categories

Use one of these categories in issues and pull requests:

- `ROLE` — responsibilities, authority, and limits for a type of agent.
- `POLICY` — reusable cross-cutting engineering rule.
- `SKILL` — just-in-time workflow for a specific task pattern.
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

## Pull requests

A pull request should include:

- the change category;
- the problem being solved;
- why the chosen layer is correct;
- context impact, especially for root `AGENTS.md` changes;
- compatibility impact;
- evidence or examples where useful.

Do not add executable tooling, package dependencies, or release automation unless explicitly discussed and accepted first.

## Issues vs discussions

- Use Discussions for design questions, governance tradeoffs, compatibility experiences, and community examples.
- Use Issues for concrete actionable changes.
- Use Pull Requests for proposed implementation.

## Versioning

Public releases use semantic versioning for the governance contract. Behavioral changes may be breaking even when they are Markdown-only.

Do not rewrite released history or remove provenance for released decisions.
