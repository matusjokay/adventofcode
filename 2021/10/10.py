#!/usr/bin/env python3


from functools import reduce


def validate(line):
    weights = {'<': 4, '{': 3, '(': 1, '[': 2, '>': 25137, '}': 1197, ')': 3, ']': 57}

    stack = []
    for c in line:
        if c in ('<', '{', '(', '['):
            stack.insert(0, c)
            continue

        # part A
        if ord(c) - ord(stack.pop(0)) not in (1,2):
            return weights[c], 0

    # part B
    return 0, reduce(lambda x,y: x*5 + weights[y], stack, 0)


lines = open('input.txt').read().splitlines()
partA, partB = zip(*map(validate, lines))
partB = sorted(partB, reverse=True)
# 1/2 elms in partB are 0 (for partA), so median is Q25 of reversed partB
print(sum(partA), partB[len(partB)//4])
