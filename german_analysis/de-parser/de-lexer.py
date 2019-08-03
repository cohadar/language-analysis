"""
Ovo je lexer za nemačke tekstove.

Od teksta vraća tokene za reči i interpunkciju.

>>> Token('WORD', 3, 5)
Token(type='WORD', lo=3, hi=5)
"""
import sys
from collections import namedtuple

Token = namedtuple('Token', 'type lo hi')

def tokenize(line):
    ret = []
    for i, c in enumerate(line):
        ret.append(Token('CHAR', i, i + 1))
    return ret

def main():
    for line in sys.stdin:
        tokens = tokenize(line)
        for token in tokens:
            data = line[token.lo:token.hi]
            print("{}\t{}".format(token.type, data.encode('utf-8')))

if __name__ == '__main__':
    main()
