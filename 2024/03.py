#!/bin/env python3

import re
from functools import reduce

# concatenate the input into one line
data = reduce(lambda x,y: x.strip()+y.strip(), open('03.input.txt').readlines(), '')

# part A
d = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', data)
print(sum([int(x)*int(y) for x, y in d]))

# part B
# each 'do()' enables a command block; each block will be a one line
data = re.sub(r'do\(\)', '\n', data).split('\n')
# remove all commands after the first "don't()" instruction and
# concatenate the commands into one line
d = ''.join([re.sub(r"don't\(\).*", '', l) for l in data])
# apply part A
d = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', d)
print(sum([int(x)*int(y) for x, y in d]))
