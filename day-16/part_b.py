#!/usr/bin/env python3

from functools import lru_cache

def get_input(fn = './input') -> list[str]:
    with open(fn, 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


rules = []
for rule in get_input('./rules'):
    name, value = rule.split(': ')
    rule = []
    for cond in value.split(' or '):
        rule.append(tuple(([int(v) for v in cond.split('-')])))
    rule.append(name)
    rules.append(tuple(rule))

def _might_be_valid_field(num: int) -> bool:
    for cond_1, cond_2, _ in rules:
        if cond_1[0] <= num <= cond_1[1] or cond_2[0] <= num <= cond_2[1]:
            return True
    return False




valid_tickets = []
for ticket in get_input('./nearby_tickets'):
    ok = True
    for num in [int(i) for i in ticket.split(',')]:
        if not _might_be_valid_field(num):
            ok = False
            break
    if ok:
        valid_tickets.append([int(i) for i in ticket.split(',')])

@lru_cache(maxsize=None)
def _is_ok_for_rule_at_index(rule: tuple, index: int) -> bool:
    cond_1, cond_2, _ = rule
    for ticket in valid_tickets:
        if cond_1[0] <= ticket[index] <= cond_1[1] or cond_2[0] <= ticket[index] <= cond_2[1]:
            pass
        else:
            # print('not ok for', ticket[index], 'in rule',rule)
            return False
    return True

bad_combination = set()


size = len(rules)


possible_choices = {}


for i in range(size):
    possible_choices.update({i:  0})
    for j in range(size):
        if _is_ok_for_rule_at_index(rules[i], j):
            possible_choices[i] += 1
            print('o ', end='')
        else:
            print('  ', end='')
    print()

print(possible_choices)

sorted_way = [x[0] for x in sorted(possible_choices.items(), key=lambda x: x[1])]
print(sorted_way)

fillins = [-1] * size


def fill_in_blocks(idx: int) -> bool:
    if idx >= size:
        return True
    print(fillins)
    rule = tuple(rules[idx])
    for ticket_idx in range(size):
        if ticket_idx in fillins:
            continue
        if _is_ok_for_rule_at_index(rule, ticket_idx):
            fillins[idx] = ticket_idx
            if fill_in_blocks(idx + 1):
                return True
            fillins[idx] = -1
    return False

fillins[15] = 11
fillins[19] = 9
fillins[13] = 17
fillins[16] = 7
fillins[18] = 12
fillins[3] = 4
fillins[2] = 2
fillins[1] = 19
fillins[5] = 6
fillins[4] = 14
fillins[0] = 1

my_ticket = 109,101,79,127,71,59,67,61,173,157,163,103,83,97,73,167,53,107,89,131
print(my_ticket[4] * my_ticket[2] * my_ticket[19] * my_ticket[6] * my_ticket[14] * my_ticket[1])


"""
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9
  x                                     0
                                      x 1
    x                                   2
        x                               3
                            x           4
            x                           5
      o             o         o o       6
      o                                 7
      o             o           o       8
o     o   o     o   o     o   o o   o   9
o     o   o         o         o o       0
o     o   o         o         o o   o   1
      o                         o       2
                                  x     3
o     o   o     o   o         o o   o   4
                      x                 5
              x                         6
o     o             o         o o       7
                        x               8
                  x                     9
"""

# use your brain and fill several grids
# could ease your computer's workload

print(fill_in_blocks(0))

print(fillins)