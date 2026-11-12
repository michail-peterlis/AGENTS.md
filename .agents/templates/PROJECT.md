# PROJECT.md — <project name>

Project-specific context for agents, loaded by root `AGENTS.md` when present. It adds
specifics and never weakens root safety rules. Project commands live in the "Project
commands" section of `AGENTS.md`.

Lasting project facts and conventions only. Active tasks, participants, channels,
check-ins and status belong in task records, not here.

## Project context

Read only when relevant:

- Mission / architecture: `<path>`
- Current state: `<path>`
- Maturity: `<prototype | pre-release | production>`

## Coordination

Define stable conventions, not a live roster or channel:

- Default transport: `<issue/PR/shared file>`
- Where each task records its channel, ownership and review gates: `<convention>`
- Headless/event-triggered jobs: `<run-context/record convention | none>`; route every
  staged role to `.agents/policies/staged-execution.md` from the repository root,
  not an invented live-peer channel.

Do not create alternative coordination channels without authorization.

## Default completion authority

Project-wide default: `<role or human>`.
Record the actual authority and any authorized exception in each task contract.

## Production boundaries

- Production environment:
- Explicitly protected datasets/services:
- Required human approval:

## Operator environment

Filled in from what the user says, never from an agent's own environment.

- Shell / OS / package manager:
- Sandbox: what is mounted; where version control and real data live:
- Where commands run (inside the agent harness or a separate terminal):
- How code reaches the operator (shared mount, copy, checkout):
- Clipboard / copy-paste available:
- Who commits and pushes:

## Version control workflow

- Branching and merge strategy (merge, squash, rebase):
- Versioning and release steps:
- Hooks and automation to keep as they are:

## Protected paths

- Paths agents must not read or search:

## Standing user decisions

In the user's words, added in the turn they are given.

- "<decision>" — `<date>` — `<scope>`

## Model profiles

- `<model / harness>`: context size, timeouts, supported capabilities; verify required instructions are loaded

## Plans and records

- Coordination workspace: `.agents/workspace/` by default; override: `<path | none>`
- Durable decision records (user-approved location): `<path | none>`
- Location for plans and task records: `<path | none>`
