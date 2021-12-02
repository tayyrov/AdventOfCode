"""
Advent Of Code 2021
Day 2
Date: 02-12-2021
Site: https://adventofcode.com/2021/day/2
"""

import sys

inputfile = open('../input_files/day2_input', 'r')

lines = inputfile.readlines()
position = 0
depth = 0
aim = 0
for line in lines:
    command, step = line.split()
    int_step = int(step)
    if command == "forward":
        position += int_step
        depth += int_step*aim
    elif command == "down":
        aim += int_step
    elif command == "up":
        aim -= int_step
    else:
        print("Unexpected input")
final_ans = position * depth
print(f"The multiplication of depth which is {depth} and position which is {position} is {final_ans}. ")