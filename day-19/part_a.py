#!/usr/bin/env python3
import json
import itertools

def get_input(f: str='./input') -> list[str]:
    with open(f, 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


dictionaries = {}
rules = get_input('./rules')
rule_count = len(rules)

while len(dictionaries) < rule_count:
    # print('len(d) =', len(dictionaries), 'rule_count =', rule_count)
    for line in rules:
        ident, body = line.split(': ')
        if body.startswith('"'):
            dictionaries.update({ident: set([eval(body)])})
        else:
            bodies = body.split(' | ')
            possible_body_strs = set()

            ok = True
            for bdy in bodies:
                try:
                    # print([dictionaries[v] for v in bdy.split(' ')])
                    for p in itertools.product(*[dictionaries[v] for v in bdy.split(' ')]):
                        possible_body_strs.add(''.join(p))
                except KeyError:
                    # print(e)
                    ok = False
                    break
            if ok:
                dictionaries.update({ident: possible_body_strs})

# print(dictionaries['0'])
# print(len(dictionaries['0']))


msgs = set(get_input('./messages'))
print(len(dictionaries['0'].intersection(msgs)))