#!/bin/sh
# Usage: read.sh FILE [SEEN_LINES | -LAST] (default 0; counts 0..2147483647, no leading zeros)
# Prints complete lines after SEEN_LINES, then "seen=<lines> sum=<checksum>".
# Advance the cursor only on exit 0. Exit 2 read failure, 64 bad usage/cursor.
[ $# -ge 1 ] && [ $# -le 2 ] || { echo "usage: read.sh FILE [SEEN_LINES | -LAST]" >&2; exit 64; }
f=$1; n=${2-0}; count=${n#-}
case $count in ''|*[!0-9]*|0?*) echo "bad SEEN_LINES: $n" >&2; exit 64;; esac
[ "${#count}" -le 10 ] && [ "$count" -le 2147483647 ] 2>/dev/null ||
  { echo "SEEN_LINES out of range: $n" >&2; exit 64; }
[ -f "$f" ] && [ -r "$f" ] || { echo "unreadable regular file: $f" >&2; exit 2; }
sum=$(cksum <"$f") || exit 2
m=$(wc -l <"$f") || exit 2
[ "$m" -ge 0 ] && [ "$m" -le 2147483647 ] 2>/dev/null ||
  { echo "line count out of range: $f" >&2; exit 2; }
m=$((m + 0))
case $n in -*) n=$((m - count)); [ "$n" -lt 0 ] && n=0;; esac
[ "$n" -gt "$m" ] && n=0
if [ "$n" -lt "$m" ]; then
  sed -n "$((n + 1)),${m}p" "$f" || exit 2
fi
printf 'seen=%s sum=%s\n' "$m" "${sum% *}-${sum#* }"
