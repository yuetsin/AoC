#!/usr/bin/env python3

import re


def get_input() -> list:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


lines = get_input()
count = 0

for line in lines:
    lower, upper, char, password = re.split(r'-|: | ', line)
    lower, upper = int(lower) - 1, int(upper) - 1
    try:
        if (password[lower] == char) ^ (password[upper] == char):
            count += 1
    except:
        # don't care about boundaries
        pass

print(count)
