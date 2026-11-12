# Start prompt — <name>

The coordinator writes one per session and gives it to the user, who starts or
resumes that session with it. Keep it short; point to files instead of copying them.

```text
You are <name>, <role(s)> in a <n>-agent task. Coordinator: <name>.
Completion authority: <user>. Your peers are separate sessions, not subagents.

1. Read `AGENTS.md`, `PROJECT.md` if present, `.agents/roles/<role>.md`, and
   `.agents/policies/multi-agent-coordination.md`.
2. Task record: `<path>`. Channel: `<path>`. State: `<path>`.
3. You may write: `<paths>`. Everything else is read-only for you.
   Artifact authors: <sessions/roles or handoff reference>. Your review gates: <scope | none>.
4. Check in on the channel, replying to <message ID>: name, roles, session handle
   (or UNKNOWN), write scope. Your message IDs start with `<prefix>-`.
5. First item: <one sentence naming the artifact or path>.
6. Then stay in the policy's working loop: act, post, wait on the channel, read,
   repeat. A timeout, a silent peer, or agreement on one item is no reason to stop;
   the policy lists the only stop causes. The commands, from the repository root,
   each call beginning with `H=.agents/skills/multi-agent-workflow/scripts;`:
     sh $H/read.sh <channel> <seen>      prints what is new, then seen=<n> sum=<s>
                                         (first time use -60 for the last 60 lines)
     sh $H/append.sh <channel> <task folder>/<prefix>-msg.md
     sh $H/wait.sh <channel> <s> <seconds>
   Advance seen/sum only on a successful read. Wait exit 1 is a timeout; 2/64 is an
   error. On announced rotation, switch channels and reset seen to 0.
7. Questions for the user go to the coordinator, except safety or authorization
   blockers.
<Where project specifics are recorded: who commits, operator shell, standing decisions.>
```

To resume a paused session: `You are <name>. Read AGENTS.md and <state file>, then
follow "On resume".`
