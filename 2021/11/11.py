#!/usr/bin/env python3


def neigh(x, y, mapa):
    return filter(lambda n: n in mapa and mapa[n] > 0,
            [(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1)])


def flash(ind, mapa):
    for n in [*neigh(*ind, mapa)]:
        mapa[n] += 1
    mapa[ind] = 0


def do_day11(mapa):
    i = cnt = 0
    while True:
        # increase by 1
        mapa = {k:v+1 for k,v in mapa.items()}

        cnt_new = True
        while cnt_new:
            # while there is/are point(s) with val > 9, flash
            cnt_new = len([flash(p, mapa) for p in filter(lambda n: mapa[n] > 9, mapa)])
            cnt += cnt_new

        i += 1
        if i == 100:
            print("Part A:", cnt)
        if not any(mapa.values()):
            break
    print("Part B:", i)


mapa = {(x,y):int(h) for x,l in enumerate(open('input.txt'))
                     for y,h in enumerate(l.strip())}
do_day11(mapa)
