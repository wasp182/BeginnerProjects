import random
import re

class Board:
    def __init__(self,dim_size,num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        # keep track of square (tuple of r and c) that are filled
        self.dug = set()
        # create board
        self.board = self.make_new_board()
        self.assign_values()

        # create new board with given size and plant bombs
        # data structure used - 2D array or list of list
    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # plant bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs :
            loc = random.randint(0,self.dim_size**2-1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            if board[row][col] == "*":
                # bomb already planted , continue to move to new position
                continue
            board[row][col] = "*"
            bombs_planted += 1
        return board

    # need to know how many bombs are there around a spot
    def assign_values(self):
        # for each values on board assign a value to nob bomb squares = no of bombs around it
        # 0-8 for all possible spaces except for edges
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                # check if its a bomb itself , if yes then nothing to check
                if self.board[r][c] == "*":
                    continue
                # we can update the empty places with value if bombs
                self.board[r][c] = self.get_num_neighbour_bombs(r,c)

    # check neighbourhood of square for bombs , called in assign values
    def get_num_neighbour_bombs(self,row,col):
        num_neighbouring_bombs = 0
        for r in range(max(row-1,0),min(row+1,self.dim_size-1)+1):
            for c in range(max(0,col-1),min(col+1,self.dim_size-1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == "*":
                    num_neighbouring_bombs += 1
        return num_neighbouring_bombs

    # show board state to user
    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] =" "

        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )
        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep


    # modifies state of board - captures r,c where digging is done (non-bomb places)
    # and returns if a bomb is dug up or not
    def dig(self,row,col):
        # store where digging has been done - during recursion values dug are stored here
        self.dug.add((row,col))
        # check board if already dug else start recursion
        if self.board[row][col] == "*":
            return False
        # below when there are bombs around this square - don't dig anymore
        elif self.board[row][col] > 0:
            return True
        # below case when no bomb in neighbourhood i.e. board value = 0 - dig neighbours
        for r in range(max(0,row-1),min(row+1,self.dim_size-1)+1):
            for c in range(max(col-1,0),min(col+1,self.dim_size-1)+1):
                if (r, c) in self.dug:
                    continue
                self.dig(r,c)
        # return true so we can stop before getting to a bomb
        return True


def play(dim_size = 10 , num_bombs= 10):
    # create board and plant bombs
    board = Board(dim_size,num_bombs)
    # show the board to user and take input
    # if bomb then display game over
    # if not bomb , then display squares that are at least near one bomb
    # if only bombs remain then stop the game
    safe = True
    # this is because dig function returns true or false if no bomb or bomb is dug
    while len(board.dug) < board.dim_size**2 - num_bombs:
        print(board)
        # New function
        # allows to split the expression separated by comma and ignore the white space via (\\s)*
        user_input = re.split(',(\\s)*',input("where would you like to dig Input as row,col"))
        row , col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue
        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            break

    if safe:
        print("Winner")
    else:
        print("Game Over")
        board.dug = [(r,c) for r in range(dim_size) for c in range(dim_size)]
        print(board)


if __name__ == '__main__': # good practice :)
    play()




