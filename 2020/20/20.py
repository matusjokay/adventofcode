#!/bin/env python3


from collections import Counter
from math import sqrt
import re


def read_input(fname):
    tiles = dict()
    tiles_orig = dict()
    for line in open(fname):
        line = line.strip()

        if line.startswith('Tile'):
            tile = []
            tid = line.split(' ')[1][:-1]
        elif not line:
            tiles_orig[tid] = tile
            tiles[tid] = tile2coord(tile)
        else:
            tile.append(line)

    return tiles, tiles_orig


def flip_vertical(tile):
    return [''.join(reversed(line)) for line in tile]


def rotate_right(tile):
    return [''.join(reversed(line)) for line in zip(*tile)]


def tile2coord(tile):
    edges = []

    edges.append(int(tile[0].replace('#','1').replace('.','0'),2)) # top border
    edges.append(int(''.join(['1' if x[-1]=='#' else '0' for x in tile]),2)) # right border
    edges.append(int(''.join(['1' if x=='#' else '0' for x in tile[-1][::-1]]),2)) # bottom border
    edges.append(int(''.join(['1' if x[0]=='#' else '0' for x in tile[::-1]]),2)) # left border

    edges.append(int(''.join(['1' if x=='#' else '0' for x in tile[0][::-1]]),2)) # vertical flip top
    edges.append(int(''.join(['1' if x[0]=='#' else '0' for x in tile]),2)) # vertical flip left
    edges.append(int(tile[-1].replace('#','1').replace('.','0'),2)) # vertical flip bottom border
    edges.append(int(''.join(['1' if x[-1]=='#' else '0' for x in tile[::-1]]),2)) # vertical flip right

    return edges


def find_tail(border, ts, image):
    tail = [tail for tail in ts if border in ts[tail]]
    if len(tail) != 1:
        print('find_tail(): find more than one candidate for a tail!')
        print(f'{tail} {border} {ts}')
    return tail[0]


ts, ts_orig = read_input('input.txt')

ts_all = []
for v in ts.values():
    ts_all += v
count = Counter(ts_all)

# part 1
mult = 1
corners = []
for key, val in ts.items():
    a = sorted(Counter([count[x] for x in val]).values())
    if len(a) > 1 and a[0] == a[1]:
        mult *= int(key)
        corners.append(key)
print(mult, '\n')

# part 2
# check corners orientation; search for a topleft corner
topleft_corner = None
for c in corners:
    if (1,2,2,1) == (count[ts[c][0]],count[ts[c][1]],count[ts[c][2]],count[ts[c][3]]):
        topleft_corner = c
if not topleft_corner:
    print("TODO: topleft corner not found!")
    # TODO: rotate any corner to topleft position

image = dict()
# we believe in order of inserted keys
image[topleft_corner] = ts_orig[topleft_corner]
# next border to find in a row; examine set of left borders
next_right = ts[topleft_corner][1]
# next border to find in a col; examine set of top borders
next_bottom = ts[topleft_corner][2]
del ts[topleft_corner]

img_len = int(sqrt(len(ts_orig)))
ind = 1
while ts:
    # searched border must be the same as top border if tail is the first in the line
    # searched border must be the same as left border if tail is the next in the line
    border_index = 4 if ind % img_len == 0 else 5
    border_to_find = next_bottom if ind % img_len == 0 else next_right

    #print(f'{ind} {border_index} {border_to_find}')
    tail_id = find_tail(border_to_find, ts, image)
    # if border orientation do not match, transform a tile
    # if it is flipped
    if border_to_find in ts[tail_id][:4]:
        ts[tail_id] = ts[tail_id][4:]+ts[tail_id][:4]
        ts_orig[tail_id] = flip_vertical(ts_orig[tail_id])
    # if it is rotated
    while ts[tail_id][border_index] != border_to_find:
        ts[tail_id] = [ts[tail_id][3]]+ts[tail_id][:3]+ts[tail_id][5:]+[ts[tail_id][4]]
        ts_orig[tail_id] = rotate_right(ts_orig[tail_id])

    image[tail_id] = ts_orig[tail_id]
    ts[tail_id] = tile2coord(ts_orig[tail_id])
    if ind % img_len == 0:
        next_bottom = ts[tail_id][2]
    next_right = ts[tail_id][1]
    del ts[tail_id]

    ind += 1

# remove borders of tiles and get them together
res = []
img = list(image.values())
for i in range(img_len):
    for x in range(1, 9):
        line = ''
        for j in range(img_len):
            line += ''.join(img[i*img_len+j][x][1:-1])
        res += [line]

for i in range(8):
    if i == 4:
        res = flip_vertical(res)
    res = rotate_right(res)

    r0 = re.finditer(r'..................#.', '\n'.join(res))
    r1 = re.finditer(r'#....##....##....###', '\n'.join(res))
    r2 = re.finditer(r'.#..#..#..#..#..#...', '\n'.join(res))

    line_len = len(res[0])+1
    rr0 = [m.span()[0]//line_len for m in r0]
    rr1 = [m.span()[0]//line_len for m in r1]
    rr2 = [m.span()[0]//line_len for m in r2]
    monsters = [m for m in rr1 if m+1 in rr2 and m-1 in rr0]

    if monsters:
        print(''.join(res).count('#')-len(monsters)*15, monsters)
