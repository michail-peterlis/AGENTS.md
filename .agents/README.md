# Agent Governance Layout

This directory contains task-selective instructions. The root `AGENTS.md` is the
only file every agent must always read.

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

## Policies

Policies define reusable cross-cutting behavior such as testing, evidence,
production safety, and compatibility.

## Skills

Skills are just-in-time workflows. Load them only when their workflow is actually
being performed.

## Nested AGENTS.md

Use nested `AGENTS.md` files for directory-specific commands, architecture,
constraints, generated-file rules, and test instructions.

The nearest applicable file should be more specific than the root, but must not
silently weaken root safety rules.

## Project-specific coordination

Repository-specific communication mechanisms (for example a particular review file,
issue tracker, PR workflow, or chat transcript) should be documented in a project
extension or nested `AGENTS.md`, not hard-coded into this reusable kit.
