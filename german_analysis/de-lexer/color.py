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

def main():
    learned = ['trla', 'baba', 'lan']
    learning = ['da', 'joj', 'prodje', 'dan']
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
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Boji tekst.')
    parser.add_argument('--wcfile', help='fajl sa brojem reči.', required=True)
    parser.add_argument('--learned', type=int, help='koliko sam naučio', required=True)
    parser.add_argument('--learning', type=int, help='koliko učim', required=True)
    args = parser.parse_args()
    print(args)
    main()
