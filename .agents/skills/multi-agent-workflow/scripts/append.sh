#!/bin/sh
# Usage: append.sh FILE MESSAGE_FILE. Appends a whole message and blank line under a mkdir lock.
# Use regular non-symlink files; FILE must have one hard link. Self-input fails with exit 64.
# Gives up after ~30s (exit 1): a stale FILE.lock needs a human or Moderator, not automatic deletion.
usage() { echo "usage: append.sh FILE MESSAGE_FILE (regular non-symlink files; FILE's folder must exist)" >&2; exit 64; }
[ $# -eq 2 ] && [ -f "$2" ] && [ -r "$2" ] || usage
# Resolve directory aliases so equivalent spellings share the same lock and self-check.
dir=$(CDPATH= cd -P "$(dirname "$1")" && pwd -P) || usage
msgdir=$(CDPATH= cd -P "$(dirname "$2")" && pwd -P) || usage
f=$dir/$(basename "$1"); message=$msgdir/$(basename "$2")
[ "$f" != "$message" ] && [ ! -L "$f" ] && [ ! -L "$message" ] || usage
n=0
until mkdir "$f.lock" 2>/dev/null; do
  n=$((n + 1)); [ "$n" -ge 30 ] && { echo "lock busy: $f.lock" >&2; exit 1; }
  sleep 1
done
trap 'rmdir "$f.lock"' EXIT
# Refuse hard-linked channels: another name would use a different lock. Check under the lock.
if [ -f "$f" ]; then
  single=$(find "$f" -prune -links 1 -print) || exit 1
  [ -n "$single" ] || usage
elif [ -e "$f" ]; then
  usage
fi
[ ! -L "$f" ] || usage
[ -s "$f" ] && [ -n "$(tail -c1 "$f")" ] && echo >> "$f"
{ cat "$message" && { [ -z "$(tail -c1 "$message")" ] || echo; } && echo; } >> "$f"
