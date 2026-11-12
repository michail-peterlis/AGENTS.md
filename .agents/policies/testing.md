# Testing

- Map tests to acceptance criteria. Test failure paths.
- Reject vacuous assertions and empty populations. Keep fixtures explicit and bounded.
- Never weaken a test to pass. Correct a faulty assertion or fixture only after finding the wrong layer and checking the approved contract; keep the reproduction.
- Never change a test to encode an assumption the user has not confirmed.
- Parsing, escaping, and serialization changes need adversarial inputs. Where safe, show that new tests fail on the pre-change code.
- Exercise what a person runs or looks at the way that person will; passing tests do not show it is usable.
- Project maturity reduces ceremony, not coverage of security, data integrity, compatibility, and authorization.
- A check, hook, or pipeline you add is tested on the user's real workflow, including a failing case, or labelled UNTESTED.
- Keep static validation separate from runtime tests. Report exactly what ran.
