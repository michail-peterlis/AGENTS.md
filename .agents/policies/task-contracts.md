# Task contracts

State the deliverable in one sentence and check it against the repository; if the brief and the repository disagree, ask first.

Before substantive work, record: objective, authority, scope in/out, acceptance and negative criteria, compatibility, resource bounds, verification, completion authority, open questions.

- Set the standard and the evidence each criterion needs before the first pass. Change an approved standard explicitly, never silently. Rework after a failed evaluation: `.agents/skills/evaluation-loop/SKILL.md`; it widens no authority.
- Tiers follow the risk and reversibility of the change, not the environment or words such as "production-ready":
  - T0, cosmetic and reversible: request and check in the reply.
  - T1, standard: the fields above, brief.
  - T2, high-risk, persistent, or frozen: durable plan (`.agents/templates/TASK.md` or an existing record), artifact named by its identity, agent consensus (`.agents/policies/review-and-status.md`).

Task records go where `PROJECT.md` says. Working records may go in `.agents/workspace/`. People-facing deliverables never go under `.agents/`.

- Record user directions verbatim with their scope (none stated: the current task); label interpretations PROPOSED. After a context loss, re-read them.
- Record a lasting project-wide preference in `PROJECT.md`, in the user's words, in the same turn, and say so. No `PROJECT.md`: ask whether to create one.
- Label agent-originated thresholds AGENT-PROPOSED; state what meeting the user's preference would cost.
- Material subjective changes (visual, layout, tone), bulk changes to shipped user-facing assets, and options, warnings, or screens a fix would add: change one, show it, and record the reply first, unless the user delegates.
