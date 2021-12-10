#!/usr/bin/env python
def main():
    import sys
    from importlib import import_module

    # take argvals from terminal
    if len(sys.argv) < 2:
        print('No arguments supplied. Please input days to select, separated by comma')
    else:
        input1 = sys.argv[1].split(',')

        print(f"Days selected: {input1}")

        # function to select a day and part to run.
        print()
        for day in input1:
            print(f"#--------------- DAY {day} ---------------#")
            module_name = 'days.day' + day
            print(f"running \'\days\day{day}.py\' ...")
            module = import_module(module_name)
            module.main()
            input('... Press Enter to continue ...')
            print()

if __name__ == '__main__':
    main()
