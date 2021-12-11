#!/usr/bin/env python
def main():
    filename = './inputs/day8.txt'

    segments = {'a' : 'a',
                'b' : 'b',
                'c' : 'c',
                'd' : 'd',
                'e' : 'e',
                'f' : 'f',
                'g' : 'g'}

    display = {'abcefg' : '0',
            'cf' : '1',
            'acdeg' : '2',
            'acdfg' : '3',
            'bcdf' : '4',
            'abdfg' : '5',
            'abdefg' : '6',
            'acf' : '7',
            'abcdefg' : '8',
            'abcdfg' : '9'}

    unprocessed_signals = []
    with open(filename) as f:
        for line in f.readlines():
            unprocessed_signals.append(line.split('|'))

    print('Extracting and deciphering output values')
    output_values = []
    digit_counter = 0
    for signal in unprocessed_signals:
        signal_patterns = signal[0].split()
        output_signal = signal[1].split()   # [0]: signal patterns, [1]: output value

        # Extract unique displays
        unique_displays = []
        while len(unique_displays) < 10:
            for pattern in signal_patterns:
                if pattern not in unique_displays:
                    unique_displays.append(pattern)

        # Sort the unique displays by length, and each entry alphabetically
        unique_displays = [sorted(entry) for entry in sorted(unique_displays, key=len)]     # [1, 7, 4, (2, 3, 5), (0, 6, 9), 8]

        # Determine cipher from unique displays
        remaining_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

        # Get 'a' from checking 1 against 7
        remainder = list(set(unique_displays[1]) - set(unique_displays[0]))[0]
        remaining_letters = list(set(remaining_letters) - set(remainder))
        segments['a'] = remainder

        # Check 6-segmented numbers (0, 6, 9) against 8
        for i in [6, 7, 8]:
            remainder = list(set(unique_displays[-1]) - set(unique_displays[i]))[0]
            if remainder in unique_displays[0]:
                segments['c'] = [char for char in unique_displays[0] if char == remainder][0]
                remaining_letters = list(set(remaining_letters) - set([char for char in unique_displays[0] if char == remainder][0]))
                segments['f'] = [char for char in unique_displays[0] if char != remainder][0]
                remaining_letters = list(set(remaining_letters) - set([char for char in unique_displays[0] if char != remainder][0]))
            elif remainder in unique_displays[2]:
                segments['d'] = remainder
                remaining_letters = list(set(remaining_letters) - set(remainder))
            else:
                segments['e'] = remainder[0]
                remaining_letters = list(set(remaining_letters) - set(remainder))

        # Check 5-segmented numbers (2, 3, 5) against 8
        for i in [3, 4, 5]:
            remainder = list(set(unique_displays[-1]) - set(unique_displays[i]))
            for num in remainder:
                if num in remaining_letters:
                    segments['b'] = num
                    remaining_letters = list(set(remaining_letters) - set(num))
        
        # Last letter (g) can be surmised from the rest:
        segments['g'] = remaining_letters[0]

        # Obtain deciphered output values
        output = []
        for encoded_output in output_signal:
            if len(encoded_output) in [2, 3, 4, 7]:
                digit_counter += 1

            decoded_output = ''
            for char in encoded_output:
                for key, value in segments.items():
                    if char == value:
                        decoded_output += key

            # Sort the segments alphabetically, and check in display dictionary
            decoded_output = "".join(sorted(decoded_output))
            output.append(display[decoded_output])
        
        # Add final 4-digit output to collective list
        output_values.append(int("".join(output)))

    print(f"[Part 1] Amount of times 1, 4, 7, or 8 appears in the output values: {digit_counter}")
    print(f"[Part 2] Total sum of the output values: {sum(output_values)}")

if __name__ == '__main__':
    main()


