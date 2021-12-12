"""
Advent Of Code 2021
Day 12
Date: 12-12-2021
Site: https://adventofcode.com/2021/day/12
Author: Tayyrov
"""
from collections import defaultdict

input_file = open('../input_files/day12_input', 'r')

matrix = [line.strip().split("-") for line in input_file.readlines()]

graph = defaultdict(list)

for u, v in matrix:
    graph[u].append(v)
    graph[v].append(u)

paths = [["start"]]
seen = []
total_unique_paths = set()
while paths:
    current_path = paths.pop()
    for node in graph[current_path[-1]]:
        if node.islower() and node in current_path:
            continue
        updated_path = current_path + [node]
        if updated_path in seen:
            continue
        seen.append(updated_path)
        if node == "end":
            total_unique_paths.add(tuple(updated_path))
        else:
            paths.append(updated_path)

print(f"The total number of unique paths is {len(total_unique_paths)}")