# Advent of code Year 2022 Day 6 solution
# Author = Mike Ion
# Date = December 2022

def open_file(code="code.py", file="input.txt"):
    with open((__file__.rstrip(code)+file), 'r') as input_file:
        f = input_file.read()
        return f

def part_1(code="code.py", file="input.txt"):
    f = open_file(code, file)
    for i in range(0, len(f)-4):
        buffer = f[i:i+4]
        buffer_set = set(buffer)
        if len(buffer_set) == 4:
            return i+4
def part_2(code="code.py", file="input.txt"):
    f = open_file(code, file)
    for i in range(0, len(f)-14):
        buffer = f[i:i+14]
        buffer_set = set(buffer)
        if len(buffer_set) == 14:
            return i+14

print("Part One : "+ str(part_1()))

print("Part Two : "+ str(part_2()))