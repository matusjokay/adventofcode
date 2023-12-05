#!/usr/bin/env python3

import re

# x, y: coordinates, m: input map, nums: coords -> num mapping, ver: 'A' or 'B'
def do_neighbors(x, y, m, nums, ver):
    # create and filter coordinates of neighbors
    nghbrs = [(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1)]
    nghbrs = filter(lambda n: n[0] >= 0 and n[0] < len(m[0]) and n[1] >= 0 and n[1] < len(m), nghbrs)
    nghbrs = list(filter(lambda n: m[n[1]][n[0]].isdigit(), nghbrs))

    # create set of numbers corresponding to filtered coordinates
    # If star is not a gear, there is only one number in a list, so append zero to get
    # two elements in a @ret and resulting zero in multiplication ret[0]*ret[1]
    ret = list(set(map(lambda n: int(nums[n]), nghbrs))) + [0]

    return ret[0] * ret[1] if ver == 'B' else sum(ret)


f = [line.strip() for line in open('input.txt')]

# find all numbers in the input
m = [(match, i) for i, l in enumerate(f) for match in re.finditer(r'(\d+)', l)]
# for each input number create a mapping between its coordinates and the number itself
nums = {(k, line): match.group() for match, line in m for k in range(*match.span())}
# find all specials in the input
specs = [(match, i) for i, l in enumerate(f) for match in re.finditer(r'([^0-9.]+)', l)]

print(sum([do_neighbors(match[0].span()[0], match[1], f, nums, 'A') for match in specs]))
print(sum([do_neighbors(match[0].span()[0], match[1], f, nums, 'B') for match in specs]))
