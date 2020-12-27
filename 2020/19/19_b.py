#!/bin/env python3


def read_input(fname):
    state = 'rules'
    data = []
    rules = dict()

    for line in open(fname):
        line = line.strip()
        if not line:
            state = 'data'
            continue

        if state == 'rules':
            ruleno, rule = line.split(': ')
            rule = [r.strip().split() for r in rule.split('|')]
            rule = [[int(r) if r.isdigit() else r[1:-1] for r in rules] for rules in rule]
            rules[int(ruleno)] = rule
        elif state == 'data':
            data.append(line)

    rules = evaluate_rules(rules)
    return rules, data


rule8 = []
rule11a = []
rule11b = []
def evaluate_rules(rules):
    global rule8
    global rule11a
    global rule11b

    change = True

    new_rules = dict()
    while change:
        change = False
        for key, rule in rules.items():
            new_rule = []
            for ind, ru in enumerate(rule):
                new_subrule = []
                for i, r in enumerate(ru):
                    if r == 8 or r == 11 or type(r) != int:
                        new_subrule.append(r)
                    else:
                        change = True
                        new_subrule = [new_subrule[:]+list(rr)+ru[i+1:] for rr in rules[r]]
                        new_rule += new_subrule
                        break
                else:
                    new_rule += [new_subrule]
            new_rules[key] = new_rule
        rules = new_rules

    res = dict()
    for key, rule in rules.items():
        remove_rule = True
        new_rule = []
        for ind, ru in enumerate(rule):
            terminal = True
            for item in ru:
                if type(item) == int:
                    terminal = False
                    remove_rule = False
                    break
            if not terminal:
                if len(ru) > 2 and len(ru) < 10:
                    num = ''.join(ru[:-1])
                    num = num.replace('a','0')
                    num = num.replace('b','1')
                    new_rule.append(tuple([num]+[ru[-1]]))
                    rule8 += [int(num,2)]
                elif len(ru) > 10:
                    num1 = ''.join(ru[:8])
                    num1 = num1.replace('a','0')
                    num1 = num1.replace('b','1')
                    num2 = ''.join(ru[9:])
                    num2 = num2.replace('a','0')
                    num2 = num2.replace('b','1')
                    new_rule.append(tuple([num1]+[ru[8]]+[num2]))
                    rule11a += [int(num1,2)]
                    rule11b += [int(num2,2)]
                    print(ru, num1, num2)
                else:
                    new_rule.append(tuple(ru))

        if not remove_rule:
            res[key] = tuple(new_rule)
            #rule[ind] = ''.join(ru)    

    return res


rules, data = read_input('input_b.txt')

rules[8] = sorted(rules[8])
rules[11] = sorted(rules[11])

rule8 = set(rule8)
rule11a = set(rule11a)
rule11b = set(rule11b)

print(rule8)
print(rule11a)
print(rule11b)

summ = 0
for line in data:
    if len(line) % 8:
        continue

    nums = []
    for i in range(0,len(line),8):
        num = line[i:i+8]
        num = num.replace('a','0')
        num = num.replace('b','1')
        nums += [int(num,2)]

    if nums[0] not in rule8:
        #print(f'{line} {nums} not in rule8 no1')
        continue
    if nums[1] not in rule8:
        #print(f'{line} {nums} not in rule8 no2')
        continue
    
    i = 2
    while i < len(nums) and nums[i] in rule8:
        i += 1
    if i == len(nums):
        #print(f'{line} {nums} not in rule8 or rule11a')
        continue

    tmp_i = i
    while i < len(nums) and nums[i] in rule11b:
        i += 1
    if i != len(nums):
        #print(f'{line} {nums} not in rule11b, {nums[i:]}')
        continue

    if tmp_i-1 < i-tmp_i:
        continue
    #print(line, nums)
    summ += 1
print(summ)



#print(rules, data)
#print(sum([1 if word in rules[0] else 0 for word in data]))
