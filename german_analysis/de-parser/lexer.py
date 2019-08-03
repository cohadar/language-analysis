"""
Ovo je lexer za nemačke tekstove.

Od teksta vraća tokene za reči i interpunkciju.

>>> Token('WORD', 3, 5)
Token(kind='WORD', lo=3, hi=5)
"""
import sys
import re

de_char = re.compile(r'[a-z]|[A-Z]|[ßäÄöÖüÜ]')

class Token:
    def __init__(this, kind, data):
        this.kind = kind
        this.data = data
    def __repr__(this):
        return "{}\t{}".format(this.kind, this.data.encode('utf-8'))

def get_kind(c):
    if c == ' ':
        return 'SPACE'
    elif c == '\n':
        return 'NL'
    elif de_char.match(c):
        return 'DEWORD'
    else:
        return 'UNKNOWN'

def tokenize(line):
    lo = 0
    kind = None
    for i, c in enumerate(line):
        ckind = get_kind(c)
        if ckind != kind:
            if kind is None:
                kind = ckind
            else:
                yield Token(kind, line[lo:i])
                kind = ckind
                lo = i
    if kind:
        yield Token(kind, line[lo:])

def main():
    has_unknown = False
    for line in sys.stdin:
        tokens = tokenize(line)
        for token in tokens:
            print(token)
            if token.kind == 'UNKNOWN':
                has_unknown = True
    if has_unknown:
        sys.exit(1)

if __name__ == '__main__':
    main()
