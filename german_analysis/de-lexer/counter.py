"""
Broji reči u tekstu.

Računa frekvencije reči naravno. Vraća sortirano.
"""

import sys
import re
from collections import Counter
from lexer import tokenize

def main():
    c = Counter()
    for line in sys.stdin:
        tokens = tokenize(line)
        for token in tokens:
            if token.kind == 'WORD':
                c[token.data] += 1
    l = list(c.items())
    l.sort(key=lambda x: x[1], reverse=True)
    for k, v in l:
        print("{}\t{}".format(k, v))

if __name__ == '__main__':
    main()
