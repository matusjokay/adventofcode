#!/bin/env python3


from copy import deepcopy as copy


coord = {'^':(0,-1), '>':(1,0), 'v':(0,1), '<':(-1,0)}
dirs = {'^':'>', '>':'v', 'v':'<', '<':'^'}


def walk(orig, start, obstacle):
    # init dataset
    m = copy(orig)
    pos = [k for k in m if m[k] == start][0]
    if obstacle:
        m[obstacle] = '#'

    traversed = set()
    try:
        while True:
            # load direction
            direct = m[pos]
            # while not an obstacle
            while m[(pos[0]+coord[direct][0],pos[1]+coord[direct][1])] != '#':
                # cycle detection
                if (pos, direct) in traversed:
                    return False
                # mark position as traversed
                traversed.add((pos, direct))
                m[pos] = 'X'
                pos = (pos[0]+coord[direct][0],pos[1]+coord[direct][1])
            # change direction
            m[pos] = dirs[direct]
    except:
        # mark the last position before falling out of the map as traversed
        m[pos] = 'X'

    # return coordinates of traversed points when falling out of the map
    return [x[0] for x in m.items() if x[1] == 'X']


with open('06.input.txt') as f:
    m = {(i, j): c for j, line in enumerate(f) for i, c in enumerate(line.strip())}


# part A
path = walk(m, '^', None)
print(len(path))


# part B
print(sum([0 if walk(m, '^', p) else 1 for p in path]))
