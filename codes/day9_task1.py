"""
Advent Of Code 2021
Day 9
Date: 09-12-2021
Site: https://adventofcode.com/2021/day/9
Author: Tayyrov
"""


def isValid(r, c):
    return 0 <= c < cols and 0 <= r < rows


input_file = open('../input_files/day9_input', 'r')

matrix = input_file.readlines()

rows = len(matrix)
cols = len(matrix[0].strip())
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0

for r in range(rows):
    for c in range(cols):
        point = matrix[r][c]
        all_good = True
        for x, y in directions:
            nr, nc = r + x, c + y
            if not isValid(nr, nc):
                continue
            if matrix[nr][nc] <= point:
                all_good = False
        if all_good:
            ans += int(point)+1

print(f"The sum of the risk levels of all low points is {ans}")
