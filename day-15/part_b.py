#!/usr/bin/env python3

start_nums = 1, 20, 8, 12, 0, 14

memo: dict[int: list[int]] = dict()

for i in range(len(start_nums)):
    v = start_nums[i]
    if not v in memo:
        memo.update({v: [i]})
    else:
        memo[v].append(i)

last_number = start_nums[-1]

time = len(start_nums)
while True:
    # print(memo)

    if len(memo[last_number]) == 1:
        this_number = 0
    else:
        this_number = memo[last_number][-1] - memo[last_number][-2]

    if this_number in memo:
        memo[this_number].append(time)
    else:
        memo.update({this_number: [time]})

    # print('say', this_number)
    # input()
    # just took half a minute...
    # let it run
    if time == 30000000:
        print(last_number)
        break

    last_number = this_number
    time += 1
