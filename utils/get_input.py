#!/usr/bin/env python3


def get_input() -> list:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]
