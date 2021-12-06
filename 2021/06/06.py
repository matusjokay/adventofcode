#!/usr/bin/env python3

from functools import lru_cache

@lru_cache(maxsize=None)
def f8(n):
    if n - 9 > 0:
        return 1 + sum([f8(i) for i in range(n-9, 0, -7)])
    return 1


def do_day6(nums, cnt):
    return len(nums) + sum([sum([f8(i) for i in range(start, 0, -7)]) for start in [cnt-n for n in nums]])


nums = [*map(int, open('input.txt').readline().split(','))]

print(do_day6(nums, cnt = 80))
print(do_day6(nums, cnt = 256))
