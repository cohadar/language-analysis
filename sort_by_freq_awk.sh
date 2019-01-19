#!/bin/sh
temp=$(mktemp)
awk '
{ words[$0]++ }
END {
	for (w in words)
		printf("%d\t%s\n", words[w], w)
}' > "$temp"
gsort -r -n -k1,1 -t$'\t' "$temp"
