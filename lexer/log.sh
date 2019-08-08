#!/bin/bash

find ../../grimms_märchen/texts -name \*.text |
while read -r NAME; do
	cat "$NAME" | python counter.py | tee ../../grimms_märchen/texts/"$NAME".wc;
done

cat ../../grimms_märchen/texts/*.wc | python sumwcs.py | tee ../../grimms_märchen/texts/__wc__

cat ../../grimms_märchen/texts/allerleirauh.text | python linebreaker.py | python color.py --wcfile ../../grimms_märchen/texts/__wc__ --nlearned=1000 --nlearning=1000 | less -R
