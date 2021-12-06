#!/usr/bin/env python
filename = "./inputs/day1.txt"

count = 0
line_count = 0
previous_line = 0
with open(filename) as f:
    for line in f.readlines():
        line = int(line)
        if previous_line < line and line_count > 0:
            count += 1
        previous_line = line
        line_count += 1

print(f"{count} increases out of {line_count} entries")