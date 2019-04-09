import sys
# print the index of the element after witch only 20% of array weight remains
# it is assumed array is sorted in descending order

if __name__ == "__main__":
    freqs = []
    for line in sys.stdin:
        freqs.append(int(line))
    pareto = sum(freqs) * 0.8
    sofar = 0
    for i, num in enumerate(freqs):
        sofar += num
        if sofar >= pareto:
            print(i)
            break
