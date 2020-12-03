#!/usr/bin/env python3

with open('input.txt') as f:
    mountain = [x.strip() for x in f.readlines()]

width = len(mountain[0])
x, y, trees = 0, 0, 0

while True:
    try:
        if mountain[y][x] == '#': trees += 1
        x = (x + 3) % width
        y += 1
    except IndexError:
        print(trees)
        break
