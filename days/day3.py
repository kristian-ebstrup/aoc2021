#!/usr/bin/env python

def main():
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

    print(f'[Part 1]')
    print(f'Gamma rate: (bin) {gamma} | (dec) {int(gamma, 2)}')
    print(f'Epsilon rate: (bin) {epsilon} | (dec) {int(epsilon, 2)}')
    print(f'Power consumption: Gamma * Epsilon = {int(gamma, 2) * int(epsilon, 2)}')

    entries = []
    with open(filename) as f:
        for line in f.readlines():
            entries.append(line[:-1])   # [:-1] scrubs line-break

    # Identify oxygen generator rating
    pos = 0
    n_active = len(entries)
    oxy_entries = entries
    while n_active != 1:
        counter = 0
        for entry in oxy_entries:
            counter += int(entry[pos])
        
        if counter < n_active / 2:
            most_common = '0'
        else:
            most_common = '1'
        #print(f"counter: {counter}, n_active: {n_active}, most_common: {most_common}")

        oxy_entries = [oxy_entries[i] for i in range(n_active) if oxy_entries[i][pos] == most_common]
        n_active = len(oxy_entries)
        pos += 1

    # Identify CO2 scrubber rating
    pos = 0
    n_active = len(entries)
    coo_entries = entries
    while n_active != 1:
        counter = 0
        for entry in coo_entries:
            counter += int(entry[pos])

        if counter < n_active / 2:
            most_common = '0'
        else:
            most_common = '1'

        coo_entries = [coo_entries[i] for i in range(n_active) if coo_entries[i][pos] != most_common]
        n_active = len(coo_entries)
        pos += 1

    oxy_entries = oxy_entries[0]
    coo_entries = coo_entries[0]

    print()
    print(f'[Part 2]')
    print(f"R_OXY: (bin) {oxy_entries}")
    print(f"R_CO2: (bin) {coo_entries}")
    print(f"R_LS: (dec) R_OXY * R_CO2 = {int(oxy_entries, 2) * int(coo_entries, 2)}")

if __name__ == '__main__':
    main()