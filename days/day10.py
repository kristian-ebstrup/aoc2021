#!/usr/bin/env python

def main():
    from math import trunc

    filename = './inputs/day10.txt'

    # pair dictionary
    pair_dict = {
        ']': '[',
        ')': '(',
        '}': '{',
        '>': '<',
    }

    value_dict = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

    first_illegal = []
    auto_completed = []
    with open(filename) as f:
        for line in f.readlines():
            state_tracker = []      # tracks open pairs
            illegal_tracker = []    # tracks illegal chars
            
            for i, char in enumerate(line):
                if char in '[({<':
                    state_tracker.append([char, i])
                if char in '])}>':
                    if state_tracker[-1][0] != pair_dict[char]:
                        illegal_tracker.append([char, i])
                        state_tracker = state_tracker[:-1]
                    else:
                        state_tracker = state_tracker[:-1]
            
            # illegal -> corrupted line, else incomplete
            if illegal_tracker:
                first_illegal.append(illegal_tracker[0][0])
            else:
                score = 0
                state_tracker.reverse()
                for entry in state_tracker:
                    score *= 5
                    score += value_dict[entry[0]]
                auto_completed.append(score)
                    
    print(f"[Part 1] Total syntax error score:    {sum([value_dict[char] for entry in first_illegal for char in entry])}")
    auto_completed.sort()
    print(f"[Part 2] Total auto-complete score:   {auto_completed[trunc(len(auto_completed)/2)]}")


    

if __name__ == '__main__':
    main()