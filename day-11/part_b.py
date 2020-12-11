#!/usr/bin/env python3
from functools import lru_cache


def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


grid = [list(v) for v in get_input()]


def modify_state(posx: int, posy: int, orig_grid: list[list[str]]) -> str:
    current_state = orig_grid[posy][posx]
    if current_state == '.':
        return current_state

    visible_neighbors = 0

    for modifier in [lambda tup: (tup[0] - 1, tup[1]),
                     lambda tup: (tup[0] + 1, tup[1]),
                     lambda tup: (tup[0], tup[1] - 1),
                     lambda tup: (tup[0], tup[1] + 1),
                     lambda tup: (tup[0] + 1, tup[1] + 1),
                     lambda tup: (tup[0] - 1, tup[1] + 1),
                     lambda tup: (tup[0] + 1, tup[1] - 1),
                     lambda tup: (tup[0] - 1, tup[1] - 1)]:
        x, y = posx, posy
        while True:
            x, y = modifier((x, y))
            try:
                assert(x >= 0 and y >= 0)
                state = orig_grid[y][x]
            except:
                break
            if state == '#':
                visible_neighbors += 1
                break
            elif state == 'L':
                break

    if current_state == 'L' and visible_neighbors == 0:
        return '#'
    elif current_state == '#' and visible_neighbors >= 5:
        return 'L'
    else:
        return current_state


while True:
    new_grid = list()
    for y in range(len(grid)):
        new_grid.append(list())
        for x in range(len(grid[y])):
            new_grid[-1].append(modify_state(x, y, grid))

    if new_grid == grid:
        break
    else:
        grid = new_grid
    # print(grid)
print(sum([v.count('#') for v in grid]))
