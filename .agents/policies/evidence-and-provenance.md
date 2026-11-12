# Evidence

- For designated results, keep source, revision, configuration, command, and output.
- Label claims asserted, observed, inferred, unknown, or conflicting.
- Use version control, not `-vN` copies, archive folders, or copies of the product tree. Do not delete files on the assumption that version control has them.
- Artifact identity: a commit; for uncommitted work, the base revision plus one digest of the diff with the one command that printed it (it must cover new files); for a file outside version control, path plus hash. Recompute when the work changes. No per-file hash lists or manifests just for review; those a contract requires stay.
- A verdict binds the artifact scope and revision, the approved standard, and the verification inputs (commands, dependencies, configuration, environment). Do not narrow the scope to convenient files.
- Changed criteria, permissions, commands, references, dependencies, or environment can make evidence stale without a source edit: reassess the affected gates. A report-only commit or branch movement does not; name the evaluated revision.
- Never rewrite failed or historical evidence; supersede it. Correct records by appending.
