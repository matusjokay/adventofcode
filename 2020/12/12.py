coord = [line.strip() for line in open('input.txt')]


def pivot_rotate(pivot, angle, rotation_dir):
    rot = (rotation_dir, -rotation_dir)
    for i in range(int(angle/90)):
        pivot[0], pivot[1] = pivot[1]*rot[0], pivot[0]*rot[1]
    return pivot


def move_ship(waypoint = None):
    manhattan=[0,0]
    
    if waypoint:
        pivot = waypoint
        pivot_coord = pivot
    else:
        pivot = manhattan
        pivot_coord = [1, 0]
    
    for c in coord:
        direct, size = c[0], int(c[1:])
        if direct == 'N':
            pivot[1] += size
        elif direct == 'S':
            pivot[1] -= size
        elif direct == 'E':
            pivot[0] += size
        elif direct == 'W':
            pivot[0] -= size
        elif direct == 'F':
            manhattan[0] += size * pivot_coord[0]
            manhattan[1] += size * pivot_coord[1]
        elif direct == 'R':
            pivot_coord = pivot_rotate(pivot_coord, size, 1)
        elif direct == 'L':
            pivot_coord = pivot_rotate(pivot_coord, size, -1)        
        #print(direct, size, manhattan, pivot, pivot_coord)
    return abs(manhattan[0])+abs(manhattan[1])


# part 1
print(move_ship())
# part 2
print(move_ship(waypoint=[10,1]))
