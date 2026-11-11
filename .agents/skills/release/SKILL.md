# Skill: Release

Load for release preparation/publication, and before writing a hook, pipeline gate,
or release check.

## Workflow

1. Verify source/config identity.
2. Run required build and verification.
3. Record version and format/schema identities.
4. Generate deterministic manifest/hashes.
5. Verify consumer compatibility and rejection behavior.
6. Verify atomic publication/rollback path.
7. Distinguish "release artifact built" from "publication authorized".
8. Publish/deploy only with explicit authorization.

## Hooks, gates, and release checks

Before writing one:

1. Ask how the user branches, merges (merge, squash, rebase), versions, and
   releases; record it in `PROJECT.md`.
2. Trace one full cycle of that workflow (commit, review, merge, release) through
   every new check, including a case that must fail.
3. A check not run where it will run is UNTESTED: say so and give the removal step.
4. Keep scripts short, readable, and free of new dependencies.
