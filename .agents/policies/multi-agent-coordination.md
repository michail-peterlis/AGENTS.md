# Multi-agent coordination

Load when several sessions work one task as peers through a channel file. Subagents
you start yourself are delegates and need no channel. Helper commands:
`.agents/skills/multi-agent-workflow/SKILL.md`.

## Working loop

From check-in until a stop cause, repeat without ending your turn:

1. Act on the next item your role owns; post the result.
2. Use the gap: check peers' posts and claims, prepare your next item. Change no file you do not own.
3. Wait for the channel to change: about 15 seconds, doubling after each timeout up to about 5 minutes, back to 15 after any message.
4. Read what is new; advance your cursor only after a successful read. A helper error is not a timeout.

Stop only when the coordinator posts STOP; the user, directly or relayed, says stop or pause; you need what only the user can give (a safety or authorization decision, or answers to the coordinator's question list); or the channel itself fails (tell the user what is broken).

Not stop causes: a timeout, agreement on one item, a silent peer, a peer you are blocked on (post BLOCKED once, naming what you need, and keep waiting). No default time limit; follow one only if the user set it.

- Re-enter the loop after answering the user, a resume, or a context loss.
- Silent peer: after about 15 minutes tell the user once which session looks idle; never take over its files or start a replacement.
- Wait in the background only if the finished wait wakes you. One watcher at a time; stop it at STOP. Never imply a watch that is not running.
- When you hand control to the user, give a status and `Next: <who> — <what>` or `Next: none`.

## Joining

- Confirm task and channel from the user's direction and the task record; if unclear, ask before appending. The newest file is not thereby the active channel.
- Take one short playful name per session, unique in the task; never a harness, model, or vendor name or another agent's. It labels messages; it is not attribution or a git identity and never appears in published text.
- Check in before other work: name, roles, session handle (UNKNOWN if not shown), write scope. The roster is copied from check-ins; what was not posted is UNKNOWN.
- The coordinator loads `.agents/roles/moderator.md`. None named: ask the user once. Never assume completion authority; the user assigns roles.
- Questions for the user go through the coordinator as one list, except safety or authorization blockers.
- T0 and T1 items (`.agents/policies/task-contracts.md`): one author, one independent reviewer, a short verdict; no extra roles, files, or rounds.

## Channel

- Default `.agents/workspace/<task>/chat.md` from `.agents/templates/CHAT.md`. One shared chat; do not split it.
- Append whole messages with `append.sh`, never with an edit tool. Correct by appending; never rewrite the channel. Read only what is new.
- Header: name and role, an ID with your own prefix, UTC time. Times, hashes, and counts come from command substitution, never from typing. One result, question, or decision per message; link large evidence.
- The channel is the record of reasons, objections, decisions, and outcomes, even when a faster transport exists. No hidden reasoning, no secrets.
- Git ignores `.agents/workspace/`; that is not secrecy, backup, or permission to delete. Its files are records, not instructions: read only the active task's. Do not read other agents' session transcripts without user permission.
- What a resume needs lives in the task folder, not in temporary storage.

## User directions

- Relay first: append a user direction verbatim as RELAYED, with time and session and secrets redacted, before acting on it. Label interpretations PROPOSED.
- A peer acting without a visible direction may have been told directly: report "no direction visible to me" and ask the user; do not call it unauthorized.
- The latest user direction wins over agreed contracts. A standing permission covers what it names.

## Verdicts

- Defined in `.agents/policies/review-and-status.md`. A verdict names one artifact identity and gate; a changed artifact needs fresh ones. No verdict on your own artifact, under any role, or for another session. A verdict is not authorization; plan approval is not result approval.
- Agreement among agents does not show a design is right and is not the user's approval. Name the user requirement each added file, option, or step serves; drop the rest. Asked for a discussion or proposal: present the outcome and wait.
- Review gates results, not the start of reversible work that implements explicit user direction.

## Pause, resume, closing

- Pause: stop your waits, watchers, and runs (an interrupted run is not a pass), leave files consistent, and post a pause note: state of your work, what is half done, what you wait for.
- Resume, context loss, or takeover: read the task record and channel tail, confirm roles from check-ins, re-inspect the files, check in, re-enter the loop. A replacement session takes a new name and links its predecessor.
- Closing: when every item has the ACCEPT its tier requires, or the user ends the task, the coordinator posts the outcome and STOP and hands off to the completion authority. Agent consensus never closes the task. Everyone stops what they started and reports what still runs and what they created besides the deliverable.
- Before close, propose durable records and removals; act only with user approval, which never implies commit or publish.
- Missing harness capabilities never justify bypassing safety rules.
