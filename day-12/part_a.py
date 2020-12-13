#!/usr/bin/env python3

from math import pi


def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


move_scripts = get_input()

posx, posy = 0, 0
deg = 0


for move in move_scripts:
    icode, ival = move[0], int(move[1:])

    if deg < 0:
        deg += 360
    elif deg >= 360:
        deg -= 360

    if icode == 'N':
        posy += ival
    elif icode == 'S':
        posy -= ival
    elif icode == 'E':
        posx += ival
    elif icode == 'W':
        posx -= ival
    elif icode == 'L':
        deg += ival
    elif icode == 'R':
        deg -= ival
    elif icode == 'F':
        if deg == 0:
            posx += ival
        elif deg == 90:
            posy += ival
        elif deg == 180:
            posx -= ival
        elif deg == 270:
            posy -= ival
        else:
            raise ValueError("unable to handle degree %d" % deg)
    else:
        raise ValueError("unable to parse icode %s" % icode)


print(abs(posx) + abs(posy))
