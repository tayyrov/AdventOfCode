"""
Advent Of Code 2021
Day 10
Date: 10-12-2021
Site: https://adventofcode.com/2021/day/10
Author: Tayyrov
"""


valid_pairs = {"()", "[]", "<>", "{}"}
points = {"(": 1, "[": 2, "{": 3, "<": 4}

input_file = open('../input_files/day10_input', 'r')
lines = input_file.readlines()
total_scores = []
for line in lines:
    stack = []
    for char in line.strip():
        if char in points:
            stack.append(char)
        elif stack[-1]+char in valid_pairs:
            stack.pop()
        else:
            break
    else:
        total_score = 0
        while stack:
            char = stack.pop()
            total_score = total_score*5+points[char]
        total_scores.append(total_score)
total_scores.sort()

print(f"The middle score for those errors is {total_scores[len(total_scores)//2]}")



