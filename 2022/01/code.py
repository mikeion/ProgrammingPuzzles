# Advent of Code Year 2022 Day 1 solution
# Author = Mike Ion
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    s = 0
    sums = []
    for n in input:
        n = n.strip("\n")
        if n != "":
            s += int(n)
        else:
            sums.append(s)
            s = 0
sums = sorted(sums, reverse=True)
print("Part One : "+ str(max(sums)))

print("Part Two : "+ str(sum(sums[:3])))