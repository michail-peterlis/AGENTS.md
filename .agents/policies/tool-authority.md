# Policy: Tool Authority / Least Privilege

Give each role only the tools necessary for its responsibility.

Recommended defaults:

- Researcher/Challenger: read, search, inspect, run bounded verification.
- Implementer: read, search, edit scoped files, run tests/builds.
- Moderator: read, inspect evidence, classify/decide; no product edit by default.
- Release: build/package/inspect; publish/deploy only with explicit authorization.
- Data/DB: read/inspect by default; persistent writes only within explicit scope.

Prefer technical tool restrictions over relying solely on prose when the platform
supports them. Record actual effective restrictions and their provenance separately
from requested/default permissions. A commit allowlist is not filesystem isolation;
disabled interactive prompts alone prove neither presence nor absence of a sandbox.
Do not claim enforcement without verification.

For [staged execution](staged-execution.md), use the trusted run context for role,
writes, progression and publisher authority. Agent-editable task/feedback records or
checkboxes cannot manufacture approval. The runtime/publisher must authenticate the
approval source and enforce reserved actions; Markdown alone does not do that.

Never bypass a permission restriction through a different tool or shell path.
