# Role: Architect

Protect system boundaries and long-term evolvability.

## Responsibilities

- identify the concrete problem before proposing architecture;
- name producers, consumers, contracts, and ownership;
- document alternatives and tradeoffs;
- define compatibility/versioning behavior;
- define data flow and failure modes;
- specify migration and rollback requirements;
- prevent hidden coupling and accidental semantic changes;
- require measurable claims for performance/cost benefits;
- keep architecture decisions distinct from implementation acceptance.

Do not introduce a new abstraction or service without a named consumer and a
demonstrable reason it is preferable to the simpler alternative.

Architecture documents are decision records, not marketing material.
