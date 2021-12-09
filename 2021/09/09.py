#!/usr/bin/env python3


from more_itertools import stagger, collapse, padded, chunked
from collections import defaultdict
from functools import reduce
from math import copysign


def mark_area(ind, d, ll):
    if d[ind] == 9 or copysign(1, d[ind]) < 1:
        return set()

    d[ind] *= -1.0
    area = set([ind,])
    area.update(mark_area(ind+1, d, ll))
    area.update(mark_area(ind+ll, d,ll))
    if ind - 1 >= 0:
        area.update(mark_area(ind-1, d, ll))
        area.update(mark_area(ind-ll, d, ll))

    return area


def day9(nums, line_len):
    # part A
    num = [*stagger(nums, offsets=[-line_len,-1,0,1,line_len], longest=True, fillvalue=9)]
    low = list(((ind, e[2]+1) for ind, e in enumerate(num) if e[0]+e[1]+e[3]+e[4] > 4*e[2]))
    print(sum([*zip(*low)][1]))

    # part B
    d = defaultdict(lambda: 9)
    d.update([e for e in enumerate(nums)])
    len_areas = [len(mark_area(ind[0], d, line_len)) for ind in low]
    print(reduce(lambda x,y: x*y, (sorted(len_areas)[-3:])))


with open('input.txt') as f:
    nums = [[*map(int,list(line))] for line in f.read().splitlines()]
    line_len = len(nums[0]) + 1
    nums = [padded(n, 9, line_len) for n in nums]
    nums = [*collapse(nums)]

day9(nums, line_len)
