#!/bin/env pypy


from collections import defaultdict


d = defaultdict(lambda: -1)
for row, line in enumerate(open('10.input.txt')):
    for col, c in enumerate(line.strip()):
        d.update({(row,col): int(c)})

ind = ((0,1), (1,0), (-1,0), (0,-1))
suniq = 0
s = 0
for h in [head for head, v in d.items() if v == 0]:
    trails = [h]
    for i in range(1, 10):
        trails = [filter(lambda c: d[c] == i, [(t[0]+ii[0], t[1]+ii[1]) for ii in ind]) for t in trails]
        trails = [e for t in trails for e in t]
    suniq += len(set(trails))
    s += len(trails)

# part A
print(suniq)

# part B
print(s)
