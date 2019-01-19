#!/bin/bash
cat words.txt | ../tuple3.py | ../sort_by_freq.sh | head -300000 > tuple3.tsv
