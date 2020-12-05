#!/usr/bin/env python3

print(max((int(l.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2) for l in open('input.txt').readlines())))


