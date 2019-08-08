#!/bin/bash
set -eu
cat list.txt |
while read -r LINK; do
	echo "downloading $LINK"
	wget -q -O "tmp/01/$(basename "$LINK")" "$LINK"
	sleep 1
done
