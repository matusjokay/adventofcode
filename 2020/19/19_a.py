#!/bin/env python3


def read_input(fname):
    state = 'rules'
    data = []
    rules = dict()

    for line in open(fname):
        line = line.strip()
        if not line:
            state = 'data'

        if state == 'rules':
            ruleno, rule = line.split(': ')
            rule = [r.strip().split() for r in rule.split('|')]
            rule = [[int(r) if r.isdigit() else r[1:-1] for r in rules] for rules in rule]
            rules[int(ruleno)] = rule
        elif state == 'data':
            data.append(line)

    rules = evaluate_rules(rules)
    return rules, data


def evaluate_rules(rules):
    change = True

    new_rules = dict()
    while change:
        change = False
        for key, rule in rules.items():
            new_rule = []
            for ind, ru in enumerate(rule):
                new_subrule = []
                for i, r in enumerate(ru):
                    if type(r) != int:
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

    for key, rule in rules.items():
        for ind, ru in enumerate(rule):
            rule[ind] = ''.join(ru)

    return rules


rules, data = read_input('input_b.txt')
#print(rules, data)
print(sum([1 if word in rules[0] else 0 for word in data]))
