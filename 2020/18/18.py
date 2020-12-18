#!/bin/env python3
'''
Implementation infix_to_postfix() and evaluate() based on

1) Shuntig-yard algorithm (invented by E. Dijkstra)
   source: en.wikipedia.org/wiki/Shunting-yard-algorithm

2) Harry Hutchins: Using a Stack to Evaluate an Expression
   source: faculty.cs.niu.edu/~hutchins/csci241/eval.htm
'''


def infix_to_postfix(expr, precedence = None):
    '''
    Transform an infix expression to postfix representation.
    '''

    if not precedence:
        precedence = {'*': 1, '+': 1}

    left_associative = {'*', '+'}
    stack = []
    res = []

    for token in expr:
        if type(token) is int:
            res.append(token)
        elif token == '(':
            stack.insert(0, token)
        elif token == ')':
            while stack and stack[0] != '(':
                res.append(stack.pop(0))
            stack.pop(0)
        else:
            if not stack or stack[0] == '(':
                stack.insert(0, token)
            else:
                while (stack and stack[0] != '('
                    and (precedence[token] < precedence[stack[0]]
                        or (precedence[token] == precedence[stack[0]]
                            and token in left_associative))):
                    res.append(stack.pop(0))
                stack.insert(0, token)

    while stack:
        res.append(stack.pop(0))

    return res


def evaluate(expr):
    stack = []
    for token in expr:
        if type(token) is int:
            stack.insert(0, token)
            continue

        op1, op2 = stack.pop(0), stack.pop(0)
        if token == '+':
            stack.insert(0, op1 + op2)
        elif token == '*':
            stack.insert(0, op1 * op2)

    return stack[0]


def tokenize(line):
    return [(int(c)) if c.isdigit() else (c) for c in line if c != ' ']


exprs = [line.strip() for line in open('input.txt')]


# part 1
precedence = {'*': 1, '+': 1}
print(sum([evaluate(infix_to_postfix(tokenize(e), precedence)) for e in exprs]))


# part 2
precedence = {'*': 1, '+': 2}
print(sum([evaluate(infix_to_postfix(tokenize(e), precedence)) for e in exprs]))
