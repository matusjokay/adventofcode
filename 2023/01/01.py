#!/usr/bin/env python3

import re
from functools import reduce

fname = "input.txt"

# part A

print(sum([int((e[0] + e[-1])) for e in [re.findall(r"(\d)", line) for line in open(fname)] if e]))

# part B

m = {
    '1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9',
    'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9',
    }
mr = {k[::-1]: v for k, v in m.items()}

r = r"one|two|three|four|five|six|seven|eight|nine"
f1 = [re.findall(r"(?:\d|"+r+r")", line)[0] for line in open(fname)]
f2 = [re.findall(r"(?:\d|"+r[::-1]+r")", line[::-1])[0] for line in open(fname)]
print(reduce(lambda a, b: a + b, [int(m[e[0]] + mr[e[1]]) for e in zip(f1, f2)]))
