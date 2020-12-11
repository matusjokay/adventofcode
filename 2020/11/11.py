import copy

# read input as two dimensional array of chars
seats = [['.']+list(line.strip())+['.'] for line in open('input.txt')]
seats.insert(0, list('.'*len(seats[0])))
seats.append(list('.'*len(seats[0])))


def print_seats(s):
    ''' print seats map '''
    [print(''.join(row)) for row in s]
    print()


def _occ(s, row, col, op, only_adjacent = True):
    '''
    Search for occupied seats only in one direction,
    given by tuple `op` - by it's content are coordinates
    row and col updated. If `only_adjacent` is True,
    occupancy test doesn't follow dots '.' to first
    occurence '#' or 'L'.
    '''
    if not only_adjacent:
        while row>0 and row<len(s)-1 and col>0 and col<len(s[0])-1 and s[row][col] == '.':
            row, col = row+op[0], col+op[1]        
    return {'.':0, 'L':0, '#':1}[s[row][col]]


def occ(s, row, col, only_adjacent = True):
    '''
    Get number of occupied seats for seat at row,col
    coordinates. If `only_adjacent` is True, search only
    for neighbors. If `only_adjacent` is False, search
    in all directions until map borders.
    '''    
    coord = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
    return sum(_occ(s, row+c[0], col+c[1], c, only_adjacent) for c in coord)


def game_of_seats(seats, treshold, only_adjacent):
    change_rule={'L':'#LLLLLLLL', '#':'#'*treshold+'L'*(9-treshold)}
    change = True
    while change:
        s_orig = copy.deepcopy(seats)
        change = False
        occupied = 0
        for row in range(1,len(seats)-1):
            for col in range(1,len(seats[0])-1):
                # floor never changes
                if s_orig[row][col] == '.':
                    continue
                
                # get number of occupied seats
                occupied = occ(s_orig, row, col, only_adjacent)
                # new state of seat at (row, col)
                ch = change_rule[s_orig[row][col]][occupied]
                seats[row][col] = ch
                # update `change` flag
                change = change or s_orig[row][col] != ch                
    return sum([''.join(row).count('#') for row in seats])


# part 1
print(game_of_seats(copy.deepcopy(seats), 4, True))

# part 2
print(game_of_seats(copy.deepcopy(seats), 5, False))
