#!/bin/env python3


from collections import defaultdict
from itertools import accumulate


# part A

d = [int(c) for c in open('09.input.txt').readlines()[0].strip()]+[0]

ind = len(d)-2
s = 0
for i, secid in enumerate([0]+list(accumulate(d))):
    if not i % 2:
        s += sum([j*i//2 for j in range(secid, secid + d[i])])
        continue
    while d[i] and ind > i:
        dif = min(d[i], d[ind])
        d[ind] -= dif
        d[i] -= dif
        s += sum([j*ind//2 for j in range(secid, secid + dif)])
        # update free blocks where were written file blocks
        secid += dif
        # add free blocks to the next free
        d[ind+1] += dif
        # if file is exhausted, move next free to prev free
        if not d[ind]:
            d[ind-1] += d[ind+1]
            d[ind+1] = 0
            # move index to next file to be processed
            ind -= 2
    if ind < i:
        break
print(s)


# part B

d = [int(c) for c in open('09.input.txt').readlines()[0].strip()]+[0]
accd = [0]+list(accumulate(d))

# free lists in dict, the key is length of the free area
free = defaultdict(lambda: [])
for i in range(len(d)//2):
    free[d[i*2+1]].append(sum(d[:i*2+1]))
# remove zero-length area
del free[0]

moved = []      # list of moved files
find = len(d)-2 # index of the first file to be moved
while find > 0:
    flen = d[find]
    # find candidates for free area:
    # a) area should be long enaugh to hold the whole file
    # b) area should not be *after* the file itself on the disk
    cand_free = ([(list(filter(lambda x: x < accd[find], v)), k) for k,v in free.items() if k >= flen])
    if not cand_free:
        find -= 2
        continue
    cand_free = list(filter(lambda x: x[0], cand_free))
    if not cand_free:
        find -= 2
        continue
    # mark the file as moved in the input
    d[find] = 0
    # from all free space candidates select the most left one
    cand_free = min(cand_free, key=lambda x: min(x[0]))
    cand_free = (cand_free[0][0], cand_free[1])
    # move the file
    moved.append([find//2, cand_free[0], flen]) # fid, secid, len
    # remove free area from the list
    free[cand_free[1]].pop(0)
    if not free[cand_free[1]]:
        del free[cand_free[1]]
    # if some space left in the free area, insert the rest in the corresponding
    # list
    if cand_free[1] - flen:
        free[cand_free[1]-flen].insert(0, cand_free[0]+flen)
        # sort the updated free area list
        free[cand_free[1]-flen].sort()

    # move to the next file
    find -= 2

# compute checksum
s = 0
for fid, secid in enumerate([v for i,v in enumerate(zip(accd, d)) if not i%2]):
    s += sum([j*fid for j in range(secid[0], secid[0] + secid[1])])
for fid, secid, l in moved:
    s += sum([j*fid for j in range(secid, secid + l)])
print(s)
