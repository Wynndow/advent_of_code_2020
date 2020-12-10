#!/usr/bin/env python3
from collections import deque
with open('input.txt') as f:
    numbers = [int(l.strip()) for l in f.readlines()]

buff = deque(n for n in numbers[0:25])
found_target = False
for i in range(25, len(numbers)):
    front_index = 0
    back_index = 24
    found = False
    sorted_buff = sorted(buff)
    while not found:
        if front_index == back_index:
            found_target = numbers[i]
            break
        tot = sorted_buff[front_index] + sorted_buff[back_index]
        if tot == numbers[i]:
            buff.popleft()
            buff.append(numbers[i])
            found = True
        elif tot > numbers[i]:
            back_index -= 1
        else:
            front_index += 1
    if found_target: break


for start_index in range(0, len(numbers)):
    result = False
    stop_index = start_index + 1
    tot = numbers[start_index] + numbers[stop_index]
    found = False
    while not found:
        if tot == found_target:
            result = min(numbers[start_index:stop_index+1]) + max(numbers[start_index:stop_index+1])
            break
        elif tot > found_target:
            break
        else:
            stop_index += 1
            tot += numbers[stop_index]
    if result: break

print(result)
