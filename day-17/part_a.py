#!/usr/bin/env python3

def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]



def get_neighbors(x: int, y: int, z: int) -> list[tuple]:
    result = []
    for rx in x - 1, x, x + 1:
        for ry in y - 1, y, y + 1:
            for rz in z - 1, z, z + 1:
                result.append((rx, ry, rz))

    result.remove((x, y, z))
    return result

def get_x_range(grids) -> tuple[int]:
    x_pos = [pos[0] for pos in grids]
    return range(min(x_pos) - 1, max(x_pos) + 2)


def get_y_range(grids) -> tuple[int]:
    y_pos = [pos[1] for pos in grids]
    return range(min(y_pos) - 1, max(y_pos) + 2)


def get_z_range(grids) -> tuple[int]:
    z_pos = [pos[2] for pos in grids]
    return range(min(z_pos) - 1, max(z_pos) + 2)

area = set()

grids = get_input()
for y in range(len(grids)):
    for x in range(len(grids[0])):
        if grids[y][x] == '#':
            area.add((x, y, 0))

cycle_count = 0

while cycle_count < 6:
    new_area = set()
    for x in get_x_range(area):
        for y in get_y_range(area):
            for z in get_z_range(area):
                light_neighbors = sum([1 if ng in area else 0 for ng in get_neighbors(x, y, z)])
                if (x, y, z) in area and light_neighbors == 2 or light_neighbors == 3:
                    new_area.add((x, y, z))
                elif not (x, y, z) in area and light_neighbors == 3:
                    new_area.add((x, y, z))   
    area = new_area
    cycle_count += 1

print(len(area))
