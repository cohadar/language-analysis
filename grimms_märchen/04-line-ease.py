# calculate "ease" of sentence as a harmonic mean of word weights
import re
import sys
import json


def load_weights(fileName):
    weights = {}
    with open(fileName, 'r') as f:
        for i, line in enumerate(f):
            a = line.rstrip('\n').split('\t')
            weights[a[1]] = int(a[0])
    return weights


# ease of a line
def calc(line, weights):
    words = [word for word in re.split(r'\W+', line) if word != ""]
    n = 1.0 * len(words)
    suminv = 0.0
    for word in words:
        suminv += 1.0 / weights[word]
    return n / suminv


# calculate line ease
def ease(weights, arr):
    ret = []
    for line in arr:
        o = {}
        o["line"] = line
        o["ease"] = calc(line, weights)
        ret.append(o)
    return ret


if __name__ == "__main__":
    weights = load_weights('04-words.tsv')
    for line in sys.stdin:
        multiarr = json.loads(line)
        newmultiarr = []
        for arr in multiarr:
            newmultiarr.append(ease(weights, arr))
        json.dump(newmultiarr, sys.stdout)
