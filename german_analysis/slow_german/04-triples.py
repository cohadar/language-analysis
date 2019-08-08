# print triples of lines
import sys
import json


class Triple:
    def __init__(self):
        self.triple = []

    def push(self, line):
        if len(self.triple) == 3:
            self.pop()
        self.triple.append(line)

    def pop(self):
        if len(self.triple) > 0:
            json.dump(self.triple, sys.stdout)
            self.triple = self.triple[1:]


if __name__ == "__main__":
    for line in sys.stdin:
        paragraphs = json.loads(line)
        t = Triple()
        for para in paragraphs:
            for line in para:
                t.push(line)
            t.pop()
