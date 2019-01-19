#!/bin/bash
set -eu
find "$1" -name \*.txt |
while read -r NAME; do
	# strip gutenberg header and footer and convert to utf-8
	cat $NAME | tail -n +500 | ghead -n -1000 | iconv -cs --from-code="$1" --to-code=UTF-8
done
