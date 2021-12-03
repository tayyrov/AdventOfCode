"""
Advent Of Code 2021
Day 3
Date: 03-12-2021
Site: https://adventofcode.com/2021/day/3
"""

import sys

inputfile = open('../input_files/day3_input', 'r')

lines = inputfile.readlines()

frequency = [0] * len(lines[0].strip())
for line in lines:

    for i, num in enumerate(line.strip()):
        if num == "1":
            frequency[i] += 1
        else:
            frequency[i] -= 1

gamma = int("".join(["1"  if i > 0 else "0" for i in frequency]), 2)
epsilon = int("".join(["0"  if i > 0 else "1" for i in frequency]), 2)

final_ans = epsilon * gamma
print(f"The multiplication of depth which is {epsilon} and position which is {gamma} is {final_ans}. ")
