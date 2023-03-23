# Advent of code Year 2022 Day 7 solution
# Author = Mike Ion
# Date = December 2022

from collections import defaultdict

def open_file(code="code.py", file="input.txt"):
    with open((__file__.rstrip(code)+file), 'r') as input_file:
        f = input_file.read().splitlines()
        return f

# Write a function to find directories and files
def traverse(code="code.py", file="input.txt"):
    f = open_file(code, file)
    current_dir = []
    
    # Dictionary where the key will be a tuple attaching the current directory
    # and the value will be the size (integer). defaultdict is used to avoid
    # key errors.

    paths = defaultdict(int)

    for line in f:
        line = line.split()
        # 5 cases: 1)$ cd .., 2)$ cd directory, 3)$ ls, 4) file, 5) dir
        # First 3 have $, last 2 don't. Just continue when we see $ ls,
        # if dir shows up, the loop will go around again. 
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    current_dir.pop()
                else:
                    current_dir.append(line[2])
        elif line[1] == "ls":
            continue
        elif line[0] != "dir":
            for i in range(len(current_dir)):
                paths[tuple(current_dir[:i+1])] += int(line[0]) 
    print(paths)
    return paths    

def part_1(code="code.py", file="input.txt"):
    f = open_file(code, file)
    paths = traverse(code, file)
    return sum(size for size in paths.values() if size < 100000)

def part_2(code="code.py", file="input.txt"):
    f = open_file(code, file)
    paths = traverse(code, file)
    space = 30000000 - (70000000 - paths[('/',)])
    return min(size for size in paths.values() if size >= space)

print("Part One : "+ str(part_1()))

print("Part Two : "+ str(part_2()))