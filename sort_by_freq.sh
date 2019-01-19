#!/bin/sh
if [ -z "$1" ]; then
	echo "please specify filename"
	exit 1
fi
temp=$(mktemp)
gsort "$1" | uniq -c > "$temp"
gsort -r -n -k1,1 "$temp" | sed 's/^ *//' | tr -s ' ' | tr ' ' '\t'
