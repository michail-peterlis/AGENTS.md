# Enterprise Agent Governance Kit

A modular `AGENTS.md` framework for multi-agent enterprise software development.

## Design goals

- small universal root;
- progressive disclosure;
- explicit roles;
- least-privilege tool authority;
- directory-scoped instructions;
- task-selective policies and skills;
- measurable acceptance criteria;
- independent verification;
- preserved evidence and provenance;
- honest incomplete/negative results;
- strong production and compatibility boundaries.

## Install

Copy:

- `AGENTS.md`
- `.agents/`

into the repository root.

Optionally adapt `PROJECT.example.md` into project-specific documentation and add
nested `AGENTS.md` files to major components.

## Recommended loading model

An agent typically reads:

1. root `AGENTS.md`;
2. assigned role file;
3. relevant policies;
4. nearest nested `AGENTS.md`;
5. active task/plan;
6. task-specific skill.

Do not preload everything.

## Recommended first customization

1. Fill in repository-wide commands in `AGENTS.md`.
2. Define project context/coordination/completion authority.
3. Add nested `AGENTS.md` files for major components.
4. Delete unused role files rather than forcing agents to read them.
5. Add project-specific skills only when a reusable workflow genuinely exists.

## Origin

This kit consolidates:
- the strongest rules from the supplied multi-agent engineering history;
- the supplied existing `AGENTS.md`;
- contemporary hierarchical AGENTS.md, custom-agent, least-privilege, and
  progressive-disclosure practices.

It intentionally avoids hard-coding project-specific coordination filenames or
polling intervals into the universal root.
