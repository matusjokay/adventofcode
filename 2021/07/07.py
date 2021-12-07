#!/usr/bin/env python3


def do(nums, fuel_cost):
    fuels = [sum([fuel_cost(n, pos) for n in nums]) for pos in range(max(nums))]
    print(fuels[fuels.index(min(fuels))])


nums = [*map(int, open('input.txt').readline().split(','))]
do(nums, lambda n,pos: abs(n-pos))
do(nums, lambda n,pos: sum(range(abs(n-pos)+1)))
