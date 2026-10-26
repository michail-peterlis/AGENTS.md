# Agent Governance Layout

This directory contains task-selective instructions. The root `AGENTS.md` is the
only file every agent must always read.

The `.agents/` layout is an opinionated Enterprise Agents extension around the
AGENTS.md convention. Do not assume every agent platform discovers it without
root-file routing or harness configuration.

## Mental model

- **Role** — who am I?
- **Policy** — what cross-cutting rules apply?
- **Skill** — how do I perform a specific occasional workflow?
- **Nested AGENTS.md** — where am I working?
- **Task / plan** — what exactly am I doing now?

## Loading model

Typical Implementer task:

1. `/AGENTS.md`
2. `.agents/roles/implementer.md`
3. relevant policies
4. nearest directory `AGENTS.md`
5. active task or execution plan
6. relevant skill, if any

Do not preload the entire `.agents/` tree.

## Roles

Role files define responsibilities and authority, not repository architecture.

## Instructions and execution

This kit supplies instructions for the agents an adopting project already uses; it
does not run agents or enforce permissions. Roles and skills apply the same way whether
agents run in one session, separate sessions, or delegated subagents. A different model
or context does not by itself make a review independent.

## Policies

Policies define reusable cross-cutting behavior such as testing, evidence,
production safety, and compatibility.

## Skills

Skills are just-in-time workflows. Load them only when their workflow is actually
being performed.

The kit ships generic, project-independent skills; all are optional. Project-specific
skills belong in the adopting repository: when a workflow recurs, create
`.agents/skills/<name>/SKILL.md` from `.agents/templates/SKILL.md` within the
project's granted authority. Registering skills with a harness's own skill mechanism
is an optional, project-side step.

## Nested AGENTS.md

Use nested `AGENTS.md` files for directory-specific commands, architecture,
constraints, generated-file rules, and test instructions.

The nearest applicable file should be more specific than the root, but must not
silently weaken root safety rules.

## Multi-agent work

When more than one agent works the same task, load
`.agents/policies/multi-agent-coordination.md`. Ask the user questions with
`.agents/templates/HUMAN-QUESTIONS.md`.

For staged delegation, use the [workflow skill](skills/multi-agent-workflow/SKILL.md).
Keep delegated tasks, public responses, objections and outcomes in files under
`.agents/workspace/<task>/`, which Git ignores by default, even if messages travel by
another mechanism. Outcomes that must outlast the task get a durable record where the
user approves. The [CHAT template](templates/CHAT.md)
is a starting layout, not an extra ledger to duplicate current state.

## Project-specific coordination

Repository-specific communication mechanisms (for example a particular review file,
issue tracker, PR workflow, or chat transcript) should be documented in `PROJECT.md`
(created from `.agents/templates/PROJECT.md`) or a nested `AGENTS.md`, not hard-coded
into this reusable kit.
