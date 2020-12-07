'''
Transform input text to a dictionary.

input text:
===========
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

dictionary:
===========
'light red': [['bright white', 1], ['muted yellow', 2]]
'dark orange': [['bright white', 3], ['muted yellow', 4]]
'bright white': [['shiny gold', 1]]
'muted yellow': [['shiny gold', 2], ['faded blue', 9]]
'shiny gold': [['dark olive', 1], ['vibrant plum', 2]]
'dark olive': [['faded blue', 3], ['dotted black', 4]]
'vibrant plum': [['faded blue', 5], ['dotted black', 6]]
'faded blue': None
'dotted black': None
'''
bags = dict()
for line in open('input.txt'):
    line = line.strip()
    line = line[:-1]
    key, val = line.split(' bags contain ')
    if val == 'no other bags':
        val = ''
    val = val.split(',')
    for ind,v in enumerate(val):
        t = v.strip().split(' ')
        if t[0] == '':
            t = None
        if t:
            val[ind] = [' '.join(t[1:3]), int(t[0])]
        else:
            val = None
    bags[key] = val
#for k,v in bags.items():
#    print(f"'{k}': {v}")

def searchBag(bags, bag, col=None):
    '''
    Recursive search bags.
    Return list of two elements:
        res[0]:
            True, if `bag` contains a bag with color `col`
            False, otherwise
        res[1]:
            number of inner bags in the `bag`
    '''
    # bag is empty
    if bags[bag] is None:
        return [False, 1]

    # search inner bags
    res = [False, 0]
    for b in bags[bag]:
        # if bag contains a bag with color 'col'
        if b[0] == col:
            res = [True, res[1]]
        # recursive search in inner bag 'b'
        r = searchBag(bags, b[0], col)

        # get number of bags in the inner bag 'b'
        res[1] += r[1] * b[1]
        # get number of the inner bag itself, but
        # only if it contains another bag(s)
        # (it's not an empty bag)
        if r[1] > 1:
            res[1] += b[1]

        # if search for a bag with a given color 'col',
        # update result only if it's still False,
        # to avoid rewriting True to False
        if not res[0]:
            res[0] = r[0]
    return res

# part 1 - get number of bags containing bag with
# a color 'shiny gold'
def searchBagSG(key):
    return searchBag(bags, key, 'shiny gold')[0]
# apply search to all bags except the 'shiny gold' bag itself
b = map(searchBagSG, {key:val for (key, val) in bags.items() if key != 'shiny gold'})
print(list(b).count(True))

# part 2 - get number of all bags in the bag 'shiny gold'
print(searchBag(bags, 'shiny gold')[1])
