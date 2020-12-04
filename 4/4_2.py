#!/usr/bin/env python3
import re

rules = (
    ('byr', lambda x: 1920 <= int(x) <= 2002),
    ('iyr', lambda x: 2010 <= int(x) <= 2020),
    ('eyr', lambda x: 2020 <= int(x) <= 2030),
    ('hgt', lambda x: bool(re.match(r'^((1[5-8][0-9])|(19[0-3]))cm$|^((59)|(6[0-9])|(7[0-6]))in$', x))),
    ('hcl', lambda x: bool(re.match(r'^#[0-9a-f]{6}$', x))),
    ('ecl', lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')),
    ('pid', lambda x: bool(re.match(r'^[0-9]{9}$', x))),
)
valid_passports = 0
code_values = {}

with open('input.txt') as f:
    batch_lines = (*(l.strip() for l in f.readlines()), '')

for line in batch_lines:
    if not line:
        try:
            if all([rule[1](code_values[rule[0]]) for rule in rules]): valid_passports += 1
        except KeyError:
            pass
        code_values = {}
    code_values = {**code_values, **{k: v for k, v in re.findall(r'(.{3}):(.*?)(?: |$)', line)}}

print(valid_passports)
