#!/usr/bin/env python3


FILE = 'input.txt'


with open(FILE) as f:
    lines = f.read().splitlines()


def part1(lines):
    gama = [1 if sum([1 for l in lines if l[i] == '1']) >= len(lines)/2 else 0 for i in range(len(lines[0]))]

    gama = int(''.join(map(str,gama)), 2)
    eps = 2**len(lines[0]) - gama - 1

    return gama * eps


def reduc(lines, majority = True):
    symbol_order = [chr(majority + ord('0')), chr(majority ^ 1 + ord('0'))]

    ind = 0
    while len(lines) > 1:
        sym = symbol_order[0] if sum([1 for l in lines if l[ind] == '1']) < len(lines)/2 else symbol_order[1]
        lines = [l for l in lines if l[ind] == sym]
        ind += 1

    return lines[0]


def part2(lines):
    oxy = reduc(lines, majority = True)
    co2 = reduc(lines, majority = False)
    return int(oxy, 2) * int(co2, 2)


print(part1(lines))
print(part2(lines))
