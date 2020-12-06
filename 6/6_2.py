#!/usr/bin/env python3
from collections import Counter

with open('input.txt') as f:
    lines = (*(l.strip() for l in f.readlines()), '')

answers = Counter()
count = 0
group_size = 0
for line in lines:
    if not line:
        count += len(list(filter(lambda x: x[1] == group_size, answers.items())))
        answers = Counter()
        group_size = 0
        continue
    group_size += 1
    for answer in line:
        answers[answer] += 1

print(count)
