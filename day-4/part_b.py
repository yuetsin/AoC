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
    try:
        for required_value in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if not required_value in it:
                raise LookupError()

        byr_num, iyr_num, eyr_num = int(
            it['byr']), int(it['iyr']), int(it['eyr'])

        assert(1920 <= byr_num <= 2002)
        assert(2010 <= iyr_num <= 2020)
        assert(2020 <= eyr_num <= 2030)

        hgt_num = int(it['hgt'][:-2])
        if it['hgt'].endswith('cm'):
            assert(150 <= hgt_num <= 193)
        elif it['hgt'].endswith('in'):
            assert(59 <= hgt_num <= 76)
        else:
            raise TypeError()

        assert(it['hcl'][0] == '#')
        int(it['hcl'][1:], base=16)
        assert(it['ecl'] in ['amb', 'blu', 'brn',
                             'gry', 'grn', 'hzl', 'oth'])

        assert(len(it['pid']) == 9)
        assert(it['pid'].isdigit())
    except:
        continue
    valid_count += 1

print(valid_count)
