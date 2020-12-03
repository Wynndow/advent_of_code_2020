#!/usr/bin/env python3

with open('input.txt') as f:
    data = [int(x.strip()) for x in f.readlines()]
    data.sort()

top_index = 0
tail_index = -1

found = False
while not found:
    sum = data[top_index] + data[tail_index]
    if sum == 2020:
        found = True
    elif sum > 2020:
        tail_index -= 1
    else:
        top_index += 1

print(data[top_index] * data[tail_index])
