"""
Advent Of Code 2021
Day 1
Date: 01-12-2021
Site: https://adventofcode.com/2021/day/1
"""

import sys

file1 = open('../input_files/day1_input1.txt', 'r')

ans = 0
nums = list(map(int, file1.readlines()))
print(nums)
ln = len(nums)
for i in range(ln-3):
    num1 = nums[i] + nums[i+1] + nums[i+2]
    num2 = nums[i+1] + nums[i+2] + nums[i+3]
    if num1 < num2:
        ans += 1



print(ans)

