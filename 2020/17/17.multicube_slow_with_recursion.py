from collections import defaultdict
from itertools import product
from functools import reduce


c = [[int(c) for c in line.strip().replace('.','0').replace('#','1')] for line in open('in.txt')]


def create_cubes(xy, dim=3):
    c = defaultdict(lambda: 0)

    for x in range(len(xy)):
        for y in range(len(xy[0])):
            coord = tuple([x,y] + [0 for _ in range(dim-2)])
            if xy[x][y]:
                c[coord] = xy[x][y]
    
    return c


def active_neighbors(cub, coord, depth = 0):
    summ = 0
    if not depth and cub[coord]:
        summ -= 1

    dim = len(list(cub.keys())[0])
    for c in (coord[depth]-1, coord[depth], coord[depth]+1):
        new_coord = tuple(list(coord)[:depth]+[c]+list(coord)[depth+1:])
        
        if depth < dim-1:        
            summ += active_neighbors(cub, new_coord, depth+1)
        else:
            summ += cub[new_coord]

    return summ


def do_new_state(cubes, min_coord, max_coord):
    new_cubes = defaultdict(lambda: 0)
    dim = len(list(cubes.keys())[0])
    ranges = [range(x-1, y+2) for x,y in zip(min_coord, max_coord)]

    coords = (c for c
              in product(*ranges)
              if all([x<=y+1 for x,y in zip(c,max_coord)]))

    for c in coords:
        act = active_neighbors(cubes, c)

        if act == 3:
            new_cubes[c] = 1
        elif act == 2 and cubes[c]:
            new_cubes[c] = 1

    return new_cubes
        

def iterate_cubes(input_data, cube_dim=3):
    cubes = create_cubes(input_data, cube_dim)
    
    for i in range(6):
        max_coord = [max(x) for x in zip(*cubes.keys())]
        min_coord = [min(x) for x in zip(*cubes.keys())]
        #print(min_coord, max_coord)
        cubes = do_new_state(cubes, min_coord, max_coord)
        
    return cubes


# part 1
print(len(iterate_cubes(c,3)))
# part 2
print(len(iterate_cubes(c,4)))
