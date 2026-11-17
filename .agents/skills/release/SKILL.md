---
name: release
description: Verifies and publishes a release with identities, manifests and a rollback path. Use for release preparation or publication, and before writing a hook, pipeline gate, or release check.
---

# Skill: Release

Load for release preparation or publication, and before writing a hook, pipeline gate,
or release check.

1. Verify the source and configuration identity; run the required build and checks.
2. Record version and format identities; generate a deterministic manifest and hashes.
3. Verify consumer compatibility, rejection of unsupported input, and an atomic
   publication and rollback path.
4. A built release artifact is not authorization to publish. Publish or deploy only
   with explicit authorization.

Before writing a hook, gate, or release check:

1. Ask how the user branches, merges, versions, and releases; record it in `PROJECT.md`.
2. Trace one full cycle (commit, review, merge, release) through every new check,
   including a case that must fail.
3. A check not run where it will run is UNTESTED: say so and give the removal step.
4. Keep scripts short, readable, and free of new dependencies.
