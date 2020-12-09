# read input as list of numbers
fname = 'input.txt'
preamble_len = {'input.txt':25, 'in.txt':5}
xmas = []
for line in open(fname):
    xmas += [int(line.strip())]

# part 1
# search for a not valid number
preamble = xmas[:preamble_len[fname]]
for n in xmas[preamble_len[fname]:]:
    # get components of n from preamble
    valid = [i for i in preamble if n-i != i and n-i in preamble]
    # if the list of components is empty, n is not valid
    if not valid:
        invalid_n = n
        break
    # update preamble window
    preamble = preamble[1:]+[n]
print(invalid_n)

# part 2
# find a contiguous set of at least two numbers
# which sum to the invalid number from part 1
cont_set = []
for n in xmas:
    # add new number to the end of sequence
    cont_set.append(n)
    s = sum(cont_set)
    # while the sum is above the limit,
    # remove numbers from the beginning of sequence
    while s > invalid_n:
        s -= cont_set[0]
        cont_set = cont_set[1:]
    # check the weakness of XMAS encryption
    if s == invalid_n:
        break
# print sum of the smallest and largest number
# in the contiguous set
cont_set = sorted(cont_set)
print(cont_set[0]+cont_set[-1])
