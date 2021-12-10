#!/usr/bin/env python

def main():
    filename = './inputs/day9.txt'
    marker = ' '    # marker for marking the searched part
    VERBOSE = False
    MAPPING = False

    height_map = []
    with open(filename) as f:
        for line in f.readlines():
            height_map.append([char for char in line[:-1]])        # [:-1] removes the line-break character
            
    # PART 1
    valleys = []    # save lowest points in valleys array
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for row in range(len(height_map)):
        for col in range(len(height_map[0])):
            boundaries = 0
            adjacents = 0
            
            # Set boundary flag if at top or left boundary
            if row == 0 or col == 0:
                boundaries += 1
            
            # Check adjacents; add 0 if adjacent is smaller, 1 if adjacent is bigger
            for direction in directions:
                try:
                    if int(height_map[row + direction[0]][col + direction[1]]) - int(height_map[row][col]) > 0 and (row + direction[0] >= 0 and col + direction[1] >= 0):
                        adjacents += 1
                except IndexError:
                    # Set boundary flag if at right or bottom boundary.
                    boundaries += 1
            
            if adjacents == 4 - boundaries:
                if boundaries == 0 and VERBOSE:
                    print(f"Valley identified at coordinates ({row}, {col}).")
                    print(f"Displaying map of surrounding cliffs:")
                    print(f"{height_map[row-1][col-1]} {height_map[row-1][col]} {height_map[row-1][col+1]}")
                    print(f"{height_map[row][col-1]} {height_map[row][col]} {height_map[row][col+1]}")
                    print(f"{height_map[row+1][col-1]} {height_map[row+1][col]} {height_map[row+1][col+1]}")
                    print()

                risk = 1 + int(height_map[row][col])
                valleys.append([row, col, risk])

    # PART 2
    coordinates = [[i, j] for i in range(len(height_map)) for j in range(len(height_map[0]))]
    remaining_coordinates = coordinates
    assigned_coordinates = []
    basins = []
    while len(assigned_coordinates) < len(height_map) * len(height_map[0]):
        basin = []

        # Find the first non-assigned coordinate which is not equal 9 as the basin starting point:
        _start = False 
        counter = 0
        while counter < len(remaining_coordinates) or not _start:
            row, col = remaining_coordinates[counter]
            if height_map[row][col] != '9':
                search_list = [[row, col]]
                _start = True
            counter += 1
        if VERBOSE:
            print(f'Starting search at ({row}, {col}) [counter: {counter - 1}]')

        # Generate and search through a list of eligible coordinates
        while len(search_list) > 0:
            for row, col in search_list:
                if height_map[row][col] != marker and height_map[row][col] != '9':
                    basin.append([row, col])
                    height_map[row][col] = marker
                    if VERBOSE:
                        print(f"basin: {basin}")
                        print(f"assigned coords: {assigned_coordinates}")
                        print(f"search list: {search_list}")
                    for direction in directions:
                        try:
                            if height_map[row + direction[0]][col + direction[1]] != '9' and (row + direction[0] >= 0 and col + direction[1] >= 0):
                                if [row + direction[0], col + direction[1]] not in assigned_coordinates:
                                    search_list.append([row + direction[0], col + direction[1]])
                        except IndexError:
                            pass
                else:
                    assigned_coordinates.append([row, col])

                search_list = search_list[1:]   # remove the searched coordinate

        # update remaining coordinates
        remaining_coordinates = list(set(map(tuple, coordinates)) - set(map(tuple, assigned_coordinates)))

        # Save the identified basin
        if basin:
            basins.append(basin)
            print(f"Basins detected: {len(basins)}. Remaining coordinates: {len(height_map) * len(height_map[0]) - len(assigned_coordinates)}", end='\r')
            if MAPPING:
                for row in height_map:
                    print(row)

    basin_sizes = [len(basin) for basin in basins]
    basin_sizes.sort()
    print(f"[Part 1] Valleys identified. Sum of risk levels: {sum([entry[-1] for entry in valleys])}")
    print(f"[Part 2]")
    print(f"Total amount of basins detected: {len(basins)}.")
    print(f"Sizes of the three largest:")
    print(f"   1. {basin_sizes[-1]}")
    print(f"   2. {basin_sizes[-2]}")
    print(f"   3. {basin_sizes[-3]}")
    print(f"Product of the three sizes: {basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]}")

if __name__ == '__main__':
    main()
    