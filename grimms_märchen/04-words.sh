#!/bin/bash

# extract words from text
tempfile=$(mktemp)
ls tmp/03 |
while read -r PAGE; do
	echo "words $PAGE"
	cat tmp/03/"$PAGE" |
		python 04-words.py \
		>> "$tempfile"
done

# sort by freq
echo "calculating word frequencies..."
cat "$tempfile" |
	sort | uniq -c | sort -r -n -k1,1 |
	sed 's/^ *//;s/ *$//' | tr ' ' '\t' \
	> 04-words.tsv

# do a pareto here
head -$(cut -f1 04-words.tsv | python 04-pareto-index.py) 04-words.tsv > 04-words.pareto.tsv

# calculate line ease
ls tmp/03 |
while read -r PAGE; do
	echo "ease $PAGE"
	cat tmp/03/"$PAGE" |
		python 04-line-ease.py \
		> tmp/04/"$PAGE"
done
