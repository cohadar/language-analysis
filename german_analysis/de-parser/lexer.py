"""
Ovo je lexer za nemačke tekstove.

Od teksta vraća tokene za reči i interpunkciju.

>>> Token('WORD', 3, 5)
Token(kind='WORD', lo=3, hi=5)
"""
import sys

class Token:
    def __init__(this, line, kind, lo, hi):
        this.line = line
        this.kind = kind
        this.lo = lo
        this.hi = hi
        assert lo <= hi
    def __repr__(this):
        return "{}\t{}".format(this.kind, this.line[this.lo:this.hi].encode('utf-8'))

def tokenize(line):
    lo = 0
    kind = None
    for i, c in enumerate(line):
        if c == ' ':
            if kind is None:
                kind = 'SPACE'
            elif kind == 'WORD':
                yield Token(line, kind, lo, i)
                kind = 'SPACE'
                lo = i
        else:
            if kind is None:
                kind = 'WORD'
            elif kind == 'SPACE':
                yield Token(line, kind, lo, i)
                kind = 'WORD'
                lo = i
    if kind:
        yield Token(line, kind, lo, len(line))

def main():
    for line in sys.stdin:
        tokens = tokenize(line)
        for token in tokens:
            print(token)

if __name__ == '__main__':
    main()
