"""
Advent Of Code 2021
Day 15
Date: 15-12-2021
Site: https://adventofcode.com/2021/day/15
Author: Tayyrov
"""
import heapq
from collections import defaultdict


def isValid(row, col):
    return 0 <= row < rows and 0 <= col < cols


def row_modifier(row):
    return [n + 1 if n < 9 else 1 for n in row]


input_file = open('../input_files/day15_input', 'r')

matrix = [list(map(int, line.strip())) for line in input_file.readlines()]
R = len(matrix)
C = len(matrix[0])
new_matrix = []


# for row in matrix:
#     temp = row[::]
#     for _ in range(4):
#         x = row_modifier(temp[-rows:])
#         print(len(x))
#         temp.extend(x)
#     new_matrix.append(temp)
# for i in range(4*rows):
#     new_matrix.append(row_modifier(new_matrix[i]))

def getValue(r, c):
    x = matrix[r % R][c % C] + r // R + c // C
    return (x - 1) % 9 + 1

q = [(0, 0, 0)]
directions = {(1, 0), (0, 1), (0, -1), (-1, 0)}
heapq.heapify(q)
distances = defaultdict(int)  # this is not necessary per se as we can print put when we encounter the target first time
visited = set()
rows = 5 * R
cols = 5 * C

while q:
    dist, x, y = heapq.heappop(q)
    # if (x, y) == (rows-1, cols-1):
    #     print(dist)
    #     break
    if (x, y) in visited:
        continue
    visited.add((x, y))
    distances[(x, y)] = dist
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if isValid(nx, ny) and (nx, ny) not in distances:  # first time is the shortest -do not update
            new_dist = getValue(nx, ny) + dist
            distances[(nx, ny)] = new_dist
            heapq.heappush(q, (new_dist, nx, ny))
print(f"The lowest total risk of any path from the top left to the bottom right is {distances[rows - 1, cols - 1]}")
