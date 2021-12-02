"""
Advent Of Code 2021
Day 1
Date: 01-12-2021
Site: https://adventofcode.com/2021/day/1
"""

import sys

file1 = open('../input_files/day1_input', 'r')

ans = 0
nums = list(map(int, file1.readlines()))
ln = len(nums)
for i in range(1, ln):
    if nums[i-1] < nums[i]:
        ans += 1



print(ans)

