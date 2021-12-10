#!/usr/bin/env python
def check_numbers(bingo_numbers, boards, marker = 'XX', VERBOSE = False):
    
    called_numbers = []
    # mark called numbers
    for num in bingo_numbers:
        called_numbers.append(num) 

        for k, board in enumerate(boards):
            r_hits = [0 for col in range(len(board[0]))]
            
            for i, row in enumerate(board):
                c_hits = 0

                # mark using marker (default 'XX')
                for j, col in enumerate(row):
                    if col == num:
                        boards[k][i][j] = marker
                    if boards[k][i][j] == marker:
                        c_hits += 1
                        r_hits[j] += 1
                
                # check row for bingo
                if c_hits == len(row):
                    if VERBOSE: print("Final board state: \n")
                    for _board in boards:
                        for _row in _board:
                            if VERBOSE: print(" ".join(_row))
                        if VERBOSE: print("\n")
                    return [called_numbers, k, i]

                # check column for bingo
                for r_count in r_hits:
                    if r_count == len(board):
                        if VERBOSE: print("Final board state: \n")
                        for _board in boards:
                            for _row in _board:
                                if VERBOSE: print(" ".join(_row))
                            if VERBOSE: print("\n")
                        return [called_numbers, k, j]
        
    return "No winners."

def check_numbers_expanded(bingo_numbers, boards, marker = 'XX', VERBOSE = False):
    
    called_numbers = []
    # mark called numbers
    for n, num in enumerate(bingo_numbers):
        called_numbers.append(num) 

        for k, board in enumerate(boards):
            r_hits = [0 for col in range(len(board[0]))]
            
            for i, row in enumerate(board):
                c_hits = 0

                # mark using marker (default 'XX')
                for j, col in enumerate(row):
                    if col == num:
                        boards[k][i][j] = marker
                    if boards[k][i][j] == marker:
                        c_hits += 1
                        r_hits[j] += 1
                
                # check row for bingo
                if c_hits == len(row):
                    if VERBOSE: print("Final board state: \n")
                    for _board in boards:
                        for _row in _board:
                            if VERBOSE: print(" ".join(_row))
                        if VERBOSE: print("\n")

                    if VERBOSE: print(f"Winner: Board {k} with last called number {num}.")
                    board_score = 0
                    for row in boards[k]:
                        if VERBOSE: print(" ".join(row))
                        for col in row:
                            if col != marker:
                               board_score += int(col)

                    board_score = board_score * int(num)
                    return [called_numbers, k, j, board_score, n]

                # check column for bingo
                for r_count in r_hits:
                    if r_count == len(board):
                        if VERBOSE: print("Final board state: \n")
                        for _board in boards:
                            for _row in _board:
                                if VERBOSE: print(" ".join(_row))
                            if VERBOSE: print("\n")

                        if VERBOSE: print(f"Winner: Board {k} with last called number {num}.")
                        board_score = 0
                        for row in boards[k]:
                            if VERBOSE: print(" ".join(row))
                            for col in row:
                                if col != marker:
                                    board_score += int(col)

                        board_score = board_score * int(num)
                        return [called_numbers, k, j, board_score, n]
        
    return "No winners."

def main():
    filename = "./inputs/day4.txt"

    # Part 1
    board = []
    boards = []
    with open(filename) as f:
        for line in f.readlines():
            if line == "\n":
                if board:
                    boards.append(board)
                    board = []
            else:
                if not boards:
                    line = line.split(',')
                else:
                    line = line.split()
                board.append(line)

    bingo_nums = boards[0][0]
    boards = boards[1:]

    marker = 'XX'
    winner = check_numbers(bingo_nums, boards, marker)
    #print(f"Winner: Board {winner[1]} with last called number {winner[0][-1]}.")
    board_score = 0
    for row in boards[winner[1]]:
        #print(" ".join(row))
        for col in row:
            if col != marker:
                board_score += int(col)

    print(f"[Part 1] Final score: {board_score * int(winner[0][-1])}")

    # Part 2
    board = []
    boards = []
    with open(filename) as f:
        for line in f.readlines():
            if line == "\n":
                if board:
                    boards.append(board)
                    board = []
            else:
                if not boards:
                    line = line.split(',')
                else:
                    line = line.split()
                board.append(line)

    bingo_nums = boards[0][0]
    boards = boards[1:]

    marker = 'XX'
    while len(boards) > 0:
        winner = check_numbers_expanded(bingo_nums, boards, marker)
        boards = [boards[i] for i, board in enumerate(boards) if i != winner[1]]
        bingo_nums = bingo_nums[winner[4]-1:]
        #print(f"Amount of boards left: {len(boards)}")

    print(f"[Part 2] Final score: {winner[3]}")

if __name__ == '__main__':
    main()

