#!/bin/bash
set -eu
echo 'downloading list.html'
wget -q https://slowgerman.com/inhaltsverzeichnis/ -O tmp/00/list.html
echo 'extracting list.txt'
cat tmp/00/list.html | python 00-getlist.py | sort -u > list.txt
