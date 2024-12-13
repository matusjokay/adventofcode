#!/bin/env python3


from collections import defaultdict


d = defaultdict(lambda: ' ')
for row, line in enumerate(open('12.input.txt')):
    for col, c in enumerate(line.strip()):
        d.update({(row,col): [c, False]}) # plant type and processed flag


# part A

ind = ((0,1), (1,0), (-1,0), (0,-1))
def get_region(c):
    if d[c][1]:
        return (0, [])

    d[c][1] = True
    neigh_all = list(filter(lambda x: d[x][0] == d[c][0], [(c[0]+ii[0], c[1]+ii[1]) for ii in ind]))
    neigh_active = [cc for cc in neigh_all if not d[cc][1]]
    r = [get_region(cc) for cc in neigh_active]
    s = [0, []] # (area, perimeter)
    for rr in r:
        s[0] += rr[0]
        s[1] += rr[1]
    return (s[0]+4-len(neigh_all), s[1]+[c])

res = []
for coord, c, done in [(coord, c, done) for coord, (c, done) in d.items()]:
    if d[coord][1]:
        continue
    res += (get_region(coord),)

print(sum([r[0] * len(r[1]) for r in res]))


# part B

# from each area filter outer and inner corners
# return their count
cors = (((0,-1),(-1,0),(-1,-1)), ((-1,0),(0,1),(-1,1)), ((0,1),(1,0),(1,1)), ((1,0),(0,-1),(1,-1)))
def corners(c):
    out = list(filter(lambda x: d[x[0]][0] != d[c][0] and d[x[1]][0] != d[c][0], [((c[0]+ii[0][0], c[1]+ii[0][1]),(c[0]+ii[1][0],c[1]+ii[1][1])) for ii in cors]))
    inn = list(filter(lambda x: d[x[0]][0] == d[c][0] and d[x[1]][0] == d[c][0] and d[x[2]][0] != d[c][0], [((c[0]+ii[0][0], c[1]+ii[0][1]),(c[0]+ii[1][0],c[1]+ii[1][1]),(c[0]+ii[2][0],c[1]+ii[2][1])) for ii in cors]))
    return len(out+inn)

# sum the corners in all areas together; use list of areas from the part A
print(sum([sum([corners(rr) for rr in r[1]])*len(r[1]) for r in res]))
