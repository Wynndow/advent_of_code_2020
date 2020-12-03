#!/usr/bin/env python3
import re

with open('input.txt') as f:
    print(sum(map(lambda pw : 1 if pw[-1].count(pw[2]) in range(int(pw[0]), int(pw[1]) + 1)  else 0, [re.split(r'\W+', l.strip()) for l in f.readlines()])))


