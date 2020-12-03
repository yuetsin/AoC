#!/usr/bin/env python3


def get_input() -> list:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


lines = get_input()
line_size = len(lines[0])


def is_tree(at: tuple[int]) -> bool:
    return lines[at[1]][at[0] % line_size] == '#'


print(sum([is_tree((i * 3, i)) for i in range(len(lines))]))
