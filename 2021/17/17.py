#!/usr/bin/env python3


def partA(y1, y2):
    res = []
    for y in range(100):
        i = 1
        trian = 0
        vals = []
        while True:
            val = y * i - trian
            vals.append(val)
            if y2 >= val >= y1:
                res.append((y, max(vals)))
                break
            if val < y1:
                break

            trian += i
            i += 1
            
    print(max([*zip(*res)][1]))


def partB(x1, x2, y1, y2):
    res = set()
    for x in range(-100,400):
        for y in range(-100,100):
            diffx = x
            curx = 0
            diffy = y
            cury = 0
            while True:
                if x1 <= curx <= x2 and y1 <= cury <= y2:
                    res.add((x,y))
                    break
                if cury < y1:
                    break

                cury += diffy
                diffy -= 1
                curx += diffx
                if diffx:
                    diffx -= 1
    print(len(res))


#example target area: x=20..30, y=-10..-5
#target area: x=281..311, y=-74..-54

partA(-74, -54)
partB(281, 311, -74, -54)
