c = [[int(c) for c in line.strip().replace('.','0').replace('#','1')] for line in open('input.txt')]
#print(c)

def create_cubes(xy, x=101, y=101, z=101, w=101):
    '''
    coordinates: cube - z, cube[0] - x, cube[0][0] - y
    '''
    c = [[[[0 for y in range(y)] for x in range(x)] for z in range(z)] for w in range(w)]

    start_w = (w-1)//2
    start_z = (z-1)//2
    start_x = (x-1)//2 - (len(xy)-1)//2
    start_y = (y-1)//2 - (len(xy[0])-1)//2

    for x in range(len(xy)):
        for y in range(len(xy[0])):
            c[start_w][start_z][start_x+x][start_y+y] = xy[x][y]

    return c

def print_cubes(c1, c2=None):
    for z in range(len(c1)):
        print(f'z={z-(len(c1)-1)//2}')
        for x in range(len(c1[z])):
            for y in range(len(c1[z][x])):
                if c1[z][x][y] == 0:
                    print('.', end='')
                else:
                    print('#', end='')

            if c2 is not None:
                print(' <-- ', end='')
                for y in range(len(c2[z][x])):
                    if c2[z][x][y] == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                        
            print()

def active_neighbors(cubes, x, y, z, w):
    summ = 0
    for _w in range(w-1, w+2):
        for _z in range(z-1, z+2):
            for _x in range(x-1, x+2):
                for _y in range(y-1, y+2):
                    summ += cubes[_w][_z][_x][_y]
    if cubes[w][z][x][y]:
        summ -= 1
    return summ

#cubes = [create_cubes(c, 21, 21, 19), create_cubes(c, 21, 21, 19)]
dim = len(c)*6+1
cubes = [create_cubes(c, dim, dim, dim, dim), create_cubes(c, dim, dim, dim, dim)]
for i in range(6):
    state = cubes[i%2]
    new_state = cubes[(i+1)%2]

    for w in range(1, len(state)-1):
        for z in range(1, len(state[0])-1):
            for x in range(1, len(state[0][0])-1):
                for y in range(1, len(state[0][0][0])-1):
                    act = active_neighbors(state, x, y, z, w)
                    new_state[w][z][x][y] = state[w][z][x][y]
                    if state[w][z][x][y] and act not in (2,3):
                        new_state[w][z][x][y] = 0
                    if not state[w][z][x][y] and act == 3:
                        new_state[w][z][x][y] = 1
#print_cubes(cubes[0], cubes[1])

summ = 0
for w in range(len(cubes[0])):
    for z in range(len(cubes[0][0])):
        for x in range(len(cubes[0][0][0])):
            for y in range(len(cubes[0][0][0][0])):
                summ += cubes[0][w][z][x][y]
print(summ)
