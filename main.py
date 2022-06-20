import collections

board1 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

ROWS, COLS = len(board1), len(board1[0])


# Function that solves a sudoku board
def solve(board):
    find = find_empty(board)
    # Base Case: We found no empty cells remaining
    if not find:
        return True
    # Else, we return the empty cell and store in Find
    else:
        row, col = find
    # Loop from 1 - 9 since this is the set of valid numbers in a board
    for i in range(1, 10):
        # Check for a valid cell in the board
        if valid(board, row, col, i):
            # If valid, add i to the board
            board[row][col] = i
            # Recursively call solve on the board
            # and return True as long as the function returns True
            if solve(board):
                return True
            # Backtrack by setting the cell back to 0 (empty)
            board[row][col] = 0
    # If we get here, we cannot solve the board and must return False
    return False


# Function that checks if a sudoku board cell is valid
def valid(board, row, col, num):
    not_in_row = num not in board[row]
    not_in_col = num not in [board[i][col] for i in range(9)]
    not_in_box = num not in [board[i][j] for i in range(row//3*3, row//3*3+3)
                             for j in range(col//3*3, col//3*3+3)]
    return not_in_row and not_in_col and not_in_box


# Function that prints the board
def print_board(board):
    for i in range(ROWS):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(COLS):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Function that finds empty cell in the Sudoku board
def find_empty(board):
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board1)
print("solving....")
solve(board1)
print_board(board1)