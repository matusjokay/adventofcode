#!/usr/bin/env python3


nums = [*map(int, open('input.txt').readline().split(','))]
print(min([sum([abs(n-pos) for n in nums]) for pos in range(max(nums))]))
print(min([sum([sum(range(abs(n-pos)+1)) for n in nums]) for pos in range(max(nums))]))
