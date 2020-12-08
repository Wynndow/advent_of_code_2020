#!/usr/bin/env python3
import re
from collections import defaultdict

with open('input.txt') as f:
    rules = (re.findall(r'(\w+ \w+)(?<!no other) bag', l) for l in f.readlines())

lookup = defaultdict(set)

for rule in rules:
    [lookup[bag].add(rule[0]) for bag in rule[1:]]

def get_containers(bag_colour):
    direct_containers = lookup[bag_colour]
    for container in direct_containers.copy():
        direct_containers.update(get_containers(container))
    return direct_containers

print(len(get_containers('shiny gold')))
