#!/usr/bin/env python3

from itertools import permutations

def get_input(fn = './input') -> list[str]:
    with open(fn, 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


rules = []
for rule in get_input('./rules'):
    name, value = rule.split(': ')
    rule = []
    for cond in value.split(' or '):
        rule.append(([int(v) for v in cond.split('-')]))
    rule.append(name)

    rules.append(rule)

def _might_be_valid_field(num: int) -> bool:
    for cond_1, cond_2, _ in rules:
        if cond_1[0] <= num <= cond_1[1] or cond_2[0] <= num <= cond_2[1]:
            return True
    return False




valid_tickets = []
for ticket in get_input('./nearby_tickets'):
    for num in [int(i) for i in ticket.split(',')]:
        if not _might_be_valid_field(num):
            break
    valid_tickets.append([int(i) for i in ticket.split(',')])

def _is_ok_for_rule_at_index(rule: list, index: int) -> bool:
    cond_1, cond_2, _ = rule
    for ticket in valid_tickets:
        if cond_1[0] <= ticket[index] <= cond_1[1] or cond_2[0] <= ticket[index] <= cond_2[1]:
            pass
        else:
            return False
    return True

bad_combination = set()

count = 0
for perm in permutations(range(len(rules))):
    print(bad_combination)
    input()
    idx = 0
    ok = True
    for i in perm:
        if (idx, i) in bad_combination:
            ok = False
            break
        if not _is_ok_for_rule_at_index(rules[idx], i):
            ok = False
            bad_combination.add((idx, i))
            break
        idx += 1
    if ok:
        print('ok!')
        exit()
    count += 1