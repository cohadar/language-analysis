#!/usr/local/bin/python3
import os
import sys

fileName = os.environ.get('FILENAME', 'temp')
files = {}
for line in sys.stdin:
    key = hash(line) % 16
    if not files.get(key):
        files[key] = open(fileName + '.' + ('%x' % key), 'w')
    files[key].write(line)
