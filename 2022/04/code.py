# Advent of code Year 2022 Day 4 solution
# Author = Mike Ion
# Date = December 2022

import re
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [s.strip() for s in input_file.readlines()]
    no_of_pairs = 0
    over_lapping = 0
    for l in input:
        l = l.split(',')
        assignment_1 = re.search(r"([0-9]+)-([0-9]+)", l[0])
        left_1, right_1 = int(assignment_1.group(1)), int(assignment_1.group(2))
        assignment_2 = re.search(r"([0-9]+)-([0-9]+)", l[1])
        left_2, right_2 = int(assignment_2.group(1)), int(assignment_2.group(2))
        # part 1 - note this case is more restrictive and adds in the part 2 case
        if ((left_1 <= left_2) & (right_1 >= right_2)) or ((left_2 <= left_1) & (right_2 >= right_1)):
            print(f'({left_1}, {right_1}) in ({left_2}, {right_2}) or ({left_2}, {right_2}) in ({left_1}, {right_1})')
            no_of_pairs +=1
            over_lapping +=1
        # part 2 - note it's overlapping if the largest of the left endpoints is 
        # less than smallest of the right endpoints.        
        elif max(left_1, left_2) <= min(right_1, right_2):
            over_lapping +=1
        else:
            print(f'({left_1}, {right_1}) in ({left_2}, {right_2}) or ({left_2}, {right_2}) in ({left_1}, {right_1})''doesn\'t work')

print("Part One : "+ str(no_of_pairs))

print("Part Two : "+ str(over_lapping))