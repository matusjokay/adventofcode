#!/bin/env python3


eq = []
with open('13.input.txt') as f:
    while True:
        a = f.readline().strip().split(': ')[1].split(', ')
        a = list(map(lambda x: int(x.split('+')[1]), a))
        b = f.readline().strip().split(': ')[1].split(', ')
        b = list(map(lambda x: int(x.split('+')[1]), b))
        prize = f.readline().strip().split(': ')[1].split(', ')
        prize = list(map(lambda x: int(x.split('=')[1]), prize))
        eq.append(([a[0], b[0], prize[0]], [a[1], b[1], prize[1]]))
        if not f.readline():
            break


def solve(e1, e2, c=0):
    z = e1[1]*e2[0] - e2[1]*e1[0]
    x = divmod((e2[2]+c)*e1[1] - (e1[2]+c)*e2[1], z)
    y = divmod((e1[2]+c)*e2[0] - (e2[2]+c)*e1[0], z)
    if x[1] or y[1]:
        return 0
    return 3*x[0]+y[0]


print('part A:', sum([solve(*e) for e in eq]))
print('part B:', sum([solve(*e, 10000000000000) for e in eq]))
