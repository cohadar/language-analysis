#!/bin/bash
set -eu
ls tmp/02 |
while read -r PAGE; do
	echo "wrapping $PAGE"
	cat "tmp/02/$PAGE" | python 03-textwrap.py | jq -c > "tmp/03/$PAGE"
done
