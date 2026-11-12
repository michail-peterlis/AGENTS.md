# Policy: Repository Safety

Before broad changes:

- inspect working-tree state;
- identify unrelated modifications;
- identify generated/vendor boundaries;
- identify active editor ownership.

During changes:

- preserve unrelated work;
- avoid destructive reset/rewrite;
- keep source and generated artifacts separate;
- preserve frozen evidence;
- do not remove historical failures merely because a fix now passes.

If concurrent edits are detected, stop on the conflicting files and coordinate ownership.

## What is already there

- Existing hooks, pipeline steps, version bumps, link or workspace entries, pinned
  versions, and environment layout are intentional. Do not remove, disable, bypass, or
  "repair" them to make your change pass; report the conflict and ask.
- The remote, the user's toolchain, and sibling directories may be invisible from your
  environment. Report "not visible from here"; say how old a tracking reference is or
  ask the user to fetch. Never reinstall, rebuild, or plan commits on that basis.
- Before deleting or overwriting anything version control cannot restore, list the
  paths and wait for a yes. A request to clean up covers what you list, not more.
- In a project that adopted this kit, `AGENTS.md` and `.agents/` change only on the
  user's direction, except `.agents/workspace/` and project skills. Project duties go
  in `PROJECT.md`, not in new role files.
