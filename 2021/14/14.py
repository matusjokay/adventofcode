#!/usr/bin/env python3


from itertools import pairwise
from collections import Counter


pairs = lambda poly: [''.join(pp for pp in p) for p in pairwise(poly)]
compute = lambda poly, i: sum([rules[p][i] for p in pairs(poly)], Counter())
    

def compute_10_round_str(poly):
    last = poly[-1]
    for i in range(10):
        poly = ''.join(rules[p][0][:-1] for p in pairs(poly)) + last
    return poly


def do_day14(poly, rules, ind):
    c = Counter()
    for p in pairs(poly):
        # compute 40-round counter only for input pairs
        if not rules[p][ind] and ind == 5:
            rules[p][ind] = compute(rules[p][3], 4)
        c += rules[p][ind]
    c[poly[-1]] += 1
    return c.most_common()[0][1] - c.most_common()[-1][1]


rules = dict()
with open('input.txt') as f:
    poly = f.readline().strip()
    f.readline()
    for l in f.read().splitlines():
        l = l.split(' -> ')
        rules[l[0]] = list((l[0][0]+l[1]+l[0][1],0,0,0,0,0,0))

    # precompute strings for 10 and 20 rounds
    for p in rules:
        # p[1] 10 rounds str, p[2] 10 rounds counter
        rules[p][1] = compute_10_round_str(p)
        rules[p][2] = Counter(rules[p][1])
        rules[p][2][p[-1]] -= 1

        # p[3] 20 rounds str, p[4] 20 rounds counter
        rules[p][3] = compute_10_round_str(rules[p][1])
        rules[p][4] = Counter(rules[p][3])
        rules[p][4][p[-1]] -= 1
    

print(do_day14(poly, rules, 2))
print(do_day14(poly, rules, 5))
