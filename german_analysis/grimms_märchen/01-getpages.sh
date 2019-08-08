#!/bin/bash
set -eu
cat list.txt |
while read -r LINK; do
	echo "downloading $LINK"
	wget -q -P tmp/01/ "$LINK"
	sleep 1
done
