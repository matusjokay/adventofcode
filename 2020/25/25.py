#!/bin/env python3


N = 20201227
p, q = [int(x) for x in open('input.txt').readlines()]
#print(p, q, N)


def brute_force(p, N):
    i = 1
    mul = 1
    while (mul * 7) % N != p:
        i += 1
        mul = (mul*7) % N
    return i


x = brute_force(p, N)
y = brute_force(q, N)
res = 1
for i in range(y):
    res = (res*p) % N
print(res)

