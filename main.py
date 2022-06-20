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

# Function that checks if a sudoku board is valid
# @param: board - a 2D array example board
# @return: True or False
def valid(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(len(board)):
        for c in range(len(board[0])):
            # Empty space is found, continue to next iteration
            if board[r][c] == 0:
                continue

            # If number in the board is already in the row / col / square, return False
            if (board[r][c] in rows[r] or board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                return False

            # Update hashsets
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True



# Function that solves a sudoku board
# @param: board - a 2D array example board
# @return:
#def solve(board):




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
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Function that finds empty cell in the Sudoku board
# @param: board - a 2D array example board
# @return: Empty cell or None
def find_empty(board):
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board1)
var = valid(board1)
print(var)