#!/usr/bin/env python3
from functools import lru_cache


def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


nums = [int(v) for v in get_input()]


def is_sumable(target: int, nums: list) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False


xmas_num = -1
for i in range(25, len(nums)):
    if not is_sumable(nums[i], nums[i - 25:i]):
        xmas_num = nums[i]
        break


for i in range(len(nums) - 1):
    summy = 0
    cnt = i
    while summy < xmas_num:
        summy += nums[cnt]
        cnt += 1

    if summy == xmas_num:
        if cnt - i > 1:
            print(max(nums[i: cnt]) + min(nums[i: cnt]))
