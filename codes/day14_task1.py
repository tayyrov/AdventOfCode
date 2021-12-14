"""
Advent Of Code 2021
Day 14
Date: 14-12-2021
Site: https://adventofcode.com/2021/day/14
Author: Tayyrov
"""

from collections import  defaultdict, Counter

letters = [line.strip() for line in open('../input_files/day14_input', 'r').readlines() if len(line) > 10][0]

codes = {line.strip().split("->")[0].strip():line.strip().split("->")[1].strip() for line
         in open('../input_files/day14_input', 'r').readlines() if "->" in line}

steps = 10
while steps > 0:
    new_letters = letters[0]
    for first, second in zip(letters, letters[1:]):
        key = first+second
        if key in codes:
            insert_letter = codes[key]
            new_letters += insert_letter+second
        else:
            new_letters += second

    letters = new_letters
    steps -= 1
letter_counting = Counter(letters)
sorted_frequency = sorted(letter_counting.values())
print(len(letters))
diff_of_max_min = sorted_frequency[-1] - sorted_frequency[0]

print(f" The quantity of the most common element and subtract the quantity of the least common element is {diff_of_max_min}")
