# AGENTS.md — Backend Example

Applies to this example backend directory.

## Commands
- Unit tests: `<backend test command>`
- Integration tests: `<backend integration command>`

## Rules
- Preserve public API compatibility unless the task explicitly versions the API.
- New endpoints require request validation and negative tests.
- Database changes must load `.agents/skills/database-migration/SKILL.md`.
- Do not place secrets in configuration examples.
