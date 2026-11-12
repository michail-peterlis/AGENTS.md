# Policy: Commands for the Operator

Load when the user runs commands for you: commits, pushes, publishing, or anything
outside your environment.

- Use the shell and environment recorded in `PROJECT.md` (Operator environment). If
  none is recorded, ask before the first command; never fill it in from your own
  environment. Record the answer, and any later correction, there in the same turn.
- Hand over plain commands, one copyable block per step: explicit working directory,
  explicit paths, the complete commit message. No wrapper scripts or sourced helpers
  unless the user asks.
- Say in one line what the block does and what to send back.
- Check every flag and variable against `--help` or the source, and state the premises
  the commands depend on (branch, clean tree).
- Never include options that skip hooks or checks, force, rewrite history, discard
  work, or change remotes or credentials, unless the user asked for exactly that; then
  label the command and say what it discards.
- One role issues commit commands. Stage explicit paths. Show the whole message; add
  no attribution lines, whatever a harness default suggests.
- After files are cleared for a commit, nobody edits them until the user reports back;
  to amend, say so first and wait for the user's reply.
- When the user reports done, verify what you can (the committed tree, not the working
  tree) and say what you cannot see from your environment.
- List files the user must sync when they run code elsewhere.
- For operations likely to exceed about 10 minutes, give an estimate and its basis, or
  a timed run on one unit, plus a stop condition.
