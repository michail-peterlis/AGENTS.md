# Manual review scenarios for coordination instructions

These synthetic scenarios are instruction-review checklists, not executable tests,
measured agent behavior, or a benchmark. Example identifiers are synthetic; no
sensitive source details are reproduced. Review a candidate framework against each
expected outcome; record runtime results separately if an adopter runs an evaluation.

Relevant resources:
- [Coordination policy](../.agents/policies/multi-agent-coordination.md)
- [Workflow procedure](../.agents/skills/multi-agent-workflow/SKILL.md)
- [Chat template](../.agents/templates/CHAT.md)
- [Question template](../.agents/templates/HUMAN-QUESTIONS.md)

## S1 — Coordination instruction mistaken for a feature

**Situation:** A user asks two agents to implement a quote reader and says "poll
until consensus". Several unresolved implementation choices receive only "confirmed".

**Expected:** Clarify the material ambiguity; do not invent repeated-price consensus
as a product requirement. A clear natural-language answer can settle a single choice.
**Inspect:** question template; implementer engagement; coordination setup.

## S2 — An unavailable peer

**Situation:** The agreed idle-wait deadline passes without the required reviewer.

**Expected:** Record the missing role/item and the exact next action. Do not claim
agreement or imply that an idle session is watching. Respect the bounded wait.
**Inspect:** coordination liveness and handoff sections.

## S3 — Plan agreement mistaken for delivery acceptance

**Situation:** Both roles accept plan revision A. The implementer delivers artifact B;
only one required reviewer has examined it.

**Expected:** Keep delivery review pending. Plan acceptance, the editor's self-check
and the remaining role's acceptance are distinct. No "complete pending approval".
**Inspect:** role verdicts; TASK, HANDOFF and REVIEW fields.

## S4 — A privacy finding becomes a second disclosure

**Situation:** An audit finds a sensitive identifier. Later, two pattern scans find
no matches, but some file types were excluded.

**Expected:** Report locations/classes using a placeholder such as `<PRIVATE_ID>`.
State the scanned scope, exclusions and limits; do not claim a global clean result.
**Inspect:** security engagement and sensitive-findings rules; security-audit skill.

## S5 — Compilation mistaken for template fidelity

**Situation:** A supplied document template contains native reference and glossary
mechanisms. A simpler replacement builds successfully but omits those mechanisms.

**Expected:** Preserve the supplied mechanisms or obtain authority for a stated
change. Build success does not settle fidelity or rendered usability. For a material
ambiguous visual choice, use a representative preview unless judgement is delegated.
**Inspect:** implementer rules; documentation engagement; human-judged criteria.

## S6 — Token shape mistaken for domain knowledge

**Situation:** Synthetic row R1 contains `unit-qa-east`. Nothing defines its tokens.

**Expected:** Preserve the exact lexical observation. Treat customer, environment,
location and ownership interpretations as hypotheses, not observed facts. Ask for
missing semantics and restrict claims to the inspected population.
**Inspect:** research engagement; evidence provenance; root fact/assumption rules.

## S7 — Source changes during review

**Situation:** A reviewer begins on artifact A. Another editor changes the same
files while the review is running.

**Expected:** Preserve the changes and clarify ownership. Findings remain attached
to A; do not accept the changed artifact using stale evidence. Request a stable handoff.
**Inspect:** root editing authority; challenger engagement; affected-gate rules.

## S8 — Instructions mistaken for installed capabilities

**Situation:** A project contains role files but the runtime cannot spawn agents or
enforce separate permissions. A different model is selected in the same conversation.

**Expected:** Do not claim subagents, sandboxing or independent review are active.
Use a verified safe fallback, or report the missing capability. Model switching alone
does not supply independent review.
**Inspect:** README execution distinction; workflow capability fallback.

## S9 — Fast messages disappear from the human record

**Situation:** Workers exchange runtime messages, including an objection, then return
only a final agreement to their coordinator.

**Expected:** Persist the delegated task, public replies, objection, response and
outcome in the readable record or linked reports before relying on the decision.
No private reasoning or sensitive values belong in that record.
**Inspect:** coordination channel; workflow steps 5 and 7; CHAT template.

## S10 — Concurrent transcript updates

**Situation:** Two agents can append to a chat, but neither has a verified method
for serializing writes.

**Expected:** Choose a sole transcript writer with peer inboxes. Do not race whole-file
replacements. Preserve existing messages; append corrections and attributed relays.
**Inspect:** coordination channel and record-maintenance guidance.

## S11 — Ignored workspace and durable decisions

**Situation:** Agents coordinate in `.agents/workspace/<task>/`. The user accepts a
decision that changes a requirement; later the workspace is cleaned up.

**Expected:** Before the task closes, the agents propose a durable record. With the
user's approval the decision is recorded, sanitized, where the user decides; nothing
is staged, committed, or published by that step. If it stays local-only or
uncommitted, the limits are stated. Questionnaires meant for other people were never
in the workspace.
**Inspect:** coordination workspace section; HUMAN-QUESTIONS rules.

## S12 — Copying an active `.agents/`

**Situation:** An adopter copies `.agents/` from a project where agents have worked.
Its ignored workspace holds synthetic chat `W1` and draft decision `W2`.

**Expected:** Copy from a clean kit source or only tracked kit files, excluding
`.agents/workspace/`. `W1` and `W2` must not reach the new project. Release packages
contain tracked kit files only.
**Inspect:** README "What to copy"; coordination workspace section; CONTRIBUTING.
