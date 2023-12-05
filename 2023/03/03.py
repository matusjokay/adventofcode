#!/usr/bin/env python3

import re

# read input map
f = [line.strip() for line in open('input.txt')]


# part A

def connected(match: re.Match, line: int, m: list[list[str]]) -> bool:
    # create initial neighbours coordinates for the number based on its span
    nghbrs = [(match.span()[0]-1, line), (match.span()[1], line)]
    nghbrs += [(i, line-1) for i in range(match.span()[0]-1, match.span()[1]+1)]
    nghbrs += [(i, line+1) for i in range(match.span()[0]-1, match.span()[1]+1)]
    # filter out coordinates out of the map
    nghbrs = filter(lambda n: n[0] >= 0 and n[0] < len(m[0]) and n[1] >= 0 and n[1] < len(m), nghbrs)
    # filter only those neighbours which are special symbols
    nghbrs = list(filter(lambda n: m[n[1]][n[0]] != '.', nghbrs))
    # if the number is not adjacent to a symbol, @nghbrs is an empty list
    return True if nghbrs else False

# find all numbers in the input
m = [(match, i) for i, l in enumerate(f) for match in re.finditer(r'(\d+)', l)]
# process all numbers: get only numbers adjacent to a symbol
print(sum([int(match[0].group()) if connected(match[0], match[1], f) else 0 for match in m]))


# part B

def gear(x: int, y: int, m: list[list[str]], nums: dict[tuple[int,int],str]) -> int:
    # create initial neighbours coordinates for the star
    nghbrs = [(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1)]
    # filter out coordinates out of the map
    nghbrs = filter(lambda n: n[0] >= 0 and n[0] < len(m[0]) and n[1] >= 0 and n[1] < len(m), nghbrs)
    # filter only those star's neighbours which are digits (i.e. part of some number)
    nghbrs = list(filter(lambda n: m[n[1]][n[0]].isdigit(), nghbrs))

    # create set of numbers corresponding to filtered coordinates
    ret = list(set(map(lambda n: int(nums[n]), nghbrs)))
    # return gear ratio
    return 0 if len(ret) == 1 else ret[0] * ret[1]

# for each input number create a mapping between its coordinates and the number itself
nums = {(k, line): match.group() for match, line in m for k in range(*match.span())}
# find all specials
stars = [(match, i) for i, l in enumerate(f) for match in re.finditer(r'(\*+)', l)]
# find all stars in the input
stars = [(match, i) for i, l in enumerate(f) for match in re.finditer(r'(\*+)', l)]
# process stars
print(sum([gear(match[0].span()[0], match[1], f, nums) for match in stars]))
