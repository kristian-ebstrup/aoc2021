#!/usr/bin/env python
filename = "./inputs/day6.txt"

# import timer string
timers = []
with open(filename) as f:
    for line in f.readlines():
        timers.append(line)

# parse timers
timers = timers[0].split(',')
timers[-1] = timers[-1][0]

# convert to list of ints:
timers = [int(char) for char in timers]

# time loop (days)
t_start = 0
t_end = 80
print(f"Amount of lanternfish at t = {t_start} days: {len(timers)}")

for t in range(t_start, t_end):
    for i in range(len(timers)):
        timers[i] -= 1
        # birth of a new lanternfish
        if timers[i] < 0:
            timers.append(8)
            timers[i] = 6
    if t == t_end - 1:
        print(f"Amount of lanternfish at t = {t + 1} days: {len(timers)}", end="\n")
    else:
        print(f"Amount of lanternfish at t = {t + 1} days: {len(timers)}", end="\r")