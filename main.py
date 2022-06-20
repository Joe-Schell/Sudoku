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

# Function that prints the board
# @param: board - a 2D array example board
# @return: None (prints to console)
def print_board(board):
    for i in range(ROWS):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(COLS):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            # Check for last position
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


print_board(board1)

# Function that finds all empty cells in the Sudoku board
# @param: board - a 2D array example board
# @return: Empty cell or None
def find_empty(board):
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None