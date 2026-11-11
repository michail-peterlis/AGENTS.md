# Policy: Evidence and Provenance

Important derived results should be traceable to their origin.

## Scope

This policy applies to designated data, results, observations, frozen evidence, and
releases. Source files, drafts, and build intermediates are not evidence unless
designated.

Prefer version control to redundant copies: do not create `-vN` copies, archive
folders, or copies of the product tree for superseded source, documents, or build
output. Do not reclassify existing designated or frozen evidence as disposable, and
do not delete files on the assumption that version control has captured them.

## Artifact identity

Name what is under review by the cheapest stable identity:

- a commit;
- for uncommitted work, the base revision plus one digest of the diff, given together
  with the one command that printed it; the command must cover new files;
- for a file outside version control, its path plus hash.

Review in place and recompute the digest when the work changes. Do not create
per-revision manifests, hashes of manifests, or per-file hash lists solely for review
bookkeeping. This does not prohibit release/package manifests, dataset lineage, or
integrity hashes required by an accepted contract. Keep a review snapshot only when
the state cannot be named otherwise, and at most one per open review.

## Preserve

Where applicable, preserve:

- source identifier;
- source revision/version;
- source hash;
- record identity;
- configuration;
- producer version;
- transformation version;
- evidence population;
- lineage;
- benchmark/test command;
- output/status.

Distinguish:

- asserted;
- observed;
- inferred;
- predicted;
- reviewed;
- unknown;
- conflicting;
- absent.

Do not merge records whose source evidence differs merely because their normalized
values are equal.

Never rewrite failed or historical evidence to make the current state cleaner.
Supersede it explicitly.

## Recorded values

Take hashes, timestamps, and counts from tool output in the same step that records
them. Correct a posted value by appending a correction, not by editing it.
