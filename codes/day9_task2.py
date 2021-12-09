"""
Advent Of Code 2021
Day 9
Date: 09-12-2021
Site: https://adventofcode.com/2021/day/9
Author: Tayyrov
"""

def isvalid(row, column):
    return 0 <= column < cols and 0 <= row < rows


input_file = open('../input_files/day9_input', 'r')

matrix = input_file.readlines()

rows = len(matrix)
cols = len(matrix[0].strip())
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
sizes = []
visited = set()
#DFS
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] != "9" and (r, c) not in visited:
            visited.add((r, c))
            size = 1
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                for dx, dy in directions:
                    new_r, new_c = dx + r, dy + c
                    if isvalid(new_r, new_c) and (new_r, new_c) not in visited and matrix[new_r][new_c] != "9":
                        size += 1
                        stack.append((new_r, new_c))
                        visited.add((new_r, new_c))
            sizes.append(size)
sizes.sort(reverse=True)
sizes_of_three_largest_basins = sizes[0] * sizes[1] * sizes[2]
print(f"The multiplication of the sizes of the three largest basins gives {sizes_of_three_largest_basins}")
