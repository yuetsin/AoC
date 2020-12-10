#!/usr/bin/env python3
from functools import lru_cache


def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


nums = sorted([int(v) for v in get_input()])

diff = ([nums[i] - nums[i - 1] for i in range(1, len(nums))])

print((diff.count(1) + 1) * (diff.count(3) + 1))
