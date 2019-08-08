import sys
import json
import textwrap


def wrap(text):
    lines = text.splitlines()
    wrapped = []
    for line in lines:
        wrapped.extend(textwrap.wrap(line, 70))
    return wrapped


if __name__ == "__main__":
    for line in sys.stdin:
        a = json.loads(line)
        b = []
        b.append(wrap(a["title"]))
        b.append(wrap(a["text"]))
        json.dump(b, sys.stdout)
