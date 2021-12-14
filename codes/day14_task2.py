"""
Advent Of Code 2021
Day 14
Date: 14-12-2021
Site: https://adventofcode.com/2021/day/14
Author: Tayyrov
"""

from collections import defaultdict, Counter

letters = [line.strip() for line in open('../input_files/day14_input', 'r').readlines() if len(line) > 10][0]

codes = {line.strip().split("->")[0].strip(): line.strip().split("->")[1].strip() for line
         in open('../input_files/day14_input', 'r').readlines() if "->" in line}

counting = defaultdict(int)
ln = len(letters)

for first, second in zip(letters, letters[1:]):
    counting[first + second] += 1

count = Counter(letters)
for _ in range(40):
    # dictionary can not modified while iterating this has to be copied before.
    new_counting = counting.copy()
    for key, val in new_counting.items():
        if key in codes:
            counting[key] -= val  # this pair is disrupted so we had to remove it
            insert_letter = codes[key]
            count[insert_letter] += val
            # new pairs are formed
            first_pair = key[0] + insert_letter
            second_pair = insert_letter + key[1]
            # add the pairs
            counting[first_pair] += val
            counting[second_pair] += val

sorted_frequency = sorted(count.values())
diff_of_max_min = sorted_frequency[-1] - sorted_frequency[0]

print(f"The difference of the most common and the least common element is {diff_of_max_min}")
