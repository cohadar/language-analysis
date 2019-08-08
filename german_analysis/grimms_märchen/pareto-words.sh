#!/bin/bash

# extract words from text
python 04-words.py > tmp/words

# sort by freq
cat tmp/words |
	sort | uniq -c | sort -r -n -k1,1 |
	sed 's/^ *//;s/ *$//' | tr ' ' '\t' \
	> tmp/words.tsv

# do a pareto here
head -$(cut -f1 tmp/words.tsv | python 04-pareto-index.py) tmp/words.tsv
