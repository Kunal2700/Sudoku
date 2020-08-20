import random

yes = set(['yes', 'yeah', 'y', 'yuh', 'yeh', 'ye', 'yez', 'yep', 'yessir', 'yup', 'ya', 'yee'])

def solve(bo):
    pos = find_empty(bo)

    # base case (last pos correct)
    if not pos:
        return True

    for num in range(1, len(bo) + 1):
        if is_valid(bo, num, pos):
            bo[pos[0]][pos[1]] = num
            if solve(bo):
                return True
            bo[pos[0]][pos[1]] = 0
    return False

def is_valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_num = (pos[0] // 3, pos[1] // 3)
    for i in range(box_num[0] * 3, box_num[0] * 3 + 3):
        for j in range(box_num[1] * 3, box_num[1] * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def print_board(board):
    for r in range(len(board)):
        if r % 3 == 0 and r != 0:
            print(' - - - - - - - - - - - ')
        for c in range(len(board[0])):
            if c % 3 == 0 and c != 0:
                print(' |', end='')
            if c == 8:
                print(' ' + str(board[r][c]))
            else:
                print(' ' + str(board[r][c]), end='')

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

# Makes a solvable board
def make_board(m=3):
    """Return a random filled m**2 x m**2 Sudoku board."""
    n = m**2
    board = [[None for _ in range(n)] for _ in range(n)]

    def search(c=0):
        "Recursively search for a solution starting at position c."
        i, j = divmod(c, n)
        i0, j0 = i - i % m, j - j % m # Origin of mxm block
        numbers = list(range(1, n + 1))
        random.shuffle(numbers)
        for x in numbers:
            if (x not in board[i]                     # row
                and all(row[j] != x for row in board) # column
                and all(x not in row[j0:j0+m]         # block
                        for row in board[i0:i])):
                board[i][j] = x
                if c + 1 >= n**2 or search(c + 1):
                    return board
        else:
            # No number is valid in this cell: backtrack and try again.
            board[i][j] = None
            return None

    return search()

# Removes some slots to create puzzle
def createPuzzle(board):
    side = 9
    squares = side * side
    empties = squares * 3 // 4
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0

# main
board = make_board()
createPuzzle(board)

print_board(board)

answer = input('\nReady to solve? (y/n)\n')
if answer[0].lower() in yes:
    solve(board)
    print('\nHere is the solution:')
    print_board(board)

print('Have a nice day!')
