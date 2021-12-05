#!/usr/bin/env python3

from collections import defaultdict


FILE = 'input.txt'
with open(FILE) as f:
    lines = [[list(map(int,p[0].split(','))), list(map(int,p[1].split(',')))] for p in [l.split(' -> ') for l in f.read().splitlines()]]


def diagram(lines, diagonal=False):
    d = defaultdict(lambda: 0)

    for l in lines:
        diffx = l[1][0] - l[0][0]
        diffy = l[1][1] - l[0][1]
        if not diagonal and diffx and diffy:
            continue
        end = diffx or diffy
        stepx = diffx//abs(diffx) if diffx else 0
        stepy = diffy//abs(diffy) if diffy else 0

        for i in range(abs(end)+1):
            d[(l[0][0]+stepx*i, l[0][1]+stepy*i)] += 1

    return sum([v > 1 for v in d.values()])


print(diagram(lines, diagonal=False))
print(diagram(lines, diagonal=True))
