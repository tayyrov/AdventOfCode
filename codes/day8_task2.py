"""
Advent Of Code 2021
Day 8
Date: 08-12-2021
Site: https://adventofcode.com/2021/day/8
Author: Tayyrov
"""

from collections import defaultdict
def decoder(codes):
    decoded = defaultdict(set)
    for code in codes[:10]:
        if len(code) == 2:
            decoded[1] = set(code)
        elif len(code) == 3:
            decoded[7] = set(code)
        elif len(code) == 4:
            decoded[4] = set(code)
        elif len(code) == 7:
            decoded[8] = set(code)
    for code in codes[:10]:
        ln = len(code)
        st = set(code)
        if ln == 5:
            if len(st.intersection(decoded[1])) == 2:
                decoded[3] = st
            elif len(st.intersection(decoded[4])) == 2:
                decoded[2] = st
            else:
                decoded[5] = st
        elif ln == 6:
            if len(st.intersection(decoded[4])) == 4:
                decoded[9] = st
            elif len(st.intersection(decoded[1])) == 1:
                decoded[6] = st
            else:
                decoded[0] = st
    ans = ""
    for code in codes[11:]:
        st = set(code)
        for key, val in decoded.items():
            if st == val:
                ans += str(key)
    return int(ans)


inputfile = open('../input_files/day8_input', 'r')

lines = inputfile.readlines()


ans = 0
for l in lines:
    modified_line = l.split()
    ans += decoder(modified_line)

print(f"The sum of the decoded codes is  {ans}.")