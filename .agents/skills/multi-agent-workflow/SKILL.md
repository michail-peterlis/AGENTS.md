# Skill: Multi-Agent Workflow

Use for a task that benefits from delegation or independent review. A procedure, not
an orchestrator or an installed integration.

*Peers* are separate sessions the user starts; they share a channel under the
[coordination policy](../../policies/multi-agent-coordination.md). *Delegates* are
subagents your session starts and collects; they need no channel, names, or check-in.
Asked to work with peers, do not spawn delegates instead. Headless jobs use
[staged execution](../../policies/staged-execution.md); evaluation and rework use
the [evaluation loop](../evaluation-loop/SKILL.md).

## Procedure

1. Establish the task contract, participants, and completion authority. Use only the
   roles the task needs: often one implementer and one independent reviewer.
2. Brief each participant in the record before dispatch: role, objective, sources,
   artifact identity, verification, return format, working directory, and the only
   paths it may write. Relevant context only. For a review, give the question and
   sources, not the answer you expect.
3. Record limits the user set; invent no waiting limit. Delegates that build or test
   get concurrency, time, and memory caps. Check what the runtime can really
   delegate, restrict, and cancel. Use the project's permitted models.
4. Run independent read-heavy work in parallel; schedule dependent edits one after
   another under the single-writer rule.
5. When a delegate returns, list what changed outside its paths; its own statement
   about side effects is REPORTED. Record replies and objections before deciding on
   them.
6. Hand off a stable artifact identity; corrections go to the assigned editor, then
   a fresh handoff. Re-check findings you act on. Record authors by session, collect
   ACCEPTs for the required gates on the same identity, and hand off the remaining
   decision with a status and `Next`.

## Channel helpers

POSIX `sh` scripts in `scripts/`; exit 2 means unreadable, 64 bad usage:

- `read.sh <channel> [<seen> | -<last>]` prints the complete new lines, then
  `seen=<lines> sum=<checksum>`. Keep the old cursor on any failure.
- `wait.sh <channel> <sum> [<seconds>]` exits 0 when the channel differs from `<sum>`,
  1 on timeout (default 120 s).
- `append.sh <channel> <message file>` appends one whole message under a lock
  (`<channel>.lock`); exit 1 if the lock stays busy for about 30 s. Regular files
  only: no symlinks, no hard-linked channel.

The loop, from the repository root. Begin every call with the first line: shell
variables may not survive between tool calls.

```sh
W=.agents/workspace/<task>; C=$W/chat.md; H=.agents/skills/multi-agent-workflow/scripts
sh "$H/read.sh" "$C" -60                  # join: last 60 lines, then seen=<n> sum=<s>
# act; write your message to $W/<prefix>-msg.md, then:
sh "$H/append.sh" "$C" "$W/<prefix>-msg.md"
sh "$H/read.sh" "$C" <n>                  # your message and anything posted meanwhile
sh "$H/wait.sh" "$C" <s> 15 >/dev/null    # 0: read from <n>; 1: back off; 2/64: error
```

Back-off and stop causes are in the policy. Keep each wait below your tool's timeout.
On an announced channel rotation, switch to the new path and reset `seen` to 0.

## Capability fallback

Without subagents, use separate sessions and plain-file handoffs. Without a shell,
write each message as a file in the task folder; one agent appends them verbatim as
sole transcript writer. If a required participant, independent context, permission,
or record cannot be provided safely, report the missing capability; never simulate an
independent reviewer inside the author's conversation. A small-context worker gets
one self-contained brief, a bounded input, and a fixed output format; treat its
return as unverified.
