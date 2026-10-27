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

## Harness independence

The framework is written to be portable across agent harnesses. Roles, policies,
skills, and templates state intent and outcomes, not harness tools or features.

- Verify the capabilities your harness actually has. Where a rule relies on one it
  lacks (background watching, permission prompts, question dialogs, subagents, file
  locks), use the stated fallback and say so; if no safe fallback exists, report
  BLOCKED. Fallbacks never bypass safety rules.
- Do not claim isolation or per-agent permission limits (for example, a read-only
  reviewer) unless the harness enforces them and you have verified it.
- Verify that your harness actually loads the root `AGENTS.md`. Some harnesses read a
  differently named instruction file by default; point it at `AGENTS.md` with the
  harness's own import or configuration mechanism instead of copying rules.
- Keep harness-specific notes in the project extension (`PROJECT.md`) or
  compatibility issues, never in roles, policies, skills, or templates.

## Using the kit with your agents

A **role** defines responsibility and authority; a **skill** is a reusable procedure
loaded for a particular task. The adopting project chooses whether its agents run
in one session, separate sessions, or delegated subagents. All use the same scoped
instruction files; this kit does not launch agents, install adapters, or enforce a
sandbox. A different model or context does not by itself make a review independent.

The optional [multi-agent workflow](.agents/skills/multi-agent-workflow/SKILL.md) is a
generic procedure for an adopter's agents, not an orchestration program. Use only
the roles the task needs and verify the chosen execution capabilities.

Keep the discussion in a human-readable file under `.agents/workspace/<task>/`, such as
`chat.md`. Git ignores the folder by default, so conversations do not clutter your
repository; outcomes that must outlast a task get a durable record where you approve.
Runtime messaging may improve delivery speed, but delegated tasks, public replies, objections, decisions
and outcomes must still be recorded in files. Large reports may be linked rather
than copied through every context. See the [CHAT template](.agents/templates/CHAT.md).

Kit skills are generic and optional. Project-specific skills belong in the adopting
repository: when a workflow recurs, create `.agents/skills/<name>/SKILL.md` from
`.agents/templates/SKILL.md` within the project's granted authority. Registering
skills with a harness's own skill mechanism is an optional, project-side step.

Maintainers can use the [manual review scenarios](docs/review-scenarios.md) when
reviewing changes to this kit.

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

1. Copy `AGENTS.md` and `.agents/` into your repository from a release package or a
   clean checkout (see "What to copy"), keeping the `LICENSE` notice with them. If the repository already has an `AGENTS.md`, merge the kit into it
   instead of replacing it; never discard existing project instructions.
2. Fill in the "Project commands" section of `AGENTS.md`.
3. Assign the roles your project uses.
4. Add nested `AGENTS.md` files for major components (see `docs/examples/`).
5. When project context is needed (coordination, completion authority, environment,
   protected paths), create `PROJECT.md` from `.agents/templates/PROJECT.md`.

## What to copy

The easiest way is a release package from GitHub Releases: `agents-kit-vX.Y.Z.zip`, or
`agents-kit-lite-vX.Y.Z.zip`, a condensed edition for models with small context
windows. Each contains only `AGENTS.md` and `.agents/`, with the license notice at
`.agents/LICENSE`; check it against the matching `.sha256` file. Unzip it into an empty
folder, then copy both into your repository, merging `AGENTS.md` if you already have one.

Without a package, copy from a clean checkout of the kit and keep the `LICENSE` notice
with the files; for example, `git archive HEAD AGENTS.md .agents | tar -x -C <target>`
copies only tracked kit files. A plain file copy of any working tree with a populated
`.agents/workspace/`, including this repository's, also copies that workspace; exclude
`.agents/workspace/` when copying.

Either way, nothing in `AGENTS.md` and `.agents/` has to be deleted before use:

- roles, policies, and skills are meant to load only when assigned or needed; what an
  unused one costs depends on the adopting runtime (some index skill descriptions), and
  removing it is optional;
- `.agents/templates/` is not part of the loading order; its templates are used only
  when your project first creates a file such as `PROJECT.md`, a project skill, a task,
  or a review;
- `.agents/.gitignore` makes Git ignore `.agents/workspace/` by default; agents create
  the folder when they first need it, and your repository's `.gitignore` needs no change.

Everything else in this repository maintains the kit and is not copied: `README.md`,
`CONTRIBUTING.md`, `CHANGELOG.md`, `docs/`, `.github/`, `SECURITY.md`, and `.gitignore`.

## Updating the kit

Replace kit files with the new release while keeping your project's own content: the
"Project commands" section of `AGENTS.md`, `PROJECT.md`, nested `AGENTS.md` files,
project skills, and `.agents/workspace/`. To see what changed between versions, compare
the release packages or run `git diff <old-tag> <new-tag> -- AGENTS.md .agents`; never
overwrite files you changed without reviewing the difference.

## Repository layout

```text
enterprise-agents/
├── AGENTS.md          copied into adopting projects
├── .agents/           copied into adopting projects
│   ├── PLANS.md
│   ├── roles/
│   ├── policies/
│   ├── skills/
│   ├── templates/
│   └── .gitignore     ignores workspace/, created on first use
├── docs/              examples and review scenarios for maintainers
├── .github/           release workflow, issue and pull request templates
└── LICENSE            notice kept with copied files
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
