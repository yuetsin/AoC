#!/usr/bin/env python3

from math import pi


def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


start_time_str, bus_count_str = get_input()

start_time = int(start_time_str)
bus_list = [int(v) for v in bus_count_str.split(',') if v != 'x']

time = start_time
while True:
    for bus in bus_list:
        if time % bus == 0:
            print((time - start_time) * bus)
            exit(0)

    time += 1
