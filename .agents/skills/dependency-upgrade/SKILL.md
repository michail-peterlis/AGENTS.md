---
name: dependency-upgrade
description: Adds or upgrades a dependency with a stated reason, release-note review and regression tests. Use when adding or upgrading a dependency.
---

# Skill: Dependency Upgrade

Load when adding or upgrading a dependency.

1. State the direct reason for the change.
2. Review release notes and breaking changes for the parts you actually use; check
   security and license constraints where required.
3. Update the authoritative declaration and lock file. No unrelated bulk upgrades
   unless scoped.
4. Run compatibility and regression tests; record runtime, deployment, or API impact.
