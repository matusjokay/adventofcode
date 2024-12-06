#!/bin/env python3

from collections import defaultdict
from functools import reduce
from itertools import permutations

# part A

d = defaultdict(lambda: set())
with open('05.input.txt') as f:
    while True:
        line = f.readline().strip().split('|')
        if not line[0]:
            break
        d[int(line[0])].add(int(line[1]))

    corr = []
    sum = 0
    for line in f.readlines():
        ll = list(map(int, line.split(',')))
        if not any([d[l[1]] & set(ll[:l[0]]) for l in enumerate(ll)]):
            sum += ll[len(ll)//2]
        else:
            corr.append(ll)
    print(sum)

# part B

sum = 0
for ll in corr:
    while True:
        err = [d[l[1]] & set(ll[:l[0]]) for l in enumerate(ll)]
        if not any(err):
            break
        for i_from, e in enumerate(err):
            if e:
                i_to = min(map(lambda x: ll.index(x), e))
                elm = ll[i_from]
                ll = ll[:i_from] + ll[i_from+1:]
                ll.insert(i_to, elm)
                break
    sum += ll[len(ll)//2]
print(sum)
