#!/usr/bin/env python3

with open('input.txt') as f:
    data = [int(x.strip()) for x in f.readlines()]
    data.sort()

top_index = 0
tail_index = len(data) - 1
mid_index = 1
counts = 1
found = False
while not found:
    print(f"Count: {counts}")
    counts += 1
    sum = data[top_index] + data[mid_index] + data[tail_index]
    if sum == 2020:
        found = True
    elif sum > 2020:
        tail_index -= 1
        if tail_index == mid_index:
           tail_index = len(data) - 1
           top_index = 0
           mid_index +=1
    else:
        top_index += 1
        if top_index == mid_index:
            tail_index = len(data) - 1
            top_index = 0
            mid_index += 1

print(data[top_index] * data[mid_index] * data[tail_index])
                
