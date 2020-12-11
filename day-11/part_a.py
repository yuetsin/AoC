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

    occupied_neighbors = 0
    for x in range(posx - 1, posx + 2):
        for y in range(posy - 1, posy + 2):
            if x == posx and y == posy:
                # skip myself
                continue
            try:
                """
                avert "smart" s[-1] syntax
                """
                assert(x >= 0 and y >= 0)
                if orig_grid[y][x] == '#':
                    occupied_neighbors += 1
            except:
                # ignore out-of-bound errors
                pass

    if current_state == 'L' and occupied_neighbors == 0:
        return '#'
    elif current_state == '#' and occupied_neighbors >= 4:
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
