#!/usr/bin/env python3

def get_input() -> list:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


lines = get_input()

# lines = ['FBFBBFFRLR']
seat_ids = []
for line in lines:
    row = -1
    column = -1

    lower, upper = 0, 128
    for ch in line[:7]:
        halfway = (upper - lower) // 2
        if ch == 'F':
            upper -= halfway
        else:
            lower += halfway
    row = lower

    lower, upper = 0, 8
    for ch in line[7:]:
        halfway = (upper - lower) // 2
        if ch == 'L':
            upper -= halfway
        else:
            lower += halfway

    column = upper - 1

    # print(row, column)
    seat_ids.append(row * 8 + column)


seat_ids_set = set(seat_ids)
for i in range(min(seat_ids), max(seat_ids) + 1):
    if not i in seat_ids_set:
        print(i)
        break
