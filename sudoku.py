from pprint import pprint

def next_empty_cell(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col
    return None, None


def is_valid(puzzle,guess,row,col):
    # Check if guess is repeated in row
    if guess in puzzle[row]:
        return False

    # check in column
    if guess in [puzzle[i][col] for i in range(9)]:
        return False

    # check in square box
    row_idx = (row//3)*3
    col_idx = (col//3)*3
    for r in range(row_idx,row_idx+3):
        for c in range(col_idx,col_idx+3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    # Data structure is a list of list with size 9*9
    # Step 1 : get a row , column to input guess
    # In case of no empty cell , evaluate the result
    row, col = next_empty_cell(puzzle)
    if row is None:
        return True

    # Step 2: Make a guess in row , col and check its validity
    for guess in range(1,10):
        # step 2.1 : in case of valid , put the guess
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col] = guess
            # print()
            # pprint(puzzle)
            # recurse the puzzle back once valid input done
            if solve_sudoku(puzzle):
                # print("recursion")
                return True
    # step 2.2 : in case of no valid guess in cell , update it to -1

        puzzle[row][col] = -1

    return False


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)


