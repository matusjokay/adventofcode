#!/usr/bin/env python3


from functools import reduce


def validate(line):
    dic  = {'<': ('>', 4), '{': ('}', 3), '(': (')', 1), '[': (']', 2),
            '>': 25137, '}': 1197, ')': 3, ']': 57}

    stack = []
    for c in line:
        if c in ('<', '{', '(', '['):
            stack.insert(0, c)
            continue

        # part A
        if c != dic[stack.pop(0)][0]:
            return dic[c], 0

    # part B
    return 0, reduce(lambda x,y: x*5 + dic[y][1], [0]+stack)


FILE = 'input.txt'
with open(FILE) as f:
    lines = f.read().splitlines()

partA, partB = zip(*map(validate, lines))
partB = sorted(partB, reverse=True)
# 1/2 elms in partB are 0 (for partA), so median is Q25 of reversed partB
print(sum(partA), partB[len(partB)//4])
