"""
Advent Of Code 2021
Day 17
Date: 17-12-2021
Site: https://adventofcode.com/2021/day/17
Author: Tayyrov
"""
input_file = open('../input_files/day17_input', 'r')

line = input_file.readline() + "."

numbers = []
temp = ""
for i, char in enumerate(line):
    if char.isdigit():
        if not temp and line[i-1] == "-":
            temp += "-"
        temp += char
    else:
        if temp:
            numbers.append(int(temp))
            temp = ""

x_min, x_max, y_min, y_max = numbers

def in_target(x, y):
    if x_min <= x <= x_max and y_min <= y <= y_max:
        return True
    return False
best = 0
count = 0
steps = 500
for xx in range(500):
    for yy in range(-100, 500):
        x = 0
        y = 0
        dx = xx
        dy = yy
        temp = 0
        found = False
        for st in range(steps):
            x += dx
            y += dy
            if y > temp:
                temp = y
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1
            if in_target(x, y):
                found = True
        if found:
            count += 1
            if temp > best:
                best = temp

print(f"Part1: The highest reachable y position is {best}")
print(f"Part2: The number distinct initial velocity values that reaches to target is {count}")



