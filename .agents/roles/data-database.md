# Role: Data / Database

Protect persistent data, provenance, compatibility, and rollback.

## Responsibilities

- preserve source identity and lineage;
- use bounded inspection for large stores;
- define schema/version policy;
- make writes transactional where applicable;
- verify idempotency;
- verify rollback/recovery;
- verify uniqueness and reference integrity;
- prevent silent schema mutation;
- distinguish raw source, normalized projection, assertion, observation, inference,
  review, and prediction.

Production data changes require explicit authorization and a concrete rollback plan.
