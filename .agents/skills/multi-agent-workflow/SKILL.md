# Skill: Multi-Agent Workflow

Use for a task that benefits from explicit delegation or independent review.
This is a procedure, not an executable orchestrator or an installed integration.

*Peers* are separate sessions the user starts; they coordinate through a channel file
under the [coordination policy](../../policies/multi-agent-coordination.md), which
also holds the decision vocabulary. *Delegates* are subagents your own session starts
and collects; they need no channel, names, or check-in. Asked to work with peers, do
not spawn delegates instead. Headless/event-triggered jobs use
[staged execution](../../policies/staged-execution.md); they imply neither peers nor
delegation. All contexts use the [evaluation loop](../evaluation-loop/SKILL.md) for
artifact evaluation and authorized rework, not separate quality frameworks.

## Procedure

1. Establish the task contract, participants and completion authority. For peers,
   use the coordination policy and name a coordinator; delegates stay under their
   parent session's scoped brief. Select only the roles the task needs.
2. Decompose the work into bounded outputs and dependencies. A small task may need
   only one implementer and an independent reviewer, not a standing committee.
3. Prepare each brief: role, objective, necessary source references, artifact
   identity, verification requirements, return format, the working directory, and
   the only paths it may write; everything else is read-only. For peers, use
   `.agents/templates/LAUNCH.md`. For a review or audit, give the question and the
   sources, not the answer you expect. Include only relevant context; distinguish
   source facts from interpretations.
4. Load [tool authority](../../policies/tool-authority.md) before assigning tools
   or permissions. Record limits the user set (time, cost, rework rounds); do not
   invent a waiting limit. For delegates that build or test, set concurrency, time and
   memory caps per command. Check the runtime's actual delegation, permission and
   cancellation capabilities; record any fallback. Select models from the project's
   permitted profiles, not hard-coded role defaults.
5. Write the brief to the human-readable record before dispatch, where a restart
   cannot erase it.
6. Dispatch independent read-heavy investigations in parallel where useful. Schedule
   dependent edits sequentially, observing the policy's ownership rules.
7. When a delegate returns, list what changed outside its paths; its own statement
   about side effects is REPORTED. Persist replies, objections, limitations and
   outcomes before using them for decisions. Link large reports instead of passing
   full logs through each agent.
8. Deliver a stable implementation handoff with its artifact identity. Select neutral
   critic inputs from it: goal, approved standard, constraints/deviations, identity and
   verification commands, not builder persuasion/history or previous verdicts. Each
   criticism round needs a fresh independent context inspecting actual output.
9. Route required corrections to the assigned editor; issue a fresh handoff after
   changes and protect previously verified criteria. Honor supplied limits; diagnose
   ineffective repetition and escalate decisions/capabilities outside scope rather
   than impose a fixed round count. Quality-loop exits do not end the peer working loop.
10. Re-check findings you will act on. For review, record artifact authors by session
    and collect ACCEPTs for the contract's required independent gates and scopes on
    the same identity; role-switching does not make an author independent. Research
    delegates return findings, not mandatory verdicts. Hand off the remaining decision
    using the policy's status and `Next` fields.

## Waiting on a shared channel

Three dependency-free POSIX `sh` helpers are in `scripts/`:

- `read.sh <channel> [<seen> | -<last>]` prints complete lines, then
  `seen=<lines> sum=<checksum>`. Counts must be 0–2147483647 without leading zeros;
  exit 2 is a read failure, 64 bad usage. Retain the old cursor on any failure.
- `wait.sh <channel> <sum> [<seconds>]` returns 0 as soon as the channel differs from
  `<sum>`, 1 on timeout (default 120 s), 2 if unreadable, 64 on a malformed sum.
- `append.sh <channel> <message file>` appends one whole message under a directory
  lock (`<channel>.lock`) and gives up after about 30 s. Use regular non-symlink files
  and a channel with one hard link; self-input and final-component symlinks are
  rejected with exit 64. Directory aliases are normalized to the same lock.
  Helpers coordinate cooperative writers, not hostile
  filesystem mutations.

The loop, from the repository root. Carry the two numbers from each `read.sh` into
the next commands; `<prefix>` is your message-ID prefix. Shell variables may not
survive between tool calls: begin every call with the first line.

```sh
W=.agents/workspace/<task>; C=$W/chat.md; H=.agents/skills/multi-agent-workflow/scripts
sh "$H/read.sh" "$C" -60                  # join: the last 60 lines, then seen=<n> sum=<s>
# act; write your message to $W/<prefix>-msg.md, then:
sh "$H/append.sh" "$C" "$W/<prefix>-msg.md"
sh "$H/read.sh" "$C" <n>                  # your message and anything a peer posted meanwhile
sh "$H/wait.sh" "$C" <s> 15 >/dev/null
# Inspect exit status: 0 -> read from <n>; 1 -> back off; 2/64 -> error, not timeout.
```

After each timeout double the seconds (15, 30, 60, 120, 240), then stay at about 300;
after any message start again at 15. Keep each call below your tool's timeout. The
stop causes are in the policy; a timeout is not one of them. On an announced channel
rotation, switch to the new path and reset `seen` to 0, even when the new file is longer.

## Capability fallback

Without native subagents, use explicitly separate sessions and plain-file handoffs.
Without a shell, write each message as a file in the task folder; one agent is the
sole transcript writer and appends them verbatim. If the required participant, independent context, permissions or file
record cannot be provided safely, report the missing capability; do not simulate an
independent reviewer inside the author's conversation.

A worker with a small context window gets one self-contained brief that fits together
with its input, a bounded input, and a fixed output format; do not expect it to
explore. Treat what it returns as unverified.
