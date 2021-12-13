"""
Advent Of Code 2021
Day 13
Date: 13-12-2021
Site: https://adventofcode.com/2021/day/13
Author: Tayyrov
"""
from itertools import zip_longest


def transpose(matrix):
    return [list(x) for x in zip(*matrix)]


matrix = [list(map(int, list(line.split(",")))) for line in open('../input_files/day13_input', 'r').readlines() if
          "," in line]
instructions = [(line.strip().split("=")[-2][-1], int(line.strip().split("=")[-1])) for line in
                open('../input_files/day13_input', 'r').readlines() if "fold" in line]

mx_x = 0
mx_y = 0
for x, y in matrix:
    mx_x = max(mx_x, x)
    mx_y = max(mx_y, y)

grid = [["."] * (mx_x + 1) for _ in range(mx_y + 1)]

for r in range(mx_y + 1):
    for c in range(mx_x + 1):
        if [c, r] in matrix:
            grid[r][c] = "#"
total = 0

for direction, value in instructions:
    if direction == "y":
        grid = transpose(grid)
    new_grid = []
    for row in grid:
        first_part = row[:value][::-1]
        second_part = row[value + 1:]
        temp = []
        for char1, char2 in zip_longest(first_part, second_part, fillvalue="."):
            if char1 == "#" or char2 == "#":
                temp.append("#")
            else:
                temp.append(".")
        new_grid.append(temp)
    grid = new_grid[::]
    if direction == "y":
        grid = transpose(grid)
for row in grid[::-1]:
    print(*row[::-1])
