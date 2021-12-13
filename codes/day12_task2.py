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

path_stack = [["start"]]
seen = []
total_unique_paths = []
while path_stack:
    current_path = path_stack.pop()
    for node in graph[current_path[-1]]:
        if node == "start":
            continue
        updated_path = current_path + [node]
        if updated_path in seen:
            continue
        if node.islower() and node != "end":
            cnt = updated_path.count(node)
            if cnt > 2:
                continue
            cnt = [updated_path.count(char) for char in updated_path if char.islower()].count(2)

            if cnt > 2:
                continue

        seen.append(updated_path)
        if node == 'end':
            if updated_path not in total_unique_paths:
                total_unique_paths.append(updated_path)
        else:
            path_stack.append(updated_path)
print(f"The total number of valid paths is {len(total_unique_paths)}")
