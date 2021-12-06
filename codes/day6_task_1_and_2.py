"""
Advent Of Code 2021
Day 6
Date: 06-12-2021
Site: https://adventofcode.com/2021/day/6
Author: Tayyrov
"""

import sys
import collections

file1 = open('../input_files/day6_input', 'r')

numbers = list(map(int, file1.readlines()[0].split(",")))

def code_of_advent_day6(end_day):
    start_day = 1
    count = collections.Counter(numbers)
    while start_day <= end_day:
        frequency = count.copy()
        count = collections.Counter()
        for key, val in frequency.items():
            count[key-1] = val

        count[8] = count[-1]
        count[6] += count[-1]
        del count[-1]
        start_day += 1
    return sum(val for val in count.values())
print(code_of_advent_day6(80))
print(code_of_advent_day6(256))
