#!/bin/bash
cat words.txt | ../tuple2.py | ../sort_by_freq.sh | head -300000 > tuple2.tsv
