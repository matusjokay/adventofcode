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


#########################################
#########################################
#########################################


nums = [*map(int, open('input.txt').readline().split(','))]

def do(nums, days):
    state = [nums.count(i) if i in nums else 0 for i in range(9)]
    for i in range(days):
        # each day:
        #    1 becomes 0, 2 becomes 1, 3 becomes 2, ..., 8 becomes 7
        #    0 becomes 6 and 7 becomes 6, too
        #    0 adds a new 8
        state = state[1:7] + [state[0]+state[7]] + [state[8]] + [state[0]]
    return sum(state)

print(do(nums, days=80))
print(do(nums, days=256))
