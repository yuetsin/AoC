#!/usr/bin/env python3
from functools import lru_cache


def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


available_joints = [int(v) for v in get_input()]

target_volt = max(available_joints) + 3

available_joints_set = set(available_joints)


@lru_cache(maxsize=None)
def ways_to(target: int) -> int:
    if target == 0:
        return 1

    if not target in available_joints_set:
        return 0

    poss = 0
    for diff in [1, 2, 3]:
        poss += ways_to(target - diff)

    return poss


print(ways_to(target_volt - 3))
