# read input as list of starting sequences
inp = [[int(x) for x in line.strip().split(',')] for line in open('input.txt')]


def rambunctious_recitation(seq, end):
    # first n-1 starting numbers append into dict
    # the number itself is a key, turn is a value
    spoken_nums = {n:turn+1 for turn,n in enumerate(seq[:-1])}
    # n-th starting number
    spoken = seq[-1]
    for turn in range(len(spoken_nums)+1, end):
        # if spoken number is not in a set of spoken numbers
        if spoken not in spoken_nums:
            # add a number into the set
            spoken_nums[spoken] = turn
            # the next spoken number is 0
            spoken = 0
        # else spoken number is already in spoken numbers
        else:
            most_recently_turn = spoken_nums[spoken]
            # update turn for a given number
            spoken_nums[spoken] = turn
            # the next spoken number will be 'age'
            # (the time a number was most recently spoken
            # before)
            spoken = turn - most_recently_turn
    return spoken


# part 1
print("2020th number spoken in rambunctious recitation game:")
for seq in inp:
    print(f'\t{seq} -->', rambunctious_recitation(seq, 2020))
print()

# part 2
print("30000000th number spoken in rambunctious recitation game:")
for seq in inp:
    print(f'\t{seq} -->', rambunctious_recitation(seq, 30000000))
print()
