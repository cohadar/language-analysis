"""
Boji tekst u zavisnosti od frekvencija reči.

Naučeno. Učim. Neučim.

"""
import sys
import argparse
from lexer import tokenize

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
ENDC = '\033[0m'

def load_words(wcfile, nlearned, nlearning):
    words = []
    with open(wcfile, "r") as f:
        for i, line in enumerate(f):
            count, word = line[:-1].split('\t')
            words.append(word)
    return words[:nlearned], words[nlearned:nlearned+nlearning]

def colorize(learned, learning):
    for line in sys.stdin:
        tokens = tokenize(line)
        for token in tokens:
            if token.kind == 'WORD':
                if token.data in learned:
                    print(token.data, end='')
                elif token.data in learning:
                    print(GREEN, end='')
                    print(token.data, end='')
                    print(ENDC, end='')
                else:
                    print(BLUE, end='')
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
    parser.add_argument('--nlearned', type=int, help='koliko sam naučio', required=True)
    parser.add_argument('--nlearning', type=int, help='koliko učim', required=True)
    args = parser.parse_args()
    learned, learning = load_words(args.wcfile, args.nlearned, args.nlearning)
    colorize(learned, learning)

if __name__ == '__main__':
    main()
