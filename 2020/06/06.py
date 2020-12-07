summ = 0
ans = set()
summ_yes = 0
yes = None
for line in open('input.txt'):
    line = line.strip()
    ans.update(tuple(line))

    if yes is None:
        yes = set(line)
    elif line:
        yes &= set(line)

    if not line:
        summ += len(ans)
        ans = set()
        
        summ_yes += len(yes)
        yes = None

print(summ, summ_yes)
