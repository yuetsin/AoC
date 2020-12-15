#!/usr/bin/env python3

from copy import deepcopy


def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


move_scripts = get_input()


def _set_mask(value: list, mask: list) -> list:
    assert(len(value) == len(mask))
    return [value[i] if mask[i] == 'X' else mask[i] for i in range(len(mask))]


def _set_mask_v2(value: list, mask: list) -> list:
    assert(len(value) == len(mask))

    possible_addrs = [[]]

    for i in range(len(mask)):
        if mask[i] == '0':
            for sub in possible_addrs:
                sub.append(value[i])
        elif mask[i] == '1':
            for sub in possible_addrs:
                sub.append('1')
        else:
            new_possible_addrs = deepcopy(possible_addrs)

            for sub in possible_addrs:
                sub.append('0')

            for sub in new_possible_addrs:
                sub.append('1')

            for sub in new_possible_addrs:
                possible_addrs.append(sub)

    return possible_addrs


mask = ['0'] * 36

memory = dict()

for line in move_scripts:
    if line.startswith('mask = '):
        mask = list(line[7:])
        print("update mask to %s" % ''.join(mask))
    elif line.startswith('mem['):
        addr, value = line[4:].split('] = ')
        addr = bin(int(addr))[2:].rjust(36, '0')
        value = int(value)

        for addr_list in _set_mask_v2(addr, mask):
            real_addr = int(''.join(addr_list), base=2)
            print("set addr %d to %d" % (real_addr, value))
            memory.update({real_addr: value})

print(sum([v for _, v in memory.items()]))
