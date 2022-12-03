# Advent of code Year 2022 Day 2 solution
# Author = Mike Ion
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    d_1 = {"A X":4, "A Y":8, "A Z":3,"B X":1,"B Y":5,"B Z":9,"C X":7,"C Y":2,"C Z":6}
    d_2 = {"A X":3, "A Y":4, "A Z":8,"B X":1,"B Y":5,"B Z":9,"C X":2,"C Y":6,"C Z":7}
    score_1 = 0
    score_2 = 0
    for l in input:
        l = l.strip('\n')
        score_1 += d_1[l]
        score_2 += d_2[l]

print("Part One : "+ str(score_1))

print("Part Two : "+ str(score_2))