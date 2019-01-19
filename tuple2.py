#!/usr/local/bin/python3
import sys

prev = "-"
for line in sys.stdin:
    curr = line[:-1]
    sys.stdout.write(prev + "\t" + curr + "\n")
    prev = curr
