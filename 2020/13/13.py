from functools import reduce


# read input file
# 1-st line contains timestamp
# 2-nd line contains bus ids; replace 'x' with an infinity representation
with open('input.txt') as f:
    ts = int(f.readline())
    lines = [float(x) for x in f.readline().replace('x','inf').split(',')]


# part 1
'''
minim = float('inf')
for bus in lines:
    t = ((ts + bus - 1) // bus)*bus - ts
    if t < minim:
        minim = t
        print(bus, t, bus*t)
print()
'''
print(int(reduce(lambda x,y: x*y, min([(((ts+bus-1)//bus)*bus-ts, bus) for bus in lines]))))


# part 2
# chinese_rem() and mul_inv()
# implementation of Chinese Remainder Theorem from
# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
# under GNU Free Documentation License 1.2
# https://www.gnu.org/licenses/fdl-1.2.html


def chinese_rem(n, a):    
    summ = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in zip(n, a):
        p = prod // n_i
        summ += a_i * mul_inv(p, n_i) * p
    return summ % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

 
n_a = list(zip(*[(int(bus), -i) for i, bus in enumerate(lines) if bus != float('inf')]))
print(chinese_rem(*n_a))
