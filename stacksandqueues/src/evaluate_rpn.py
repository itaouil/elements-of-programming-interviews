
"""
    Given a Reverse-Polish-Notation
    expression evaluate its value.
"""

import operator

# Get operator function
def operator(char):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.div
    }[char]

# Evaluates RPN expression
def evaluate(exp):
    stack = Stack()

    list_exp = exp.split(',')

    for token in list_exp:
        if not operator(token):
            stack.push(token)
        else:
            res = operator(char)(stack.pop(), stack.pop())
            stack.push(res)

    return stack.pop()
