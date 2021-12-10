#!/usr/bin/env python3


def validate(line):
    dic  = {'<': ('>', 4), '{': ('}', 3), '(': (')', 1), '[': (']', 2),
            '>': 25137, '}': 1197, ')': 3, ']': 57}

    partA = 0
    stack = []
    for c in line:
        if c in ('<', '{', '(', '['):
            stack.insert(0, c)
        else:
            cc = stack.pop(0)
            if c != dic[cc][0]:
                partA = dic[c]
                stack = None
                break

    partB = 0
    while stack:
        c = stack.pop(0)
        partB = 5 * partB + dic[c][1]

    return partA, partB


def day10(lines):
    partA, partB = zip(*map(validate, lines))
    partB = sorted(partB)
    partB = partB[len(partB) - partB[::-1].index(0):] # remove zeros
    print(sum(partA), partB[len(partB)//2])


FILE = 'input.txt'
with open(FILE) as f:
    lines = f.read().splitlines()

day10(lines)
