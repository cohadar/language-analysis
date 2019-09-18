"""
Boji tekst u zavisnosti od frekvencija reči.

Naučeno. Nauči. Prevedi. Ignoriši.

"""
import sys
import argparse
from lexer import tokenize

WHITE = '\033[89m'
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
PINK = '\033[95m'
GRAY = '\033[37m'
DARKGRAY = '\033[90m'
ENDC = '\033[0m'

COLORS = [
    WHITE,
    GREEN,
    BLUE,
]

GRADES = [
        0,
        1000,
        2000,
]


def load_words(wcfile, nlearned):
    words = []
    with open(wcfile, "r") as f:
        for i, line in enumerate(f):
            count, word = line[:-1].split('\t')
            words.append(word)
    g = [nlearned + x for x in GRADES]
    return (words[:g[0]], words[g[0]:g[1]], words[g[1]:g[2]])


def colorize(wt):
    for line in sys.stdin:
        tokens = tokenize(line)
        for token in tokens:
            if token.kind == 'WORD':
                if token.data in wt[0]:
                    print(token.data, end='')
                elif token.data in wt[1]:
                    print(COLORS[1], end='')
                    print(token.data, end='')
                    print(ENDC, end='')
                elif token.data in wt[2]:
                    print(COLORS[2], end='')
                    print(token.data, end='')
                    print(ENDC, end='')
                else:
                    print(DARKGRAY, end='')
                    print(token.data, end='')
                    print(ENDC, end='')
            elif token.kind == 'UNKNOWN':
                print(RED, end='')
                print(token.data, end='')
                print(ENDC, end='')
            else:
                print(token.data, end='')


def main():
    parser = argparse.ArgumentParser(description='Boji tekst.')
    parser.add_argument('--wcfile', help='fajl sa brojem reči.', required=True)
    parser.add_argument('--nlearned', type=int, help='koliko sam već naučio', required=True)
    args = parser.parse_args()
    colorize(load_words(args.wcfile, args.nlearned))


if __name__ == '__main__':
    main()
    # for x in range(1, 257):
    #     print('\033[{}m hello colors: {}'.format(x, x))
