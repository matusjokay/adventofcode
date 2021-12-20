#!/usr/bin/env python3


def printd(dots, zeros=True):
    print(''.join(''.join([str(x) if x or zeros else ' ' for x in y])+'\n' for y in dots))


foldx = lambda dots, flip: [*zip(*foldy([*zip(*dots)], flip))]
def foldy(dots, flip):  
    up, bo = dots[:flip], dots[:flip:-1]
    for y in range(len(up)-1, -1, -1):
        up[y] = [up[y][i] or bo[y][i] for i in range(len(up[y]))]
    return up
    #return [[up[y][i] or bo[y][i] for i in range(len(up[y]))] for y in range(len(up)-1, -1, -1)][::-1]


def do_day13(instr, dots):
    for ins in instr:
        dots = ins[0](dots, ins[1])
    return dots


dots = []
with open('input.txt') as f:
    lines = f.read().splitlines()
    coord, _instr = lines[:lines.index('')], lines[lines.index('')+1:]

    coord = [[int(_d) for _d in d.split(',')] for d in coord]
    maxx, maxy = [max(v)+1 for v in zip(*coord)]
    dots = [[1 if [x,y] in coord else 0 for x in range(maxx)] for y in range(maxy)]

    instr = []
    for i in _instr:
        f, v = i.split('fold along ')[1].split('=')
        instr.append((foldx if f == 'x' else foldy, int(v)))
        
#part A    
print(sum((sum(y) for y in do_day13(instr[:1], dots))))
#part B
printd(do_day13(instr, dots), False)
