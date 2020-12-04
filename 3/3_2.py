#!/usr/bin/env python3
from collections import namedtuple

with open('input.txt') as f:
    mountain = tuple(x.strip() for x in f.readlines())

Slope = namedtuple('Slope', ['right', 'down'])
slopes = (Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2))

total_trees = 1
width = len(mountain[0])

for slope in slopes:
    x, y, trees = 0, 0, 0
    while True:
        try:
            if mountain[y][x] == '#': trees += 1
            x = (x + slope.right) % width
            y += slope.down
        except IndexError:
            total_trees *= trees
            break

print(total_trees)
