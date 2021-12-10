#!/usr/bin/env python
def main():
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

    # set up lanternfish array based on their timer
    max_timer = 8
    lanternfish = [0 for i in range(max_timer + 1)]

    # input starting lanternfish into array
    for timer in timers:
        lanternfish[timer] += 1

    # time loop (days)
    t_start = 0
    t_part1 = 80
    t_end = 256
    print(f"Amount of lanternfish at t = {t_start} days: {sum(lanternfish)}")

    for t in range(t_start, t_end):
        birthers = lanternfish[0]
        lanternfish = lanternfish[1:]
        lanternfish.append(birthers)
        lanternfish[6] += birthers
        if t == t_part1 - 1:
            print(f"[Part 1] Amount of lanternfish at t = {t + 1} days: {sum(lanternfish)}", end="\n")
        else:
            print(f"[Part 1] Amount of lanternfish at t = {t + 1} days: {sum(lanternfish)}", end="\r")
        if t == t_end - 1:
            print(f"[Part 2] Amount of lanternfish at t = {t + 1} days: {sum(lanternfish)}", end="\n")
        else:
            print(f"[Part 2] Amount of lanternfish at t = {t + 1} days: {sum(lanternfish)}", end="\r")

if __name__ == '__main__':
    main()