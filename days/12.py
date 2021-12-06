#!/usr/bin/env python
filename = "./inputs/day1.txt"

measurements = []
with open(filename) as f:
    for line in f.readlines():
        measurements.append(int(line))

count = sum([1 for i in range(len(measurements)) if sum(measurements[i+1:i+4]) > sum(measurements[i:i+3])])

print(f"{count} increases out of {len(measurements)} entries")