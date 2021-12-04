#!/usr/bin/env python3

FILE = 'input.txt'

with open(FILE) as f:
    lines = f.read().splitlines()
    nums = [*map(int,lines[0].split(','))]

    bingo = []
    for ind in range(2, len(lines)-2, 6):
        bingo.append([list(map(int, l.split())) for l in lines[ind:ind+5]])


def play(lines, test_fnc):
    winners = [0 for i in range(len(bingo))]
    for n in nums:
        for ind, b in enumerate(bingo):
            for row in b:
                if n in row:
                    # mark num: change value num to -1
                    elm_index = row.index(n)
                    row[elm_index] = -1

                    # check actual row and col for win
                    if sum(row) == -len(row) or sum(list(zip(*b))[elm_index]) == -len(row):
                        winners[ind] = 1

                    # check win condition and return sum of unused elms of winner table
                    # multiplied by winner num
                    if test_fnc(winners):
                        return n * sum([sum([elm if elm > 0 else 0 for elm in row]) for row in b])


print(play(lines, any))
print(play(lines, all))
