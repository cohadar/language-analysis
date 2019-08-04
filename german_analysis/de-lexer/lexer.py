"""
Ovo je lexer za nemačke tekstove.

Od teksta vraća tokene za reči i interpunkciju.

>>> print_all(tokenize('trla baba  lan'))
WORD    trla
SPACE   b' '
WORD    baba
SPACE   b'  '
WORD    lan

>>> print_all(tokenize('trla, baba'))
WORD    trla
PUNKT   ,
SPACE   b' '
WORD    baba

>>> print_all(tokenize('trla,,baba'))
WORD    trla
PUNKT   ,
PUNKT   ,
WORD    baba

>>> print_all(tokenize('trla{baba'))
WORD    trla
UNKNOWN b'{'
WORD    baba
"""
import sys
import re

re_word = re.compile(r'\w')

punkt = '-.,:;!?()[]' + '"' + "'"

class Token:
    def __init__(this, kind, data):
        this.kind = kind
        this.data = data
    def __repr__(this):
        if this.kind in ['WORD', 'PUNKT']:
            return "{:8}{}".format(this.kind, this.data)
        else:
            return "{:8}{}".format(this.kind, this.data.encode('utf-8'))

def get_kind(c):
    if c == ' ':
        return 'SPACE'
    elif c == '\t':
        return 'TAB'
    elif c == '\n':
        return 'NL'
    elif re_word.match(c):
        return 'WORD'
    elif c in punkt:
        return 'PUNKT'
    else:
        return 'UNKNOWN'

def tokenize(line):
    lo = 0
    kind = None
    for hi, c in enumerate(line):
        ckind = get_kind(c)
        if ckind != kind or ckind in ['PUNKT', 'UNKNOWN']:
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
        print(token)

def main():
    has_unknown = False
    for line in sys.stdin:
        tokens = tokenize(line)
        for token in tokens:
            print(repr(token))
            if token.kind == 'UNKNOWN':
                has_unknown = True
    if has_unknown:
        sys.exit(1)

if __name__ == '__main__':
    main()
