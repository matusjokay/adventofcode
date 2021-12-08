#!/usr/bin/env python3

def decode(digits, numbers):
        d = [None for i in range(10)]

        # digits '1', '4', '7', '8' based on number of segments
        for num in digits:
            if len(num) == 2:
                d[1] = num
            elif len(num) == 3:
                d[7] = num
            elif len(num) == 4:
                d[4] = num
            elif len(num) == 7:
                d[8] = num

        # other digits based on set operations
        for num in digits:
            if num in d:
                continue
            if (d[8]-d[1]).issubset(num):
                d[6] = num
            if (d[7] | (d[4])).issubset(num):
                d[9] = num

        for num in digits:
            if num in d:
                continue
            if ((d[6]-d[4]) | d[1]).issubset(num):
                d[0] = num
            if (d[4]-d[7]).issubset(num):
                d[5] = num

        for num in digits:
            if num in d:
                continue
            if (d[7] | (d[8]-d[0])).issubset(num):
                d[3] = num

        # the last digit '2'
        d[2] = [num for num in digits if num not in d][0]

        # return decoded number
        return int(''.join(str(c) for c in [d.index(n) for n in numbers]))


lines = [l.split(' | ') for l in open('example.txt')]
print(sum(len([ll for ll in l[1].split() if len(ll) in (2,3,4,7)]) for l in lines))
print(sum(decode([set(s) for s in l[0].split()], [set(s) for s in l[1].split()]) for l in lines))
