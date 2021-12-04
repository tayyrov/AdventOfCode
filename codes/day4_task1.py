"""
Advent Of Code 2021
Day 4
Date: 04-12-2021
Site: https://adventofcode.com/2021/day/4
"""
import math
import sys

inputfile = open('../input_files/day4_input', 'r')
lines = inputfile.readlines()
nums = list(map(int, lines[0].split(",")))
lines.pop(0)
lines.append(lines.pop(0))
matrix = []
index = 0
last_called_index = math.inf
target_matrix_index = None
whole_matrix = []
for line in lines:
    row = list(map(int, line.split()))
    new_row = [nums.index(n) for n in row]
    if row and max(new_row) < last_called_index:
        last_called_index = max(new_row)
        target_matrix_index = index
    if not row:
        whole_matrix.append(matrix)
        transpose = [list(x) for x in zip(*matrix)]

        for row in transpose:
            if max(row) < last_called_index:
                last_called_index = max(row)
                target_matrix_index = index
        matrix = []
        index += 1
    else:
        matrix.append(new_row)
target_matrix = whole_matrix[target_matrix_index]
unmarked_sum = 0
last_called_number = nums[last_called_index]
for row in target_matrix:
    for num in row:
        if num > last_called_index:
            unmarked_sum += nums[num]

print(f" The score of the winning board is multiplication of sum of all unmarked numbers which is {unmarked_sum} \n "
      f"with number last called i.e. {last_called_number}, Thus final answer ==", unmarked_sum*last_called_number)

