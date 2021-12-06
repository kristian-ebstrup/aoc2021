#!/usr/bin/env python
filename = "./inputs/day3.txt"

counter = []
line_count = 0
with open(filename) as f:
    for line in f.readlines():
        line_count += 1
        if not counter:
            for char in line:
                if char.isnumeric():
                    counter.append(int(char))
        else:
            for index, char in enumerate(line):
                if char.isnumeric():
                    counter[index] += int(char)                    

gamma = ''
gamma_binary = 0
epsilon = ''
for val in counter:
    # Bit-shifting (alternative solution)
    gamma_binary <<= 1
    if val > line_count / 2:
        gamma_binary += 1
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'                

print(f'Gamma rate: (bin) {gamma} | (dec) {int(gamma, 2)}')
print(f'Epsilon rate: (bin) {epsilon} | (dec) {int(epsilon, 2)}')
print(f'Power consumption: Gamma * Epsilon = {int(gamma, 2) * int(epsilon, 2)}')