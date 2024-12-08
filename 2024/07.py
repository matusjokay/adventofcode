#!/bin/env pypy


from itertools import product
from functools import reduce
from operator import add, mul


f = [[map(int,l.split()) for l in line.strip().split(': ')] for line in open('07.input.txt')]


def test(e, op=None):
    ops = [mul, add] if not op else [mul, add, op]
    r = [reduce(lambda x,y: (x[1](x[0], y[0]), y[1]), zip(e[1], p+(None,)), (0, add))[0] for p in product(ops, repeat=len(e[1])-1)]
    return filter(lambda x: e[0][0] == x, r)


print(sum([i[0][0] for i in filter(lambda x: x[0][0] in test(x), f)]))
print(sum([i[0][0] for i in filter(lambda x: x[0][0] in test(x, lambda x,y: int(str(x)+str(y))), f)]))
