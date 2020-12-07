cnt = 0
part1 = 0
part2 = 0
for line in open('input.txt'):
    cnt += 1
    k,v = line.strip().split(': ')
    interval,char = k.split(' ')
    minim, maxim = interval.split('-')    
    minim = int(minim)
    maxim = int(maxim)

    # part1
    if v.count(char) in range(minim, maxim+1):
        part1 += 1
        
    # part2
    valid = 0
    if (minim-1 < len(v)) and v[minim-1] == char: valid += 1
    if (maxim-1 < len(v)) and v[maxim-1] == char: valid += 1
    if valid == 1: part2 += 1
    
print(part1)
print(part2)
    
