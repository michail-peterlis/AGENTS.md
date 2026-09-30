# Policy: Versioning and Compatibility

Version any incompatible persistent or external contract.

Examples:

- database schema;
- serialized payload;
- release format;
- protocol;
- token map;
- public API;
- cache identity when producer semantics change.

Consumers must reject unsupported active payloads explicitly.

Do not:

- silently ignore new semantic fields;
- silently mutate old persistent stores;
- reuse an old format identity for incompatible semantics;
- assume successful parsing means semantic compatibility.

When producer behavior changes but cached results could remain key-identical, bump
the producer/cache identity and preserve old entries rather than deleting them.
