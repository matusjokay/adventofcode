#!/usr/bin/env python3

#nums = [*map(int, open('example.txt'))]
#print(nums)

FILE = 'input.txt'

with open(FILE) as f:
    horizontal = 0
    depth = 0

    while line := f.readline().strip():
        line = line.split()
        if line[0] == 'forward':
            horizontal += int(line[1])
        elif line[0] == 'down':
            depth += int(line[1])
        elif line[0] == 'up':
            depth -= int(line[1])

    print(horizontal * depth)


with open(FILE) as f:
    horizontal = 0
    depth = 0
    aim = 0

    while line := f.readline().strip():
        line = line.split()
        if line[0] == 'forward':
            horizontal += int(line[1])
            depth += aim * int(line[1])
        elif line[0] == 'down':
            aim += int(line[1])
        elif line[0] == 'up':
            aim -= int(line[1])

    print(horizontal * depth)
