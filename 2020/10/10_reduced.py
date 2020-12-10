from functools import reduce

jolts = [0] + sorted([int(line.strip()) for line in open('input.txt')])
jolts.append(jolts[-1]+3)

coeff = (1, 1, 2, 4, 7)
hist = [0,0,0]
mul = 1
for i in range(1, len(jolts)):
    # part 1
    hist[jolts[i]-jolts[i-1]-1] += 1

    # part 2
    if jolts[i]-jolts[i-1] == 1:
        hist[1] += 1
    else:
        mul *= coeff[hist[1]]
        hist[1] = 0
        
print(hist[0]*hist[2])
print(mul)
