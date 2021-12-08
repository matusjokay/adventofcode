#!/usr/bin/env python3

def decode(digits, numbers):
        d = [None for i in range(10)]

        # digits '1', '4', '7', '8' based on number of segments
        for i, l in [(1,2), (7,3), (4,4), (8,7)]:
            d[i] = [num for num in digits if len(num) == l][0]

        # other digits based on set operations
        for dig in digits:
            if len(dig) == 6:
                # 9 <-- ('8' - 'dig') intersect '4' is empty set
                if d[8] - dig - d[4]:
                    d[9] = dig
                # 6 <-- ('8' - 'dig') in '1'
                elif not d[8] - dig - d[1]:
                    d[6] = dig
                # 0 <-- ('8' - 'dig') not in '1'
                else:
                    d[0] = dig
            elif len(dig) == 5:
                # 3 <-- ('8' - 'dig') intersect '1' is empty set
                if len(d[8] - dig - d[1]) == 2:
                    d[3] = dig
                # 5 <-- ('8' - 'dig') not all in '4'
                elif d[8] - dig - d[4]:
                    d[5] = dig
                # 2 <-- ('8' - 'dig') all in '4'
                else:
                    d[2] = dig

        # return decoded number
        return int(''.join(str(c) for c in [d.index(n) for n in numbers]))


lines = [l.split(' | ') for l in open('input.txt')]
print(sum(len([ll for ll in l[1].split() if len(ll) in (2,3,4,7)]) for l in lines))
print(sum(decode([set(s) for s in l[0].split()], [set(s) for s in l[1].split()]) for l in lines))
