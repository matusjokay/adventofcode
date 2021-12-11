#!/usr/bin/env python3


def neigh(x, y, mapa):
    return filter(lambda n: n in mapa and mapa[n] > 0,
            [(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1)])


def flash(ind, mapa):
    for n in [*neigh(*ind, mapa)]:
        mapa[n] += 1
    mapa[ind] = 0
    return set(filter(lambda n: mapa[n] > 9, neigh(*ind, mapa)))


def do_day11(mapa):
    i = flcnt = 0
    while True:
        # increase by 1
        mapa = {k:v+1 for k,v in mapa.items()}

        # get all start points with value == 10
        fl = set(filter(lambda n: mapa[n] > 9, mapa))
        flcnt += len(fl)
        while fl:
            flfl = flash(fl.pop(), mapa)
            flcnt += len(flfl-fl)
            fl.update(flfl)

        i += 1
        if i == 100:
            print("Part A:", flcnt)
        if not any(mapa.values()):
            break
    print("Part B:", i)


mapa = {(x,y):int(h) for x,l in enumerate(open('input.txt'))
                     for y,h in enumerate(l.strip())}
do_day11(mapa)
