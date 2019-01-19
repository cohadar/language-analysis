#!/bin/bash
set -u
find gutenberg -name \*.txt |
while read -r NAME; do
	# strip gutenberg header and footer
	cat "$NAME" | tail -n +500 | ghead -n -1000
done

