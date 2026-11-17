---
name: security-audit
description: Reviews trust boundaries, untrusted inputs, secrets and dependencies, and reports findings without exposing sensitive values. Use for an explicit security review.
---

# Skill: Security Audit

Load for an explicit security review.

1. Define trust boundaries and sensitive assets; list untrusted inputs and privileged
   actions.
2. Triage untrusted or suspect code statically first. Build, test, install, or run it
   only with explicit authorization and isolation.
3. Review authentication and authorization; command, path, SQL, and deserialization
   boundaries; secrets and logging; dependency and supply-chain changes; resource
   exhaustion and unsafe temporary files.
4. Reproduce concrete findings minimally; never reproduce resource exhaustion at real
   scale.
5. Classify severity and impact without exaggeration. Report sensitive findings by
   location and class; never repeat the sensitive value.
6. Recommend the smallest fix that keeps required behavior, with safe defaults in code
   first. An option, warning, or screen a fix would add is user-visible: list it and
   preview one representative case with the user before applying it everywhere.
