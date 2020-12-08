#!/usr/bin/env python3

with open('input.txt') as f:
    instructions = [i.strip().split() for i in f.readlines()]

instructions_run = set()
accumulator = 0
instruction_index = 0
while True:
    if instruction_index in instructions_run: break
    instructions_run.add(instruction_index)
    op, arg = instructions[instruction_index]
    instruction_index += 1
    if op == 'acc':
        accumulator += int(arg)
    elif op == 'jmp':
        instruction_index += int(arg) - 1


print(accumulator)

