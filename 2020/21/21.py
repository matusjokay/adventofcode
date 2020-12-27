#!/bin/env python3


from copy import deepcopy
from collections import defaultdict


def read_input(fname):
    foods = []
    for line in open(fname):
        line = line.replace(',','')
        line = line[:-2].split(' (contains ')
        foods.append([set(line[0].split()), set(line[1].split())])
    return foods


# foods[0] - ingredients
# foods[1] - alergens
def part1(foods):
    identified_alerg = dict()
    # while there are not matched alergens
    while set.union(*[a[1] for a in foods]):
        # get list of foods with not matched alergens
        cand = [c for c in foods if c[1]]
        alerg = set.union(*[a[1] for a in cand])

        rrr = {a: set.intersection(*[c[0] for c in cand if a in c[1]]) for a in alerg}
        alerg = [(list(f)[0],a) for a,f in rrr.items() if len(f) == 1][0]
        identified_alerg[alerg[1]] = alerg[0]

        for i, f in enumerate(foods):
            if alerg[0] in f[0]:
                f[0].remove(alerg[0])
            if alerg[1] in f[1]:
                f[1].remove(alerg[1])

    res = sum([len(f[0]) for f in foods if f[0]])
    print(res)
   
    return identified_alerg


foods = read_input('input.txt')
alerg = part1(deepcopy(foods))


# part 2
[print(f'{v[1]},', end='') for v in sorted([(k, v) for k,v in alerg.items()])]
print()
