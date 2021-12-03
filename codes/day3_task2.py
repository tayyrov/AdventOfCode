"""
Advent Of Code 2021
Day 3
Date: 03-12-2021
Site: https://adventofcode.com/2021/day/3
"""

import sys

inputfile = open('../input_files/day3_input', 'r')

lines = inputfile.readlines()
def frequency_calculator(lines, index, type):
    ones = sum(1 for line in lines if line[index] == "1")
    zeros = sum(1 for line in lines if line[index] == "0")
    if type == "oxygen":
        if ones >= zeros:
                return  [line for line in lines if line[index] == "1"]
        else:
            return [line for line in lines if line[index] == "0"]
    else:
        if ones < zeros:
                return  [line for line in lines if line[index] == "1"]
        else:
            return  [line for line in lines if line[index] == "0"]


oxygen_done = False
co_done = False
lines_oxygen = lines[::]
lines_co = lines[::]
for i in range(12):
    lines_oxygen = frequency_calculator(lines_oxygen, i, "oxygen")
    if len(lines_oxygen) == 1 and not oxygen_done:
        oxygen_rating = int(lines_oxygen[0], 2)
        oxygen_done = True
    lines_co = frequency_calculator(lines_co, i, "co")
    if len(lines_co) == 1 and not co_done:
        co_rating = int(lines_co[0], 2)
        co_done = True


final_ans = oxygen_rating * co_rating
print(f"The multiplication of oxygen rating which is {oxygen_rating} and co2 rating which is {co_rating} is {final_ans}. ")
