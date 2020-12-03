#!/usr/bin/env python3


def get_input() -> list:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


lines = get_input()
line_size = len(lines[0])


def is_tree(at: tuple[int]) -> bool:
    return lines[at[1]][at[0] % line_size] == '#'


result = 1
for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    count = 0
    i = 0
    while True:
        try:
            i += 1
            count += is_tree((i * right, i * down))
        except:
            break

    result *= count

print(result)
