#!/usr/bin/env python3

#nums = [*map(int, open('example.txt'))]
#print(nums)

FILE = 'input.txt'

with open(FILE) as f:
    lines = f.read().splitlines()


'''
horiz = sum(int(l[-1]) for l in lines if l[0] == 'f')
down = sum(int(l[-1]) for l in lines if l[0] == 'd')
up = sum(int(l[-1]) for l in lines if l[0] == 'u')
return horiz * (down - up)
'''
def part1(lines):
    s = [sum(int(l[-1]) for l in lines if l[0] == c) for c in ['f', 'd', 'u']]
    return s[0] * (s[1] - s[2])


def part2(lines):
    horiz = depth = aim = 0
    for direct, n in ((l[0], int(l[-1])) for l in lines):
        if direct =='f':
            horiz += n
            aim += n * depth
        elif direct == 'u':
            depth -= n
        elif direct == 'd':
            depth += n
    return horiz * aim


print(part1(lines))
print(part2(lines))
