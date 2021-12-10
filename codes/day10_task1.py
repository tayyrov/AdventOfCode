"""
Advent Of Code 2021
Day 10
Date: 10-12-2021
Site: https://adventofcode.com/2021/day/10
Author: Tayyrov
"""
"""
): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
"""

valid_pairs = {"()", "[]", "<>", "{}"}
points = {")": 3, "]": 57, ">": 25137, "}": 1197}

input_file = open('../input_files/day10_input', 'r')
lines = input_file.readlines()
total_score = 0
for line in lines:
    stack = []

    for char in line:
        if char not in points:
            stack.append(char)
        elif not stack:
            total_score += points[char]
            break
        elif stack[-1]+char in valid_pairs:
            stack.pop()
        else:
            total_score += points[char]
            break

print(f"The total syntax error score for those errors is {total_score}")



