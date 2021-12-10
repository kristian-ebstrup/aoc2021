#!usr/bin/env python

def main():
    import numpy as np

    filename = './inputs/day7.txt'

    # extract horizontal crab positions
    pos_crabs = []
    with open(filename) as f:
        for line in f.readlines():
            pos_crabs.append(line)

    pos_crabs = [int(pos) for pos in pos_crabs[0].split(',')]

    # run from minimum crab position to max crab position and compute the fuel costs
    fuel_cost_1 = []
    fuel_cost_2 = []
    for pos_align in range(min(pos_crabs), max(pos_crabs)):
        fuel_cost_1.append(sum([abs(pos - pos_align) for pos in pos_crabs]))
        fuel_cost_2.append(sum([sum([i for i in range(1, abs(pos - pos_align) + 1)]) for pos in pos_crabs]))

    print(f"[Part 1] The best position is found to be at hor = {np.argmin(fuel_cost_1)}, with minimum fuel cost estimated to be {min(fuel_cost_1)}")

    print(f"[Part 2] The best position is found to be at hor = {np.argmin(fuel_cost_2)}, with minimum fuel cost estimated to be {min(fuel_cost_2)}")