#!/usr/bin/env python3
from functools import lru_cache


def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


lines = get_input()


for i in range(len(lines)):

    visited_locs_set = set()
    rip = 0
    acc = 0

    if lines[i].startswith('acc'):
        # acc instruction corruption won't affect the exec flow
        continue
    elif lines[i].startswith('nop'):
        lines[i] = 'jmp' + lines[i][3:]
    elif lines[i].startswith('jmp'):
        lines[i] = 'nop' + lines[i][3:]

    while True:
        try:
            icode, iargs = lines[rip].split(' ')
        except:
            print("EXEC_OVER")
            print("acc =", acc)
            break
        new_rip = rip

        if icode == 'nop':
            new_rip += 1
        elif icode == 'acc':
            acc += int(iargs)
            new_rip += 1
        elif icode == 'jmp':
            new_rip += int(iargs)

        if new_rip in visited_locs_set:
            # print("DEAD_LOOP")
            break
        else:
            rip = new_rip
            visited_locs_set.add(rip)

    # recover the modified instructions
    if lines[i].startswith('nop'):
        lines[i] = 'jmp' + lines[i][3:]
    elif lines[i].startswith('jmp'):
        lines[i] = 'nop' + lines[i][3:]
