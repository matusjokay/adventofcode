#!/usr/bin/env python3

with open('input.txt') as f:
    change_plus = 0
    prev = int(f.readline().strip())

    while line := f.readline().strip():
        num = int(line)

        if num - prev > 0:
            change_plus += 1
        prev = num

    print(change_plus)

with open('input.txt') as f:
    change_plus = 0
    prev = int(f.readline().strip())
    prev2 = int(f.readline().strip())
    prev3 = int(f.readline().strip())

    while line := f.readline().strip():
        num = int(line)

        if num - prev > 0:
            change_plus += 1
        prev, prev2, prev3 = prev2, prev3, num

    print(change_plus)
