#!/usr/bin/env python3

def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


_, bus_count_str = get_input()

bus_list = [int(v) if v != 'x' else 0 for v in bus_count_str.split(',')]

bus_dict = dict()

bus_count = len(bus_list)

for i in range(bus_count):
    if bus_list[i] != 0:
        bus_dict.update({i: bus_list[i]})

bus_items = tuple(bus_dict.items())

min_step = max(bus_list)

min_possible = 100000000000000

min_possible = (min_possible // min_step) * min_step

offset = bus_list.index(min_step)

main_mod = bus_list[0]

for real_i in range(min_possible, 1000000000000000, min_step):
    i = real_i - offset

    if i % main_mod != 0:
        continue

    # print('%20d' % i, end='\r')

    ok = True
    for bus_i, bus_v in bus_items:
        if (i + bus_i) % bus_v != 0:
            ok = False
            break

    if ok:
        print()
        print(i)
        break
