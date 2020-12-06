#!/usr/bin/env python3

with open('input.txt') as f:
    lines = (*(l.strip() for l in f.readlines()), '')

answers = set()
count = 0
for line in lines:
    if not line:
        count += len(answers)
        answers = set()
    answers.update(line)

print(count)
