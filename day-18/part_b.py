#!/usr/bin/env python3

# 亏你想得出…

class MadNumber:
    value: int

    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        return MadNumber(self.value * other.value)

    def __mul__(self, other):
        return MadNumber(self.value + other.value)

def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]

def padding(exp: str) -> list:
    padding = exp.replace('(', ' ( ').replace(')', ' ) ').replace('+', ' + ').replace('*', ' * ')
    return [int(v) if v.isnumeric() else v.strip() for v in padding.split(' ') if v.strip()]

def evaluate(tokens: list) -> int:
    new_tokens = []
    for token in tokens:
        if token == '+':
            new_tokens.append('*')
        elif token == '*':
            new_tokens.append('+')
        elif type(token) == int:
            new_tokens.append('MadNumber(%d)' % token)
        else:
            new_tokens.append(token)

    result = eval(''.join(new_tokens))
    if type(result) == int:
        return result
    else:
        return result.value



print(sum([evaluate(padding(line)) for line in get_input()]))