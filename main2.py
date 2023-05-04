import random
from BFS_Sudoku import BFS_solve
from DFS_Sudoku import DFS_solve

def generate_sudoku(size, mode):
    if size == 6:
        rows, cols, box_rows, box_cols = 6, 6, 2, 3
    elif size == 9:
        rows, cols, box_rows, box_cols = 9, 9, 3, 3
    else:
        raise ValueError("Invalid size specified. Must be 6 or 9.")

    if mode not in ['easy', 'hard']:
        raise ValueError("Invalid mode specified. Must be 'easy' or 'hard'.")
    
    puzzle = [[0 for j in range(cols)] for i in range(rows)]

    def backtrack_solve():
        # define recursive helper function for backtracking
        def solve(row, col):
            if col == cols:
                col = 0
                row += 1
                if row == rows:
                    return True  # solution found
            if puzzle[row][col] != 0:
                return solve(row, col+1)
            for val in random.sample(range(1, size+1), size):
                if is_valid(puzzle, row, col, val, box_rows, box_cols):
                    puzzle[row][col] = val
                    if solve(row, col+1):
                        return True  # solution found
                    puzzle[row][col] = 0
            return False  # no solution found

        solve(0, 0)

    # generate solution using backtracking
    backtrack_solve()

    # remove some numbers to create the puzzle
    if mode == 'easy':
        cells_to_remove = size*size//4
    elif mode == 'hard':
        cells_to_remove = size*size//1.5
    
    num_removed = 0
    while num_removed < cells_to_remove:
        row = random.randint(0, rows-1)
        col = random.randint(0, cols-1)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            num_removed += 1

    return puzzle

def is_valid(puzzle, row, col, value, box_rows, box_cols):
    # check row and column
    for i in range(len(puzzle)):
        if puzzle[row][i] == value:
            return False
        if puzzle[i][col] == value:
            return False

    # check box
    box_row = (row // box_rows) * box_rows
    box_col = (col // box_cols) * box_cols
    for i in range(box_row, box_row + box_rows):
        for j in range(box_col, box_col + box_cols):
            if puzzle[i][j] == value:
                return False

    return True



puzzle = generate_sudoku(6, 'hard') # generates a 6x6 sudoku grid

print ("Problem:")
for row in puzzle:
      print (row)

BFS_solve(puzzle)
DFS_solve(puzzle)

print ("")
print ("------------------------------------------------------------")
print ("")

puzzle = generate_sudoku(9, 'easy') # generates a 9x9 sudoku grid

print ("Problem:")
for row in puzzle:
      print (row)

BFS_solve(puzzle)
DFS_solve(puzzle)