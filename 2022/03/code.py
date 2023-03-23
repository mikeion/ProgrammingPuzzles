# Advent of code Year 2022 Day 3 solution
# Author = Mike Ion
# Date = December 2022
import re


with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [s.strip() for s in input_file.readlines()]
    priority_1 = 0
    priority_2 = 0
  
    for l in input:
        comp_1 = l[:len(l)//2]
        comp_2 = l[len(l)//2:]
        both_comps = str(set(comp_1) & set(comp_2))
        both_comps = re.sub(r'\W+', '', both_comps)
        for i in both_comps:
        # Note ord('a')=96 and ord('A')=65 so we can assign priority 
        # to be ord('lower') - 96 and ord=('upper') -38
            if i.islower() is True:
                priority_1 += ord(i) - 96
            else:
                priority_1 += ord(i) - 38
    for j in range(len(input)//3):
        all_comps = str(set(input[3*j]) & set(input[3*j+1]) & set(input[3*j+2]))
        all_comps = re.sub(r'\W+', '', all_comps)
        for k in all_comps:
        # Note ord('a')=96 and ord('A')=65 so we can assign priority 
        # to be ord('lower') - 96 and ord=('upper') -38
            if k.islower() is True:
                priority_2 += ord(k) - 96
            else:
                priority_2 += ord(k) - 38



print("Part One : "+ str(priority_1))


print("Part Two : "+ str(priority_2))