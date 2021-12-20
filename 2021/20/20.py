#!/usr/bin/env python3


from collections import defaultdict
from math import sqrt


def neigh(x, y, d):
    return [d[(x-1,y-1)], d[(x-1,y)], d[(x-1,y+1)], d[(x,y-1)],
            d[(x,y)], d[(x,y+1)], d[(x+1,y-1)], d[(x+1,y)], d[(x+1,y+1)]]


def day20(enhance, image, cnt):
    dim = int(sqrt(len(image)))

    for i in range(cnt):
        image = defaultdict(
                image.default_factory,
                {
                    (row,col) : enhance[int(''.join(map(str, neigh(row, col, image))), 2)]
                        for col in range(-1-i, dim+1+i)
                        for row in range(-1-i, dim+1+i)
                }
            )
        default = enhance[int(image.default_factory()) * 511]
        image.default_factory = lambda: default

    print(sum(image.values()))


d = defaultdict(lambda: 0)
with open('input.txt') as f:
    enhance = [*map(int, f.readline().replace('.','0').replace('#','1').strip())]
    f.readline()
    image = defaultdict(
            lambda:0,
            {
                (row,col) : int(l)
                    for row, line in enumerate(f.read().splitlines())
                    for col, l in enumerate(line.replace('.','0').replace('#','1'))
            }
        )

day20(enhance, image, cnt=2)
day20(enhance, image, cnt=50)
