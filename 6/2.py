#!/usr/bin/env python

filename = 'input'

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

# set up lanternfish array based on their timer
max_timer = 8
lanternfish = [0 for i in range(max_timer + 1)]

# input starting lanternfish into array
for timer in timers:
    lanternfish[timer] += 1

# time loop (days)
t_start = 0
t_end = 256
print(f"Amount of lanternfish at t = {t_start} days: {sum(lanternfish)}")

for t in range(t_start, t_end):
    birthers = lanternfish[0]
    lanternfish = lanternfish[1:]
    lanternfish.append(birthers)
    lanternfish[6] += birthers
    print(f"Amount of lanternfish at t = {t + 1} days: {sum(lanternfish)}", end="\n")