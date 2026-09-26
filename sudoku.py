# sudoku solver using backtracking algorithm
# board is a 9x9 grid with 9 boxes made up of 3x3 spaces

board = [
    [0,0,6,0,0,0,5,0,8],
    [1,0,2,3,8,0,0,0,4],
    [0,0,0,2,0,0,1,9,0],
    [0,0,0,0,6,3,0,4,5],
    [0,6,3,4,0,5,8,7,0],
    [5,4,0,9,2,0,0,0,0],
    [0,8,7,0,0,4,0,0,0],
    [2,0,0,0,9,8,4,0,7],
    [4,0,9,0,0,0,3,0,0]

]


# Function to print the board, one row per line
def print_board(board):
    for row in board:
        print(*row) # * is the unpacking operator, breaks down lists into individual elements so each list of list gets printed separated by a space

# Function to check if a number is valid in space
def is_valid(row, column, number, board):

    # Conditions to check if placing a number at (row, column) creates a PROMISING node.
    # A node is promising if the new number doesn't repeat in its row, column or 3x3 box
    # If the number repeats, the node is NOT PROMISING: the branch is pruned and we return False

    # row check
    for n in range(0, 9):
       if board[row][n] == number: # row is fixed, n moves across columns
           return False # NOT PROMISING: number already in row

    # column check
    for n in range (0, 9):
        if board[n][column] == number: # column is fixed, n moves down the rows
            return False # NOT PROMISING: number already in this column

    # 3x3 box check
        # row // 3 and column // 3 give the box's section (0, 1 or 2), * 3 turns each into the box's starting index
    start_row = (row // 3)* 3
    start_column = (column // 3)* 3

    # external loop -> increases row index
    # internal loop -> increases column index

    for r in range(0,3):
        for c in range(0,3):
            if board[start_row+r][start_column+c] == number:
                return False # NOT PROMISING: number already in this box

    # If it passed all the 3 checks the node IS PROMISING
    return True

# function that loops through the board to start solving it, it uses backtracking while exploring the node's children
def solve(board):

    # Returns True if the node leads to a solution
    # Returns false if every child ends up to be NOT PROMISING or a dead end

    for row in range(0,9):
        for column in range(0,9):

            # empty cell means the node IS NOT a solution yet, children must be explored
            if board[row][column] == 0: # 

                # loop for trying with every number from 1 to 9 (generating children)
                for number in range(1,10):

                    # if the child is PROMISING we keep exploring...
                    if is_valid(row, column, number, board):
                        board[row][column] = number # replacing with the valid number

                         # we call solve() with the updated board with the valid number
                        if solve(board): # if going deeper in the nodes succeeds
                            return True # a solution was found below, tell the caller to stop searching

                        # BACKTRACKING: child was promising but led to a dead end
                        # The board is shared, so we erase the number to restore the parent node and try the parent's next child
                        # if the child leads to a dead end, we return it to the parent and it gets pruned and we keep the parent
                        board[row][column] = 0 

                # if no child of the node was promising or led to a solution:
                return False # false if the loop tried everything but did not succeed, we go one level up
    
    # if no more empty cells left, the node is a leaf and a solution
    return True

print("Puzzle:")
print_board(board)

solve(board)

print("\nSolution:")
print_board(board)
                        

