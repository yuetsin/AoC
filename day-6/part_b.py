#!/usr/bin/env python3

def get_input() -> list[str]:
    with open('./input', 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


def _get_input_raw() -> list[str]:
    with open('./input', 'r') as f:
        return [v.strip() for v in f.readlines()]


def get_input_by_chunks() -> list[list[str]]:
    raw_input = _get_input_raw()
    lists = [list()]

    for imp in raw_input:
        if imp:
            lists[-1].append(imp)
        else:
            lists.append(list())
    return lists


yes_questions_count = 0
for chunk in get_input_by_chunks():
    yes_questions = set('abcdefghijklmnopqrstuvwxyz')
    for line in chunk:
        yes_questions = yes_questions.intersection(set(line))
    yes_questions_count += len(yes_questions)

print(yes_questions_count)
