"""
Razbija tekst na rečenice.

Nije 100% uspešan, al nema veze. Gut genug.

"""
import sys
from lexer import tokenize, is_pre_breaking, is_post_breaking

def main():
    broken = False
    for line in sys.stdin:
        tokens = tokenize(line)
        for token in tokens:
            if broken and token.kind in ['SPACE', 'NL']:
                continue
            if token.kind == 'PUNKT':
                if is_pre_breaking(token.data) and not broken:
                    print()
                    broken = True
                print(token.data, end='')
                if is_post_breaking(token.data):
                    print()
                    broken = True
            else:
                print(token.data, end='')
                broken = False

if __name__ == '__main__':
    main()
