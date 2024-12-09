#!/bin/env pypy


from collections import defaultdict
from itertools import combinations, chain


f = open('08.input.txt').readlines()
d = defaultdict(lambda: [])
[d[c].append((row,col)) for row, line in enumerate(f) for col, c in enumerate(line) if c != '.']


def resonance(start=1, end=2):
    anti = []
    for pairs in [list(combinations(freq, 2)) for freq in d.values()]:
        dif = defaultdict(lambda: [])
        for x, y in pairs:
            dif[x].append((x[0]-y[0], x[1]-y[1]))
            dif[y].append((y[0]-x[0], y[1]-x[1]))
        for mult in range(start, end):
            for ant, diff in dif.items():
                anti += [(ant[0] + mult*dd[0], ant[1] + mult*dd[1]) for dd in diff]
    print(len(filter(lambda x: x not in d.values() and x[0] >= 0 and x[0] < len(f) and x[1] >= 0 and x[1] < len(f), set(anti))))


# part A
resonance()

# part B
resonance(0, len(f))
