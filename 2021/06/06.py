#!/usr/bin/env python3

from functools import lru_cache

nums = [*map(int, open('input.txt').readline().split(','))]


@lru_cache(maxsize=None)
def f8(n):
    if n - 9 > 0:
        return 1 + sum([f8(i) for i in range(n-9, 0, -7)])
    return 1


#return len(nums) + sum([sum([f8(i) for i in range(start, 0, -7)]) for start in [cnt-n for n in nums]])
def do_day6(nums, cnt):
    s = 0
    start8 = [cnt-n for n in nums]
    for i in start8:
        s += sum([f8(j) for j in range(i, 0, -7)])
    return s + len(nums)


print(do_day6(nums, cnt = 80))
print(do_day6(nums, cnt = 256))
