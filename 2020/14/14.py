# read memory program
program = [line.strip().split(' = ') for line in open('input.txt')]


def setMask(m, part):
    '''
    Based on input mask (i.e. 'X1001X') create two output
    masks for operations: and, or. Also create an auxiliary
    array of powers in input mask where symbol 'X' is placed.
    '''
    m_and, m_or = 0, 0
    power = 0
    x = []
    for bit in m[-1::-1]:
        # bits_part: first value in this array is used for symbol
        # 'X' in the input mask, next two values are used for
        # symbol '0' and the last two values for symbol '1'
        bits_part1 = [1]+[1 & int(bit) for i in range(4) if bit != 'X']
        bits_part2 = [0]+[1,0,0,1]
        bit_value = bits_part1 if part == 'part1' else bits_part2
        
        if bit == '0' or bit == '1':
            m_and |= bit_value[int(bit)*2+1] << power
            m_or |= bit_value[int(bit)*2+2] << power
        else:
            m_and |= bit_value[0] << power
            x.append(power)
        power += 1
    return m_and, m_or, x


def ind2addr(ind, x, i):
    '''
    Apply floating bits to value `ind`. Variable `x`
    contains list of powers of `ind` where will be
    bits of `i` set.
    '''
    for k in range(len(x)):    
        ind |= 1 << x[k] if i & (1 << k) else 0
    return ind


def execute_program(program, part = 'part1'):
    '''
    Execute a `program` consisting from two types of
    commands:
        mask = 000000000000000000000000000000X1001X
        mem[42] = 100
    The first sets mask, the second sets a value on a
    given address.
    '''
    mem = dict()
    for line in program:
        # if the command sets a mask
        if line[0] == 'mask':
            mask_and, mask_or, x = setMask(line[1], part)
            continue

        # else the command sets a value on memory location
        ind = int(line[0][4:-1])
        val = int(line[1])

        if part == 'part1':
            mem[ind] = (val & mask_and) | mask_or
        else:
            ind = (ind & mask_and) | mask_or
            for i in range(1 << len(x)):
                addr = ind2addr(ind, x, i)
                mem[addr] = val
    return sum(mem.values())


print(execute_program(program, 'part1'))
print(execute_program(program, 'part2'))
