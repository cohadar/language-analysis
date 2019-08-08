import re
import sys


if __name__ == "__main__":
    for line in sys.stdin:
        for word in re.split(r'\W+', line):
            if word != '':
                print(word)
