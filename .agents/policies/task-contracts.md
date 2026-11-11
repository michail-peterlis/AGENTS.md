# Policy: Task Contracts

Before planning, state the deliverable in one sentence and check it against the
repository. If a supplied brief and the repository disagree, ask first; the brief is
input until that sentence is confirmed.

Before substantive implementation, record:

- objective;
- authority;
- active files/modules;
- explicitly out-of-scope areas;
- producer/consumer path;
- measurable acceptance criteria;
- negative criteria;
- compatibility/version requirements;
- data/provenance requirements;
- resource bounds;
- production boundaries;
- verification requirements;
- completion authority;
- known unresolved questions.

A task contract should be specific enough that another agent can determine whether
the work is complete without relying on the Implementer's intent.

## Proportionality

Scale the contract to the risk and reversibility of the change, not to the
environment or to words such as "production-ready" in a brief:

- T0 — cosmetic and reversible: state the request and the check in your reply; no files;
- T1 — standard: the fields above, as short as clarity allows;
- T2 — high-risk, persistent, or frozen: full contract; name the artifact under review
  by its identity (`.agents/policies/evidence-and-provenance.md`); agent consensus
  (`.agents/policies/review-and-status.md`).

T0 and T1 contracts can live in the reply. T2 work needs a durable scoped plan; it may
be an existing record (issue, pull request, or the task's workspace chat) rather than a new file. Write
separate plan or task files only for T2, multi-session, or multi-agent work, or when
asked. Keep task records in the project-configured location (see
`PROJECT.md`). Working records may live in `.agents/workspace/`; user-facing
deliverables never go under `.agents/`.

## User directions

- Record each direction verbatim with its scope. A direction applies within its stated
  scope, including an explicitly standing one; without a stated scope, it applies to
  the current task. A permission ("you don't need to X") is not a prohibition.
- A request to explain, discuss, compare, or plan authorizes no product edits.
- Record a project-wide lasting preference or correction in `PROJECT.md` (Standing
  user decisions), in the user's words, in the same turn, and say that you did; in a
  shared task the coordinator writes it. Keep task-scoped directions in the task
  record and link their relay messages; the state summary links, not duplicates,
  directions in force. Redact secrets and mark redactions. If no `PROJECT.md` exists,
  ask whether to create one for a lasting project preference.
- After a context loss, re-read the recorded directions before continuing.
- Quote relayed directions verbatim; label interpretations PROPOSED.
- Mark agent-originated thresholds AGENT-PROPOSED. They never override or filter a
  user choice; state what meeting the user's preference would cost.

## Human-judged criteria

For material, ambiguous visual, layout, tone, or other subjective changes, record the
user's exact words and add a HUMAN-PREVIEW gate: show one representative rendered
sample and record the reply before full implementation, unless the user delegates the
judgement. The gate also covers bulk changes to shipped user-facing assets (examples,
templates, dialogs) and any options, warnings, or screens a fix would add: change one,
show it, then do the rest. Small reversible adjustments need no extra round trip.
Measurable proxies are secondary checks, not substitutes.
Ask questions with `.agents/templates/HUMAN-QUESTIONS.md`.
