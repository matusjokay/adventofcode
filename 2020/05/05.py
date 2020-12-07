minim = None
maxim = None
summ = 0
cnt = 0
for line in open('input.txt'):
    line = line.strip()
    line = line.replace('R','1')
    line = line.replace('L','0')
    line = line.replace('B','1')
    line = line.replace('F','0')
    row = int(line[:-3],2)
    col = int(line[-3:],2)
    i = row * 8 + col
    if not minim or i < minim:
        minim = i
    if not maxim or i > maxim:
        maxim = i
    summ += i
    cnt += 1
print(maxim)

# sum(a,b) = n*(a+b)/2
print(int((cnt+1)*(minim+maxim)/2)-summ)
