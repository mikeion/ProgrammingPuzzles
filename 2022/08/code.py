# Advent of code Year 2022 Day 8 solution
# Author = Mike Ion
# Date = December 2022

import numpy as np
import copy

def open_file(code="code.py", file="input.txt"):
    forest = list(map(str, open((__file__.rstrip(code)+file), 'r').read().split('\n')))
    # Create matrix
    for a in forest:
        lst = []
        for digit in a:
            lst.append(int(digit))
        forest[forest.index(a)] = lst
    
    # First determine the outer layer (automatically shows up)
    # 2 * (width + height) - 4

    width = len(forest[0])
    height = len(forest)
    visible = 2 * (width + height) - 4
    # Create a list to put all the scenic scores in
    scenic = []

    # Now to loop through the inner layers
    # looping through the (width - 2) * (height - 2) matrix
    for i in range(width)[1:-1]:
        for j in range(height)[1:-1]:
            tree = forest[i][j]
            # For part 2, these will keep track of the viewing distance in each direction
            # from the tree.
            l, r, u, d = 0, 0, 0, 0
            # Determine the list of trees in each direction: north, south, east, west
            # For part 2, order matters. So for north and west, we'll need to reverse the 
            # order of the lists.
            north = [row[j] for row in forest[:i]]
            north.reverse()
            # South
            south = [row[j] for row in forest[i+1:]]
            # East
            east = forest[i][j+1:]
            # West
            west = forest[i][:j]
            west.reverse()

            # Determine if tree is tallest in any direction
            if tree > max(north) or tree > max(south) or tree > max(east) or tree > max(west):
                visible += 1
            # Now to determine the viewing distance in each direction
            # North
            for n in north:
                for k in range(len(north)):
                    if north[k] >= tree:
                        break
                u = k+1
            # South
            for s in south:
                for y in range(len(south)):
                    if south[y] >= tree:
                        break
                d = y+1
            # West
            for w in west:
                for z in range(len(west)):
                    if west[z] >= tree:
                        break
                l = z+1
            # East
            for e in east:
                for m in range(len(east)):
                    if east[m] >= tree:
                        break
                r = m+1         
            scenic.append(u*d*l*r)
    scenic_score = max(scenic)
    return visible, scenic_score

visible, scenic_score = open_file()

print("Part One : "+ str(visible))

print("Part Two : "+ str(scenic_score))