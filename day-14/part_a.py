#!/usr/bin/env python3


def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


move_scripts = get_input()


def _set_mask(value: list, mask: list) -> list:
    assert(len(value) == len(mask))
    return [value[i] if mask[i] == 'X' else mask[i] for i in range(len(mask))]


mask = ['0'] * 36

memory = dict()

for line in move_scripts:
    if line.startswith('mask = '):
        mask = list(line[7:])
        print("update mask to %s" % ''.join(mask))
    elif line.startswith('mem['):
        addr, value = line[4:].split('] = ')
        addr = int(addr)
        value = bin(int(value))[2:].rjust(36, '0')
        real_value = int(''.join(_set_mask(value, mask)), base=2)
        print("set addr %d to %d" % (addr, real_value))
        memory.update({addr: real_value})

print(sum([v for _, v in memory.items()]))
