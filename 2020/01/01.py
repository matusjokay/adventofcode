nums = [int(line) for line in open('input.txt')]
print(next(i*j for i in nums for j in nums if i+j == 2020))
print(next(i*j*k for i in nums for j in nums for k in nums if i+j+k == 2020))
