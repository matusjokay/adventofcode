'''
read program as sequence of triples: [cmd, num, flag]
cmd - instruction to be executed
num - instruction argument (an integer)
flag - set to True for each executed instruction

flag is tested before instruction executing
if it is set to True before executing, that means
that there is a cycle (the instruction was executed
in the past)
'''
program = []
for line in open('input.txt'):
    program += [line.split()[:2]+[False]]
    program[-1][1] = int(program[-1][1])

def run(p):
    '''
    Execute a program `p`.
    
    Cycle detection is based on the flag value of
    each instruction to be executed: if its value
    is True, the instruction was executed in the
    past and there is a cycle.

    Returns two values:
    ret[0] is value of accumulator at the end of the
        program execution
    ret[1] is True, if there was no cycle detected
        during the program execution, False otherwise
    '''
    # clear flag for cycle detection
    p = [[v[0],v[1],False] for v in p]

    # accumulator and instruction pointer        
    acc = 0
    ip = 0
    while True:
        # break at the end of the program
        if ip == len(p):
            break
        # break on cycle
        if p[ip][2] == True:
            break
        # set executed flag on instruction
        p[ip][2] = True

        # execute instruction
        if p[ip][0] == 'nop':
            ip += 1
        elif p[ip][0] == 'acc':
            acc += p[ip][1]
            ip += 1
        elif p[ip][0] == 'jmp':
            ip += p[ip][1]
            
    # return acc val and True, if program
    # terminated normally (no loop detected)
    return acc, ip == len(p)

def fixProgram(p):
    '''
    A program `p` is correct, if it terminates
    without a cycle detected. This function tries
    to fix a corrupted program changing exactly
    one jmp instruction to nop or nop to jmp.
    '''
    ret = None
    for i,val in enumerate(program):
        cmd = program[i][0]
        if cmd == 'nop':
            program[i][0] = 'jmp'
        elif cmd == 'jmp':
            program[i][0] = 'nop'
        else:
            continue
        ret = run(program)
        if ret[1] == True:
            break            
        program[i][0] = cmd
        
    # if in the program are no jmp and nop
    # instruction, run the program to obtain
    # result in accumulator
    if ret is None:
        ret = run(program)
    return(ret)

print(run(program)[0])
print(fixProgram(program)[0])
