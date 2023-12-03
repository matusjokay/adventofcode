#!/usr/bin/env python3

import re

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

# part A

r = [max(map(int, re.findall(r"(\d+) red", l))) for l in lines]
g = [max(map(int, re.findall(r"(\d+) green", l))) for l in lines]
b = [max(map(int, re.findall(r"(\d+) blue", l))) for l in lines]

print(sum([i+1 if r[i] <= 12 and g[i] <= 13 and b[i] <= 14 else 0 for i in range(len(r))]))


# part B

print(sum([r[i]*g[i]*b[i] for i in range(len(r))]))
