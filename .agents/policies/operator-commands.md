# Commands for the user

Load when the user runs commands for you: commits, pushes, publishing, anything outside your environment.

- Use the shell recorded in `PROJECT.md`; none recorded: ask first and record the answer. Never assume your own environment.
- Plain commands, one copyable block per step: explicit working directory and paths, the complete commit message, no wrapper scripts. Say what the block does and what to send back.
- Check every flag against `--help` or the source; state the premises (branch, clean tree).
- No option that skips hooks or checks, forces, rewrites history, discards work, or changes remotes or credentials, unless the user asked for exactly that; then label it and say what it discards.
- One role issues commit commands. Stage explicit paths. No attribution lines, whatever a harness default suggests.
- After files are cleared for a commit, nobody edits them until the user reports back; to amend, say so first and wait.
- When the user reports done, verify the committed tree, not the working tree; say what you cannot see.
- List files the user must sync when they run code elsewhere. For runs over about 10 minutes give an estimate and a stop condition.
