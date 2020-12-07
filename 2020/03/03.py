
def slope(coord):
    row, col = coord
    act_col = 0
    res = 0
    wait_row = row
    for line in open('input.txt'):     
        if wait_row > 0:
            wait_row -= 1
            continue

        wait_row = row - 1
        line = line.strip()
        act_col = (act_col + col) % len(line)    
        c = line[act_col]
        if c == '#':
            res += 1
        #print(c)
            
    return res

# part 1
print(slope((1,3),))

# part 2
print(reduce(lambda x,y: x*y, map(slope, [(1,1), (1,3), (1,5), (1,7), (2,1)])))
