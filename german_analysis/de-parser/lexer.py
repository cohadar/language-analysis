"""
Ovo je lexer za nemačke tekstove.

Od teksta vraća tokene za reči i interpunkciju.

>>> Token('WORD', 3, 5)
Token(kind='WORD', lo=3, hi=5)
"""
import sys
from collections import namedtuple

Token = namedtuple('Token', 'kind lo hi')

def tokenize(line):
    lo = 0
    kind = None
    for i, c in enumerate(line):
        if c == ' ':
            if kind is None:
                kind = 'SPACE'
            elif kind == 'WORD':
                yield Token(kind, lo, i)
                kind = 'SPACE'
                lo = i
        else:
            if kind is None:
                kind = 'WORD'
            elif kind == 'SPACE':
                yield Token(kind, lo, i)
                kind = 'WORD'
                lo = i
    if kind:
        yield Token(kind, lo, len(line))

def main():
    for line in sys.stdin:
        tokens = tokenize(line)
        for token in tokens:
            data = line[token.lo:token.hi]
            print("{}\t{}".format(token.kind, data.encode('utf-8')))

if __name__ == '__main__':
    main()
