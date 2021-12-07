"""
Advent Of Code 2021
Day 7
Date: 07-12-2021
Site: https://adventofcode.com/2021/day/7
Author: Tayyrov
"""

import sys
import math
from statistics import mean

file1 = open('../input_files/day7_input', 'r')
numbers = list(map(int, file1.readlines()[0].split(",")))

average_value = int(mean(numbers))
answer = 0

for n in numbers:
    difference = abs(n-average_value)
    answer += difference*(difference+1)//2

print(f"The answer for day 6 task2 is {answer}.")