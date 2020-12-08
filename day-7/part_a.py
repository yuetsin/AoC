#!/usr/bin/env python3
from functools import lru_cache


def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


lines = get_input()

bag_dict = {}


@lru_cache(maxsize=None)
def can_get_shiny_gold(name: str) -> bool:
    if name == 'shiny gold':
        return True
    for item in bag_dict[name]:
        if can_get_shiny_gold(item[1]):
            return True
    return False


def get_bag_name(raw_name: str) -> str:
    raw_name = raw_name.strip()
    if raw_name.endswith('bags'):
        return raw_name[:-4].strip()
    elif raw_name.endswith('bag'):
        return raw_name[:-3].strip()


for line in lines:
    line = line[:-1]
    container, containees = line.split(' contain ')

    conts = []
    for containee in containees.split(', '):
        num, bag_name = containee.split(' ', maxsplit=1)
        if num == 'no':
            break
        conts.append((int(num), get_bag_name(bag_name)))

    bag_dict.update({get_bag_name(container): conts})


result = sum([1 if can_get_shiny_gold(k) else 0 for k, _ in bag_dict.items()])

# idiot question
if 'shiny gold' in bag_dict:
    result -= 1

print(result)
