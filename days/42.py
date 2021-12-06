#!/usr/bin/env python
filename = "./inputs/day4.txt"

def check_numbers_expanded(bingo_numbers, boards, marker = 'XX'):
    
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
                    print("Final board state: \n")
                    for _board in boards:
                        for _row in _board:
                            print(" ".join(_row))
                        print("\n")

                    print(f"Winner: Board {k} with last called number {num}.")
                    board_score = 0
                    for row in boards[k]:
                        print(" ".join(row))
                        for col in row:
                            if col != marker:
                               board_score += int(col)

                    board_score = board_score * int(num)
                    return [called_numbers, k, j, board_score, n]

                # check column for bingo
                for r_count in r_hits:
                    if r_count == len(board):
                        print("Final board state: \n")
                        for _board in boards:
                            for _row in _board:
                                print(" ".join(_row))
                            print("\n")

                        print(f"Winner: Board {k} with last called number {num}.")
                        board_score = 0
                        for row in boards[k]:
                            print(" ".join(row))
                            for col in row:
                                if col != marker:
                                    board_score += int(col)

                        board_score = board_score * int(num)
                        return [called_numbers, k, j, board_score, n]
        
    return "No winners."

_board = []
boards = []
with open(filename) as f:
    for line in f.readlines():
        if line == "\n":
            if _board:
                boards.append(_board)
                _board = []
        else:
            if not boards:
                line = line.split(',')
            else:
                line = line.split()
            _board.append(line)

bingo_nums = boards[0][0]
boards = boards[1:]

marker = 'XX'
while len(boards) > 0:
    winner = check_numbers_expanded(bingo_nums, boards, marker)
    boards = [boards[i] for i, board in enumerate(boards) if i != winner[1]]
    bingo_nums = bingo_nums[winner[4]-1:]
    print(f"Amount of boards left: {len(boards)}")

print(f"Final score: {winner[3]}")

