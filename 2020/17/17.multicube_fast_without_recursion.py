from collections import defaultdict
from itertools import product
from functools import reduce
from timeit import timeit


c = [[int(c) for c in line.strip().replace('.','0').replace('#','1')] for line in open('input.txt')]


def create_cubes(xy, dim=3):
    c = defaultdict(lambda: 0)

    for x,y in product(range(len(xy)), range(len(xy[0]))):
        if xy[x][y]:
            c[tuple([x,y] + [0 for _ in range(dim-2)])] = xy[x][y]
    
    return c


def active_neighbors(cub, coord):
    summ = sum([cub[c] for c in product(*[range(x-1,x+2) for x in coord])])
    return summ - 1 if cub[coord] else summ


def do_new_state(cubes, min_coord, max_coord):
    new_cubes = defaultdict(lambda: 0)
    dim = len(list(cubes.keys())[0])
    ranges = [range(x-1, y+2) for x, y in zip(min_coord, max_coord)]

    coords = (c for c
              in product(*ranges)
              if all([x <= y+1 for x, y in zip(c, max_coord)]))

    for c in coords:
        act = active_neighbors(cubes, c)

        if act == 3:
            new_cubes[c] = 1
        elif act == 2 and cubes[c]:
            new_cubes[c] = 1

    return new_cubes
        

def iterate_cubes(input_data, cube_dim=2):
    cubes = create_cubes(input_data, cube_dim)
    
    for i in range(6):
        max_coord = [max(x) for x in zip(*cubes.keys())]
        min_coord = [min(x) for x in zip(*cubes.keys())]
        #print(min_coord, max_coord)
        cubes = do_new_state(cubes, min_coord, max_coord)
        
    return cubes


# part 0 :)
#print(timeit('print(len(iterate_cubes(c,2)))', globals=globals(), number=1))
# part 1
print(timeit('print(len(iterate_cubes(c,3)))', globals=globals(), number=1))
# part 2
print(timeit('print(len(iterate_cubes(c,4)))', globals=globals(), number=1))
# part 3 :) :)
#print(timeit('print(len(iterate_cubes(c,5)))', globals=globals(), number=1))
# part 4 :) :) :)
#print(timeit('print(len(iterate_cubes(c,6)))', globals=globals(), number=1))
