import sys
from collections import namedtuple

Token = namedtuple('Token', 'type lo hi')


def tokenize(line):
    ret = []
    ret.append(Token('WORD', 0, 1))
    ret.append(Token('WORD', 1, 2))
    return ret

def main():
    for line in sys.stdin:
        tokens = tokenize(line)
        for token in tokens:
            print("{}\t{}".format(token.type, line[token.lo:token.hi]))
