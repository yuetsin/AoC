#!/usr/bin/env python3
from functools import lru_cache


def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


lines = get_input()

visited_locs_set = set()
rip = 0
acc = 0


while True:
    icode, iargs = lines[rip].split(' ')

    new_rip = rip

    if icode == 'nop':
        new_rip += 1
    elif icode == 'acc':
        acc += int(iargs)
        new_rip += 1
    elif icode == 'jmp':
        new_rip += int(iargs)

    if new_rip in visited_locs_set:
        print(acc)
        break
    else:
        rip = new_rip
        visited_locs_set.add(rip)
