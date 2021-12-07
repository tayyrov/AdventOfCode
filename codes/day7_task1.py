"""
Advent Of Code 2021
Day 7
Date: 07-12-2021
Site: https://adventofcode.com/2021/day/7
Author: Tayyrov
"""

import sys

file1 = open('../input_files/day7_input', 'r')

numbers = list(map(int, file1.readlines()[0].split(",")))
numbers.sort()

middle = numbers[len(numbers)//2]

ans = 0

for n in numbers:
    ans += abs(middle-n)

print(ans)
