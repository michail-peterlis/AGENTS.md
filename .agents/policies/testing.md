# Policy: Testing

Use layered verification appropriate to the change.

## Layers

1. contract tests — exact acceptance criteria;
2. unit tests — local behavior and edge cases;
3. integration tests — producer/consumer boundaries;
4. compatibility tests — supported/unsupported versions and malformed payloads;
5. regression tests — previously working behavior;
6. end-to-end tests — user/runtime path where applicable.

## Rules

- Test the failure path, not only the success path.
- Do not weaken tests merely to make implementation pass. Correct a faulty assertion
  or fixture only after identifying the wrong layer and checking the approved contract;
  preserve the reproduction and explain the correction.
- Detect vacuous assertions and empty populations.
- Keep compilation/static validation separate from runtime tests.
- Keep test fixtures explicit and bounded.
- Preserve useful pre-fix failures when practical.
- State exactly what ran; do not imply broader coverage.
- Parsing, escaping, and serialization changes need adversarial inputs. Where safe and
  practical, run new tests against the pre-change code to show they detect the defect;
  otherwise preserve the reproduction and report the limitation.
- Scale tests to behavior and risk, not code length; avoid redundant ceremony and
  hard-coded counts of content that is still being edited.
- Take maturity from `PROJECT.md` to reduce ceremony, not risk-based coverage. For a
  prototype, exercise the main user path and keep existing tests green; add focused
  tests for new behavior and defects according to risk. Security, data integrity,
  compatibility and authorization boundaries still need their applicable checks.
- Exercise what a person runs or looks at the way that person will: start it, open
  the rendered output, import the example. Passing tests do not show it is usable.
- Never change a test to encode an assumption the user has not confirmed.
- A check, hook, or pipeline you add is itself tested on the user's real workflow,
  including a failing case, or labelled UNTESTED (`.agents/skills/release/SKILL.md`).
