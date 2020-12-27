#!/bin/env python3


cups = [int(c) for c in open('input.txt').readline().strip()]


def game(cups, cnt = 100):
    ind = 0
    for i in range(cnt):
        pick = cups[ind]
        three0 = cups.pop(ind+1 if ind+1 < len(cups) else 0)
        three1 = cups.pop(ind+1 if ind+1 < len(cups) else 0)
        three2 = cups.pop(ind+1 if ind+1 < len(cups) else 0)

        zero_ind = False
        if ind+1 >= len(cups):
            zero_ind = True

        destination = pick - 1 if pick - 1 else len(cups)+3
        if destination==three0 or destination==three1 or destination==three2:
            destination = destination - 1 if destination - 1 else len(cups)+3
        if destination==three0 or destination==three1 or destination==three2:
            destination = destination - 1 if destination - 1 else len(cups)+3
        if destination==three0 or destination==three1 or destination==three2:
            destination = destination - 1 if destination - 1 else len(cups)+3
        destination_ind = (cups.index(destination)+1) % len(cups)

        cups.insert(destination_ind, three2)
        cups.insert(destination_ind, three1)
        cups.insert(destination_ind, three0)

        if zero_ind:
            ind = 0
        elif destination_ind > ind:
            ind = (ind+1) % len(cups)
        else:
            ind = (ind+4) % len(cups)


    ind_1 = cups.index(1)
    if cnt <= 100:
        res = cups[(ind_1+1) % len(cups)]
        for i in range(1,len(cups)-1):
            res *= 10
            res += cups[(i+ind_1+1) % len(cups)]
        return res
    else:
        return cups[(ind_1+1) % len(cups)], cups[(ind_1+2) % len(cups)]


print(game(cups[:]))

for i in range(max(cups)+1, 1000000+1):
    cups.append(i)
res = game(cups,10000000)
print(res[0], res[1], res[0]*res[1])
