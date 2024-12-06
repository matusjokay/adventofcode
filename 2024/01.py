#!/bin/env python3

from collections import Counter

data = open("01.input.txt").readlines()
data = [i.strip().split("   ") for i in data]
data = list(zip(*data))
data = (list(sorted(map(int, data[0]))), list(sorted(map(int, data[1]))))

# part A
print(sum([abs(a-b) for a,b in zip(data[0], data[1])]))

# part B
c = Counter(data[1])
print(sum(map(lambda x: x*c[x], data[0])))
