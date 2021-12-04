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
                    # mark num with sign, but zero is special one...
                    elm_index = row.index(n)
                    row[elm_index] = -n if n else -0xffffffff

                    # check actual row for win
                    if sum([1 if elm < 0 else 0 for elm in row]) == len(row):
                        winners[ind] = 1
                        break

                    # check actual col for win
                    if sum([1 if elm < 0 else 0 for elm in list(zip(*b))[elm_index]]) == len(row):
                        winners[ind] = 1
                        break

            # check win condition and return sum of unused elms of winner table
            # multiplied by winner num
            if test_fnc(winners):
                return n * sum([sum([elm if elm > 0 else 0 for elm in row]) for row in b])


print(play(lines, any))
print(play(lines, all))
