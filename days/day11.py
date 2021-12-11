#!/usr/bin/env python
def main():
    # class color used for prettifying the terminal output
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    filename = './inputs/day11.txt'

    energies = []
    with open(filename) as f:
        for line in f.readlines():
            energies.append([int(char) for char in line.strip()])

    ### The main loop works in the following steps:
    ###     1. Increase the energy level of all octopi by 1
    ###     2. Check if any energy level is above 9. If yes, FLASH, and increase the energy of all 9 adjacent octopi by 1.
    ###     3. Repeat Step 2 until either no octopus is above energy level 9 who has not flashed
    ### Advanced one time-step and repeat from step 1.

    directions = [[0, 1], [1, 0], [1, 1], [0, -1], [-1, 0], [-1, 1], [1, -1], [-1, -1]] # directions towards all 9 adjacents
    flash_state = [[0 for j in range(10)] for i in range(10)]   # 0 = no flash, 1 = flash expended
    n = 0       # start step
    n_1 = 100   # amount of time-steps for part 1
    n_octopi = 100      # amount of octopi (10 x 10)
    flash_counter = 0   # counts flashes

    while sum([sum(row) for row in flash_state]) != n_octopi:
        primed = []   # list of primed (about to flash) octopi

        # reset flash state
        flash_state = [[0 for j in range(10)] for i in range(10)]

        # Step 1
        for row, _ in enumerate(energies):
            for col, _ in enumerate(energies[row]):
                energies[row][col] += 1
                if energies[row][col] > 9:
                    primed.append([row, col])

        # Step 2 + Step 3
        while primed:
            for row, col in primed:
                flash_state[row][col] = 1
                flash_counter += 1
                for direction in directions:
                    try:
                        if row + direction[0] >= 0 and col + direction[1] >= 0:
                            energies[row + direction[0]][col + direction[1]] += 1
                            if energies[row + direction[0]][col + direction[1]] > 9 and flash_state[row + direction[0]][col + direction[1]] == 0 and [row + direction[0], col + direction[1]] not in primed:
                                primed.append([row + direction[0], col + direction[1]])
                    except IndexError:
                        pass
                primed = primed[1:]

        # Reset all energies which have flashed
        for row, _ in enumerate(energies):
            for col, _ in enumerate(energies[row]):
                if flash_state[row][col] == 1:
                    energies[row][col] = 0

        # advance one step
        n += 1

        if n == n_1:
            print()
            print(f"{color.YELLOW}[Part 1] Total amount of flashes after {n+1} steps: {flash_counter}{color.END}")

    print(f"{color.CYAN}[Part 2] Synchronization first occurs after {n+1} steps, after a total of {flash_counter} flashes{color.END}.")




if __name__ == '__main__':
    main()