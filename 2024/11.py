#!/bin/env python3


from functools import cache


@cache
def blink(s, dep):
    if not dep:
        return 1

    if s == '0':
        return blink(str(1), dep-1)
    elif len(s) % 2:
        return blink(str(int(s) * 2024), dep-1)

    return blink(s[:len(s)//2], dep-1) + blink(str(int(s[len(s)//2:])), dep-1)


stones = open('11.input.txt').read().split()

# part A
print(sum([blink(s, 25) for s in stones]))

# part B
print(sum([blink(s, 75) for s in stones]))
