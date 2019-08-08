#!/bin/bash
set -eu
ls tmp/01 |
while read -r PAGE; do
	echo "extracting $PAGE"
	cat "tmp/01/$PAGE" | python 02-extract.py > "texts/${PAGE}.text"
done
