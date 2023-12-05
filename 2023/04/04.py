#!/usr/bin/env python3

import re

m = [match.groups() for l in open('input.txt') for match in re.finditer(r'Card\s+\d+:((?:\s+\d+)+)\s+\|((?:\s+\d+)+)', l)]

# part A
wins = [len(set(map(int, g[0].split())) & set(map(int, g[1].split()))) for g in m]
print(sum(map(lambda n: 2**(n-1), filter(None, wins))))

# part B
c = [1 for _ in range(len(wins))]
for i in range(len(wins)-1):
    c[i+1:i+1+wins[i]] = [n + c[i] for n in c[i+1:i+1+wins[i]]]
print(sum(c))
