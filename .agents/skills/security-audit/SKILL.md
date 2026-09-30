# Skill: Security Audit

Load for explicit security review.

## Workflow

1. Define trust boundaries and sensitive assets.
2. Enumerate untrusted inputs and privileged actions.
3. Review authentication/authorization where applicable.
4. Review command/path/SQL/deserialization boundaries.
5. Review secrets/logging.
6. Review dependency and supply-chain changes.
7. Review resource exhaustion and unsafe temporary-file behavior.
8. Reproduce concrete findings minimally.
9. Classify severity/impact without exaggeration.
10. Recommend the smallest correction that preserves required functionality.
