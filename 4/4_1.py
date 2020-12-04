#!/usr/bin/env python3
import re

must_haves = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valid_passports = 0
codes = set()

with open('input.txt') as f:
    for line in f:
        if line == '\n':
            if must_haves.issubset(codes): valid_passports += 1
            codes = set()
        codes.update(tuple(re.findall(r'(.{3}):', line)))

if must_haves.issubset(codes): valid_passports += 1
print(valid_passports)
