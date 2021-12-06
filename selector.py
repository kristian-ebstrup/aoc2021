#!usr/bin/env python
import sys

# take argvals from terminal
if len(sys.argv) < 3:
    print('Not enough arguments supplied. Please give (str) days and (str) parts (support multiple days and parts by separating with comma)')
else:
    input1 = sys.argv[1].split(',')
    input2 = sys.argv[2].split(',')

    print(f"Days selected: {input1}")
    print(f"Parts selected: {input2}")
    # function to select a day and part to run.
    print()
    for day in input1:
        print(f"#----- DAY {day} -----#")
        for part in input2:
            module_name = 'days.' + day + part
            print(f"... running \'\days\{day + part}.py\'")
            module = __import__(module_name)
            input('... Press Enter to continue ...')
            print()

