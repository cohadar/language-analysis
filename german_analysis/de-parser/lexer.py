r"""
Ovo je lexer za nemačke tekstove.

Od teksta vraća tokene za reči i interpunkciju.

>>> print_all(tokenize('trla baba  lan'))
DEWORD  trla
SPACE   b' '
DEWORD  baba
SPACE   b'  '
DEWORD  lan

>>> print_all(tokenize('trla, baba, lan'))
DEWORD  trla
DEPUNKT ,
SPACE   b' '
DEWORD  baba
DEPUNKT ,
SPACE   b' '
DEWORD  lan
"""
import sys
import re

de_char = re.compile(r'[a-z]|[A-Z]|[ßäÄöÖüÜ]')
de_punkt = re.compile(r'[.,:;\'"!?]')

class Token:
    def __init__(this, kind, data):
        this.kind = kind
        this.data = data
    def __str__(this):
        if this.kind in ['DEWORD', 'DEPUNKT']:
            return "{:8}{}".format(this.kind, this.data)
        else:
            return "{:8}{}".format(this.kind, this.data.encode('utf-8'))
    def __repr__(this):
        if this.kind in ['DEWORD', 'DEPUNKT']:
            return "{}\t{}".format(this.kind, this.data)
        else:
            return "{}\t{}".format(this.kind, this.data.encode('utf-8'))

def get_kind(c):
    if c == ' ':
        return 'SPACE'
    elif c == '\n':
        return 'NL'
    elif de_char.match(c):
        return 'DEWORD'
    elif de_punkt.match(c):
        return 'DEPUNKT'
    else:
        return 'UNKNOWN'

def tokenize(line):
    lo = 0
    kind = None
    for hi, c in enumerate(line):
        ckind = get_kind(c)
        if ckind != kind or ckind in ['DEPUNKT', 'UNKNOWN']:
            if kind:
                yield Token(kind, line[lo:hi])
                kind = ckind
                lo = hi
            else:
                kind = ckind
    if kind:
        yield Token(kind, line[lo:])

def print_all(tokens):
    for token in tokens:
        print(str(token))

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
