"""
Advent Of Code 2021
Day 11
Date: 11-12-2021
Site: https://adventofcode.com/2021/day/11
Author: Tayyrov
"""


def isValid(r, c):
    return 0 <= c < cols and 0 <= r < rows


input_file = open('../input_files/day11_input', 'r')

matrix = [list(map(int, list(line.strip()))) for line in input_file.readlines()]

rows = len(matrix)
cols = len(matrix[0])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]

steps = 0
total_flashes = 0
while steps < 100:
    stack = []
    flashed = set()
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 9:
                stack.append((r,c))
                total_flashes += 1
                flashed.add((r,c))
                matrix[r][c] = 0
            else:
                matrix[r][c] +=1
    while stack:
        r,c = stack.pop()
        for dx, dy in directions:
            new_r, new_c = r+dx, c+dy

            if isValid(new_r, new_c) and (new_r, new_c) not in flashed:
                if matrix[new_r][new_c] == 9:
                    total_flashes += 1
                    flashed.add((new_r, new_c))
                    matrix[new_r][new_c] = 0
                    stack.append((new_r, new_c))
                else:
                    matrix[new_r][new_c] += 1
    steps += 1

print(total_flashes)