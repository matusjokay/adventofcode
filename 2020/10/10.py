from functools import reduce

# read input as list of sorted numbers
jolts = sorted([int(line.strip()) for line in open('input.txt')])
jolts.append(jolts[-1]+3)

# part 1
hist = [0,0,0]
runs = []
ones = 0
prev = 0
for i in jolts:
    # compute difference and update histogram
    diff = i-prev
    hist[diff-1] += 1
    prev = i

    # compute run of ones - for part 2
    if diff == 1:
        ones += 1
    else:
        if ones > 1:
            runs.append(ones-1)
        ones = 0
print(hist[0]*hist[2])

# returns sum of binomial coefficients C(0,n),
# C(1,n) and C(2,n), which forms a Triangular
# number T(n) plus one
# T_plus_one(n) = 1 + T(n) = 1 + n*(n+1)/2
def c0c1c2(n):
    return 2 if n == 1 else 1+n+int(n*(n-1)/2)

# part 2 - product of all T(n)+1 numbers, for
# n from run of ones
coeff = (2, 4, 7, 11, 16, 22, 29)
print(reduce(lambda x,y: x*y, map(lambda x: coeff[x-1], runs)))
