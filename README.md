# Enterprise Agents

A modular AGENTS.md framework for disciplined multi-agent software engineering.

Coding agents can produce code quickly. Reliable software engineering also requires:

- explicit edit ownership
- scoped acceptance criteria
- independent review
- evidence preservation
- test integrity
- architecture discipline
- production safety
- progressive context loading

Enterprise Agents is an opinionated governance framework built around the open `AGENTS.md` convention. It is not a new AGENTS.md standard.

## What this repository provides

```text
AGENTS.md       universal repository rules
.agents/roles/ who the agent is
.agents/policies/
                cross-cutting engineering rules
.agents/skills/
                just-in-time workflows
nested AGENTS.md
                component-specific rules
task/plan       what is being done now
```

The root `AGENTS.md` acts as a router for the framework unless a particular harness provides native support for additional files.

## Compatibility statement

This project uses the open `AGENTS.md` convention for repository-level instructions. The `.agents/roles`, `.agents/policies`, `.agents/skills`, templates, and related structure are an opinionated extension provided by this framework and are not part of the core AGENTS.md specification.

Do not assume every coding-agent implementation automatically discovers `.agents/*`. Agents should load the additional files only when directed by the root `AGENTS.md`, a task, or project-specific harness configuration.

## Core model: progressive context loading

Agents should normally read only:

1. root `AGENTS.md`;
2. assigned role under `.agents/roles/`;
3. policies required by the active task;
4. nearest nested `AGENTS.md`;
5. active task or execution plan;
6. task-specific `.agents/skills/*/SKILL.md` when needed.

Agents must not preload every role, policy, skill, or historical document.

## Quick start

1. Copy `AGENTS.md` and `.agents/` into your repository.
2. Fill in repository-specific build/test commands in `AGENTS.md`.
3. Select the roles your project uses.
4. Add nested `AGENTS.md` files for major components.
5. Customize project coordination and completion authority.

Optional: copy `PROJECT.example.md` into project-specific documentation and adapt the examples under `examples/`.

## Adoption levels

### Minimal

```text
AGENTS.md
```

Use this when you only want core repository rules and compatibility with the AGENTS.md convention.

### Standard

```text
AGENTS.md
.agents/roles/
.agents/policies/
```

Recommended default for teams that want explicit responsibilities and reusable engineering guardrails.

### Full

```text
AGENTS.md
.agents/
examples/
templates/
plans
skills
```

Use this when you want the complete governance framework, reusable workflows, templates, and examples.

## Repository layout

```text
enterprise-agents/
├── AGENTS.md
├── .agents/
│   ├── README.md
│   ├── PLANS.md
│   ├── roles/
│   ├── policies/
│   ├── skills/
│   └── templates/
├── examples/
├── PROJECT.example.md
└── MANIFEST.json
```

## Contribution architecture

The root `AGENTS.md` has a context budget. New rules must justify why every agent should always load them.

Default placement:

```text
Universal invariant       → AGENTS.md
Role responsibility       → .agents/roles/
Cross-cutting rule        → .agents/policies/
Occasional workflow       → .agents/skills/
Component-specific rule   → nested AGENTS.md
One task                  → task/plan
```

This prevents the root file from growing back into a large governance manual.

## Positioning

Enterprise Agents is a modular engineering-governance framework for coding agents, derived from practical multi-agent development workflows where implementation and adversarial review were deliberately separated.

Important characteristics include:

- single-writer ownership;
- measurable acceptance contracts;
- adversarial/independent review;
- evidence preservation;
- no consensus by silence;
- honest negative/incomplete results;
- version/compatibility discipline;
- least privilege;
- bounded large-data inspection;
- progressive context disclosure.

## Community

Use GitHub Discussions for design/community questions and Issues for concrete actionable changes. Suggested discussion categories are Ideas, Questions, Governance Design, Agent Compatibility, and Show and Tell.

See `CONTRIBUTING.md` for contribution guidance and proposal expectations.

## License

MIT License. See `LICENSE`.
