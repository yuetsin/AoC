#!/usr/bin/env python3

# 亏你想得出…

def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]

def padding(exp: str) -> list:
    padding = exp.replace('(', ' ( ').replace(')', ' ) ').replace('+', ' + ').replace('*', ' * ')
    return [int(v) if v.isnumeric() else v.strip() for v in padding.split(' ') if v.strip()]

def evaluate(tokens: list) -> int:
    

    lvalue = 0
    opcode = '+'

    i = 0
    while i < len(tokens):
        token = tokens[i]
        # print(token)
        rvalue = None
        if token == '(':
            index = i
            paren_depth = 0
            paren_starts_at = i
            while True:
                if tokens[index] == '(':
                    paren_depth += 1
                elif tokens[index] == ')':
                    paren_depth -= 1
                    if paren_depth == 0:
                        break
                index += 1
                    
            rvalue = evaluate(tokens[paren_starts_at + 1 : index])
            i = index + 1

        elif type(token) == int:
            rvalue = token
            i += 1
        else:
            opcode = token
            i += 1
        
        if rvalue != None and opcode != None:
            if opcode == '+':
                lvalue = lvalue + rvalue
            elif opcode == '*':
                lvalue = lvalue * rvalue
            else:
                assert(False)
            rvalue = None
            opcode = None
        
    # print(''.join([str(v) for v in tokens]), '=', lvalue)
    return lvalue

print(sum([evaluate(padding(line)) for line in get_input()]))