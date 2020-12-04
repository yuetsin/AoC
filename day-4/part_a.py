#!/usr/bin/env python3

def get_input() -> list:
    with open('./input', 'r') as f:
        return [v.strip() for v in f.readlines()]


lines = get_input()

items = [dict()]

for line in lines:
    if line == '':
        items.append(dict())
    else:
        for tok in line.split(' '):
            k, v = tok.split(':')
            items[-1].update({k: v})


valid_count = 0

for it in items:
    valid = True
    for required_value in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if not required_value in it:
            valid = False
            break

    if valid:
        valid_count += 1

print(valid_count)
