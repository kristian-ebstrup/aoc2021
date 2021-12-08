#!usr/bin/env python
filename = './inputs/day8.txt'

unprocessed_signals = []
with open(filename) as f:
    for line in f.readlines():
        unprocessed_signals.append(line.split('|'))

digit_counter = 0
for signal in unprocessed_signals:
    output_signal = signal[1].split()   # [0]: signal patterns, [1]: output value

    # Collectively count 1, 4, 7, and 8 in output values
    for digit in output_signal:
        if len(digit) in [2, 3, 4, 7]:
            digit_counter += 1

print(f"Amount of times 1, 4, 7, or 8 appears in the output values: {digit_counter}")


