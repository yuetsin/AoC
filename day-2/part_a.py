#!/usr/bin/env python3

import re


def get_input() -> list:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


lines = get_input()
count = 0

for line in lines:
    lower, upper, char, password = re.split(r'-|: | ', line)
    lower, upper = int(lower), int(upper)
    if lower <= password.count(char) <= upper:
        count += 1

print(count)
