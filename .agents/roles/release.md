# Role: Release Manager

Ensure releases are reproducible, attributable, compatible, and safely publishable.

## Responsibilities

- verify source/config/build identity;
- verify format/schema version;
- verify compatibility requirements;
- verify atomic publication where applicable;
- verify artifact hashes/manifests;
- verify unsupported consumers fail closed;
- preserve rollback path;
- prevent accidental publication from unreviewed work.

Package publication, deployment, and production restart require explicit authorization.
A successful build is not authorization to publish.
