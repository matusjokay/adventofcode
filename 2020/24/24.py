#!/bin/env python3


from collections import defaultdict


def part1(tiles):
    res = defaultdict(lambda: 'white')

    for t in tiles:
        coord = [0, 0]
        t = list(t)
        while t:
            direct = t.pop(0)
            if direct in ('s', 'n'):
                direct += t.pop(0)

            if direct == 'e':
                coord[0] += 2
            elif direct == 'w':
                coord[0] -= 2
            elif direct == 'ne':
                coord[0] += 1
                coord[1] -= 1
            elif direct == 'nw':
                coord[0] -= 1
                coord[1] -= 1
            elif direct == 'se':
                coord[0] += 1
                coord[1] += 1
            elif direct == 'sw':
                coord[0] -= 1
                coord[1] += 1

        coord = tuple(coord)
        if coord not in res:
            res[coord] = 'black'
        else:
            if res[coord] == 'black': res[coord] = 'white'
            else: res[coord] = 'black'

    print(len([v for k,v in res.items() if v == 'black']))
    return res


def part2(tiles):
    for i in range(100):        
        new_tiles = defaultdict(lambda: 'white')

        neighbors = ((-2,0),(-1,-1),(1,-1),(2,0),(1,1),(-1,1))
        tiles_to_exam = set(((t[0]+n[0], t[1]+n[1]) for t in tiles for n in neighbors))
        for t in tiles_to_exam:
            summ = sum([1 for n in neighbors if tiles[(t[0]+n[0], t[1]+n[1])] == 'black'])
            if summ == 2 or (summ == 1 and tiles[t] == 'black'):
                new_tiles[t] = 'black'
        tiles = new_tiles

    print(len([v for k,v in tiles.items() if v == 'black']))
    return tiles


tiles = [line.strip() for line in open('input.txt')]
tiles = part1(tiles)
part2(tiles)
