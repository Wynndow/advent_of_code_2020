#!/usr/bin/env python3
from collections import deque
with open('input.txt') as f:
    numbers = [l.strip() for l in f.readlines()]

buff = deque(int(n) for n in numbers[0:25])
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
        if tot == int(numbers[i]):
            buff.popleft()
            buff.append(int(numbers[i]))
            found = True
        elif tot > int(numbers[i]):
            back_index -= 1
        else:
            front_index += 1
    if found_target: break

print(found_target)
