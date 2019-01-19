#!/bin/bash
set -u
find "$1" -name \*.txt |
while read -r NAME; do
	# strip gutenberg header and footer and convert to utf-8
	# files that cannot be converted are ignored, because they usualy have wrong encoding spec,
	# and would produce a lot of bad data.
	cat $NAME | tail -n +500 | ghead -n -1000 | iconv --from-code="$1" --to-code=UTF-8
done
