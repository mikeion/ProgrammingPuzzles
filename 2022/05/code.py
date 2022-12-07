# Advent of code Year 2022 Day 5 solution
# Author = Mike Ion
# Date = December 2022

import numpy as np
import re
import copy

def open_file(code="code.py", file="input.txt"):
    with open((__file__.rstrip(code)+file), 'r') as input_file:
        f = [s.strip() for s in input_file.readlines()]
        return f

def create_dict(fl):
    # Grab the input
    stack = fl[:8]
    # Add the blank spaces and the letters in order per layer of the stack
    rows = [[row[(j*4)+1] for j in range(9)] for row in stack]
    # Create a dictionary for the stack and add letters with the top at postition 0
    stack_dict = {}
    for i in range(9):
        stack_dict[i+1] = []
    for row in rows:
        for i, letter in enumerate(row):
            if letter != " ":
                stack_dict[i+1].append(letter)
    # Grab the instructions
    return stack_dict

def part_1(code="code.py", file="input.txt"):
    f = open_file(code, file)
    stack_dict = create_dict(f)
    instructions = f[10:]
    for line in instructions:
        # We want to parse the instructions to grab the necessary numbers
        line_split = line.split()
        # The move instruction is in the second spot, this says how many times to 
        # move elements from one list to the other.
        for i in range(int(line_split[1])):
            # Pop the top of the stack from the index 5 and add it to the correct spot
            stack_dict[int(line_split[5])].insert(0, stack_dict[int(line_split[3])].pop(0))
    final_msg = ""
    for key in stack_dict.keys():
        final_msg += stack_dict[key][0]
    return final_msg

def part_2(code="code.py", file="input.txt"):
    f = open_file(code, file)
    stack_dict = create_dict(f)
    print(stack_dict)
    instructions = f[10:]
    for line in instructions:
        # We want to parse the instructions to grab the necessary numbers
        line_split = line.split()
        print(f'stackdict 2 is {stack_dict[2]}')
        sect = stack_dict[int(line_split[3])][:int(line_split[1])]
        print(f' sect is {sect}')
        for i in sect[::-1]:
            stack_dict[int(line_split[3])].remove(i)
            stack_dict[int(line_split[5])].insert(0, i)
    final_msg = ""
    for key in stack_dict.keys():
        final_msg += stack_dict[key][0]
    return final_msg


print("Part One : "+ part_1())
print("Part One : "+ part_2())
