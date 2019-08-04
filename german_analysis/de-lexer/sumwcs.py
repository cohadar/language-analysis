"""
Suma broja reči

na ulazu su tabom razdvojeni brojevi i reči
"""

import sys
import re
from collections import Counter
from lexer import tokenize

def main():
    c = Counter()
    for line in sys.stdin:
        count, data = line[:-1].split('\t')
        c[data] += int(count)
    l = list(c.items())
    l.sort(key=lambda x: x[1], reverse=True)
    for k, v in l:
        print("{}\t{}".format(v, k))

if __name__ == '__main__':
    main()
