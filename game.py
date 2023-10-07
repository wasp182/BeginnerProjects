import time

from  tick_tack_toe import HumanPlayer,RandomComputerPlayer , MinMaxPlayer

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| "+" |".join(row)+" |")


    @staticmethod
    def print_board_nums():
        # take rows and give indices of rows applicable
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| "+" |".join(row)+" |")


    def available_moves(self):
        # returns list of indices where move can be made
        moves = []
        for (i,spot) in enumerate(self.board):
            if spot == " ":
                moves.append(i)
        return moves
        # list comprehension verion
        # return [i for (i,spot) in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board
        # returns true if there is any empty space in board left

    def num_empty_spaces(self):
        return len(self.available_moves())

    def make_move(self,spot,sign):
        # Update the board if move is valid , return move as valid or invalid
        if self.board[spot] == " ":
            self.board[spot] = sign
            # Check here if there is a winner now , since input is valid
            if self.winner(spot,sign):
                self.current_winner = sign
            return True
        return False

    def winner(self,spot,sign):
        # check if all three in row , diagonal
        # check row of given spot
        row_ind = spot // 3
        row_check = self.board[row_ind*3:(row_ind+1)*3]
        if all([square==sign for square in row_check]):
            return True
        # Check column
        col_ind = spot % 3
        col_check = [self.board[i*3+col_ind] for i in range(3)]
        if all([square==sign for square in col_check]):
            return True
        # Check diagonal ,which only applicable when spot is even no
        if spot % 2 == 0:
            diagonal_check_1 = [self.board[i] for i in [0,4,8]]
            if all([square == sign for square in diagonal_check_1]):
                return True
            diagonal_check_2 = [self.board[i] for i in [2,4,6]]
            if all([square == sign for square in diagonal_check_2]):
                return True
        #if no check completed , return false
        return False


def play(game,x_player,O_player,printGame = True):
    sign = "X"
    if printGame:
        game.print_board_nums()

    while game.empty_squares():
        # while there is an empty space , get the input from player
        if sign == "O":
            spot = O_player.get_move(game)
        else:
            spot = x_player.get_move(game)

        # update the board if move is valid , return move as valid or invalid
        if game.make_move(spot,sign):
            if printGame:
                print(sign + f' makes move to {spot}')
                game.print_board()
                print(" ")
        # Need to check if there is any current winner and print it
            if game.current_winner:
                if printGame:
                    print(sign + " Wins!")
                return sign

        # Update player turn
            sign = "X" if sign == "O" else "O"
        if printGame:
            time.sleep(0.8)

    if printGame:
        print("It\'s a tie :(")


if __name__ == "__main__":
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1000):
        x_player = RandomComputerPlayer("X")
        o_player = MinMaxPlayer("O")
        game1 = TicTacToe()
        result = play(game1,x_player,o_player,printGame=False)
        if result == "x":
            x_wins += 1
        elif result == "o":
            o_wins += 1
        else:
            ties += 1
    print(f"X wins {x_wins} , O wins {o_wins} with {ties} ties" )