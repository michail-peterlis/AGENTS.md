# Changelog

All notable public changes to Enterprise Agents are documented here.

This project uses semantic versioning for the governance contract. Behavioral changes may be breaking even when they are Markdown/configuration-only.

## [v0.1.0] - 2026-10-01

### Added

- Initial public Enterprise Agents governance framework.
- Root `AGENTS.md` compatibility layer with progressive context loading.
- Role, policy, skill, and template structure under `.agents/`.
- Example nested `AGENTS.md` files for backend, database, and ML components.
- Contribution, security, code of conduct, issue template, and pull request template documentation.

### Notes

- `.agents/*` is an opinionated framework extension and is not part of the core AGENTS.md specification.
- No executable tooling or package dependencies are included in this release.
