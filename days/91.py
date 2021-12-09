#!usr/bin/env python

filename = './inputs/day9.txt'
VERBOSE = False

height_map = []
with open(filename) as f:
    for line in f.readlines():
        height_map.append(line[:-1])        # [:-1] removes the line-break character

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

print(f"Valleys identified. Sum of risk levels: {sum([entry[-1] for entry in valleys])}")