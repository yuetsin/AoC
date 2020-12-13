#!/usr/bin/env python3

from math import pi


def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


move_scripts = get_input()

wpx, wpy = 10, 1

posx, posy = 0, 0

for move in move_scripts:
    icode, ival = move[0], int(move[1:])

    if icode == 'N':
        wpy += ival
    elif icode == 'S':
        wpy -= ival
    elif icode == 'E':
        wpx += ival
    elif icode == 'W':
        wpx -= ival
    elif icode == 'L':
        if ival == 90:
            wpx, wpy = -wpy, wpx
        elif ival == 180:
            wpx, wpy = -wpx, -wpy
        elif ival == 270:
            wpx, wpy = wpy, -wpx
    elif icode == 'R':
        if ival == 270:
            wpx, wpy = -wpy, wpx
        elif ival == 180:
            wpx, wpy = -wpx, -wpy
        elif ival == 90:
            wpx, wpy = wpy, -wpx
    elif icode == 'F':
        posx += wpx * ival
        posy += wpy * ival
    else:
        raise ValueError("unable to parse icode %s" % icode)


print(abs(posx) + abs(posy))
