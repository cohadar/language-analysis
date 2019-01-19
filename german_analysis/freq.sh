#!/bin/bash
cat raw.txt | ../german_stream.sh | ../words.sh > words.txt
cat words.txt | ../sort_by_freq.sh > freq.tsv
