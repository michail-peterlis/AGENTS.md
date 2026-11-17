---
name: database-migration
description: Plans and tests a schema or data migration, including rollback, idempotency and old/new compatibility. Use only when a migration is actually part of the task.
---

# Skill: Database Migration

Load only when a schema or data migration is actually part of the task.

1. Identify the current schema version and the project's migration mechanism.
2. Define forward and rollback behavior, transaction boundaries, idempotency, and the
   compatibility window for old and new readers.
3. Test on disposable fixtures: fresh and populated databases, rollback and failure,
   repeated runs, unsupported versions, and data and reference integrity.
4. Run the required integration and regression tests.
5. Never run against production without explicit production authorization.
