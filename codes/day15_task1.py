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

input_file = open('../input_files/day15_input', 'r')

matrix = [list(map(int, line.strip())) for line in input_file.readlines()]
rows = len(matrix)
cols = len(matrix[0])

q = [(0,0,0)]
directions = {(1, 0), (0, 1), (0, -1), (-1, 0)}
heapq.heapify(q)
distances = defaultdict(int) # this is not necessary per se as we can print put when we encounter the target first time
visited = set()

while q:
    dist, x, y = heapq.heappop(q)
    # if (x, y) == (rows-1, cols-1):
    #     print(dist)
    #     break
    if (x,y) in visited:
        continue
    visited.add((x,y))
    distances[(x, y)] = dist
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if isValid(nx, ny) and (nx, ny) not in distances: # first time is the shortest -do not update
            new_dist = matrix[nx][ny] + dist
            distances[(nx, ny)] = new_dist
            heapq.heappush(q, (new_dist, nx, ny))
print(f"The lowest total risk of any path from the top left to the bottom right is {distances[rows-1,cols-1]}")


