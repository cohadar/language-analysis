#!/usr/local/bin/python3
import sys

preva = "-"
prevb = "-"
for line in sys.stdin:
    curr = line[:-1]
    print(preva + "\t" + prevb + '\t' + curr)
    preva = prevb
    prevb = curr
