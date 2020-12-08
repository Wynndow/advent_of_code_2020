#!/usr/bin/env python3
import re
from collections import defaultdict

with open('input.txt') as f:
    rules = (re.findall(r'((?:^|\d+ )\w+ \w+)', l) for l in f.readlines())
lookup = defaultdict(list)

for rule in rules:
    for bag in rule[1:]:
        lookup[rule[0]].append((int(bag[0]), bag.split(' ', 1)[-1]))

def count_contents(bag):
    if not lookup[bag]:
        return 0
    return sum([inner_bag[0] + (inner_bag[0] * count_contents(inner_bag[1])) for inner_bag in lookup[bag]])

print(count_contents('shiny gold'))
