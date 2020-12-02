#!/usr/bin/env python3


def get_input() -> list:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


nums = [int(v) for v in get_input()]
TARGET = 2020

# O(n^3) isn't so bad compared to 200 input size
nums_len = len(nums)
for i in range(nums_len):
    for j in range(nums_len):
        if i == j:
            continue
        for k in range(nums_len):
            if i == k or j == k:
                continue
            if nums[i] + nums[j] + nums[k] == TARGET:
                print(nums[i] * nums[j] * nums[k])
