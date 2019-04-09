#!/bin/bash

# calculate triple ease
ls tmp/04 |
while read -r PAGE; do
	echo "ease $PAGE"
	cat tmp/04/"$PAGE" |
		python 05-ease.py \
		> tmp/05/"$PAGE"
done

# sort triples by ease
echo "sorting triples"
cat tmp/05/* | sort -t$'\t' -k1 -n | cut -f2 > tmp/sorted-triples.jsonl

echo "search like this:"
echo "cat tmp/sorted-triples.jsonl | jq -r '.[]' | grep -C1 Apfel"
