"""
Advent Of Code 2021
Day 8
Date: 08-12-2021
Site: https://adventofcode.com/2021/day/8
Author: Tayyrov
"""

inputfile = open('../input_files/day8_input', 'r')

lines = inputfile.readlines()
ans = 0
for l in lines:
    modified_line = l.split()
    counting_start = False
    for code in modified_line:
        if code == "|":
            counting_start = True

        if counting_start and len(code) in {2, 4, 3, 7}:
            ans += 1

print(f"The digits 1, 4, 7, or 8 appears {ans} times in this decoded samples")