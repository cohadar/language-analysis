#!/bin/bash
wget https://www.grimmstories.com/de/grimm_maerchen/list -O list.html
python 00-getlist.py | sort -u > list.txt
