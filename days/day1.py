#!/usr/bin/env python
def main():
    filename = "./inputs/day1.txt"

    count = 0
    line_count = 0
    previous_line = 0
    measurements = []
    with open(filename) as f:
        for line in f.readlines():
            # Part 1
            line = int(line)
            if previous_line < line and line_count > 0:
                count += 1
            previous_line = line
            line_count += 1

            # Part 2
            measurements.append(int(line))

    print(f"[Part 1] {count} increases out of {line_count} entries")

    count = sum([1 for i in range(len(measurements)) if sum(measurements[i+1:i+4]) > sum(measurements[i:i+3])])
    print(f"[Part 2] {count} increases out of {len(measurements)} entries")

if __name__ == '__main__':
    main()