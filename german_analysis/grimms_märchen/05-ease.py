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


# ease of a triple of lines
def ease(triple, weights):
    n = 0.0
    suminv = 0.0
    for line in triple:
        words = [word for word in re.split(r'\W+', line) if word != ""]
        n += 1.0 * len(words)
        for word in words:
            suminv += 1.0 / weights[word]
    return n / suminv


if __name__ == "__main__":
    weights = load_weights('04-words.tsv')
    for line in sys.stdin:
        triple = json.loads(line)
        print('{}\t{}'.format(ease(triple, weights), line.rstrip('\n')))
