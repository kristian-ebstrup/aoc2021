#!/usr/bin/env python
def main():
    filename = "./inputs/day5.txt"

    thermal_ranges = []
    with open(filename) as f:
        for line in f.readlines():
            # input syntax is "x1,y1 -> x2,y2"
            line = line.split()
            line = [element.split(',') for element in line if element != '->']
            thermal_ranges.append(line)

    # PART 1
    # sort the horizontal and vertical thermal lines into its own list
    straight_thermal_ranges = [element for element in thermal_ranges if (element[0][0] == element[1][0] or element[0][1] == element[1][1])]

    # use a dictionary to track intersections
    thermal_map = {}
    for element in straight_thermal_ranges:
        if element[0][0] == element[1][0]:
            x_range = [int(element[0][0])]
            sorted_y = sorted([int(element[0][1]), int(element[1][1])])
            y_range = range(sorted_y[0], sorted_y[1] + 1)
        elif element[0][1] == element[1][1]:
            y_range = [int(element[0][1])]
            sorted_x = sorted([int(element[0][0]), int(element[1][0])])
            x_range = range(sorted_x[0], sorted_x[1] + 1)
        for i in x_range:
            for j in y_range:
                if ", ".join([str(i), str(j)]) in thermal_map:
                    thermal_map[", ".join([str(i), str(j)])] += 1
                else:
                    thermal_map[", ".join([str(i), str(j)])] = 1

    n_intersections = sum([ 1 for key in thermal_map if thermal_map.get(key, 0) > 1] )
    print(f"[Part 1] Detected thermal intersections (straight lines): {n_intersections}")

    # PART 2
    # use a dictionary to track intersections
    thermal_map = {}
    for element in thermal_ranges:
        # Boolean to control the mapping loop
        diagonal_line = False

        # straight lines
        if element[0][0] == element[1][0]:
            x_range = [int(element[0][0])]
            sorted_y = sorted([int(element[0][1]), int(element[1][1])])
            y_range = range(sorted_y[0], sorted_y[1] + 1)
        elif element[0][1] == element[1][1]:
            y_range = [int(element[0][1])]
            sorted_x = sorted([int(element[0][0]), int(element[1][0])])
            x_range = range(sorted_x[0], sorted_x[1] + 1)
        # diagonal lines
        else:
            diagonal_line = True
            if int(element[0][0]) > int(element[1][0]):
                x_range = [i for i in range(int(element[1][0]), int(element[0][0]) + 1)]
                x_range.reverse()
            else:
                x_range = [i for i in range(int(element[0][0]), int(element[1][0]) + 1)]

            if int(element[0][1]) > int(element[1][1]):
                y_range = [i for i in range(int(element[1][1]), int(element[0][1]) + 1)]
                y_range.reverse()
            else:
                y_range = [i for i in range(int(element[0][1]), int(element[1][1]) + 1)]

            

        if diagonal_line == False:
            for i in x_range:
                for j in y_range:
                    if ", ".join([str(i), str(j)]) in thermal_map:
                        thermal_map[", ".join([str(i), str(j)])] += 1
                    else:
                        thermal_map[", ".join([str(i), str(j)])] = 1
        else:
            for index, _i in enumerate(x_range):
                if ", ".join([str(x_range[index]), str(y_range[index])]) in thermal_map:
                    thermal_map[", ".join([str(x_range[index]), str(y_range[index])])] += 1
                else:
                    thermal_map[", ".join([str(x_range[index]), str(y_range[index])])] = 1
                


    n_intersections = sum([ 1 for key in thermal_map if thermal_map.get(key, 0) > 1] )
    print(f"[Part 2] Detected thermal intersections (incl. diagonals): {n_intersections}")

if __name__ == '__main__':
    main()