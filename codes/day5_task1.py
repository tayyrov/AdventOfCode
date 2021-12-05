"""
Advent Of Code 2021
Day 5 task1
Date: 05-12-2021
Site: https://adventofcode.com/2021/day/5
"""
import sys

inputfile = open('../input_files/day5_input', 'r')
lines = inputfile.readlines()

matrix = [[0] * 1000 for _ in range(1000)]
for line in lines:
    xy1, xy2 = line.split("->")
    x1, y1 = map(int, xy1.split(","))
    x2, y2 = map(int, xy2.split(","))

    if x1 == x2:
        if y1 > y2:
            y2 , y1 = y1, y2
        for y in range(y1, y2+1):
            matrix[x1][y] += 1
    elif y1 == y2:
        if x1 > x2:
            x2, x1 = x1, x2
        for x in range(x1, x2 + 1):
            matrix[x][y1] += 1
overlapping_lines = 0
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] > 1:
            overlapping_lines += 1
print(f"The number of points where at least two lines overlap is {overlapping_lines}.")



