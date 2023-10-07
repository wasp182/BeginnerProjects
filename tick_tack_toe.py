import random
import math

class Player:
    def __init__(self, sign):
        # signature is x or o
        self.sign = sign

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, sign):
        super().__init__(sign)

    def get_move(self, game):
        # takes random spot / index from available moves (0-9) value where available
        spot = random.choice(game.available_moves())
        return spot


class HumanPlayer(Player):
    def __init__(self, sign):
        super().__init__(sign)

    def get_move(self, game):
        valid_spot = False
        spot_value = None
        while not valid_spot:
            user_value = input(self.sign + '\'s "enter a spot value from (0-9)')
            # check if that board spot value is available to user or valid
            try:
                spot_value = int(user_value)
                if spot_value not in game.available_moves():
                    raise ValueError
                valid_spot = True
            except ValueError:
                print("Invalid square. Try again")

        return spot_value

class MinMaxPlayer(Player):
    def __init__(self,sign):
        # How to initialize super class
        super().__init__(sign)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            spot = random.choice(game.available_moves())
        else:
            # get the minimax algorithm to return move
            spot = self.minimax(game,self.sign)['position']
        return spot

    def minimax(self,game_state,player):
        # maximize the utility of max_player with given sign
        # Find the possible states of move and apply them to max_player
        # returns optimal position and score
        max_player = self.sign
        other_player = "0" if max_player == "X" else "X"

        # return if previous case was a winner - base case
        if game_state.current_winner == other_player :
            return {'position' : None,
                    'score': 1*(game_state.num_empty_spaces()+1) if other_player == max_player else
                    -1*(game_state.num_empty_spaces()+1)
                    }
        elif not game_state.empty_squares():
            return {'position': None, 'score':0}

        # actual algorithm
        if player == max_player:
            # save the best position to move and the corresponding utility
            # initialization to compare the utility of upcoming move score
            best = {'position': None , 'score': -math.inf}
        else:
            best = {'position': None , 'score': math.inf} #initilizaize for minimizer player

        for possible_moves in game_state.available_moves():
            # try each spot
            game_state.make_move(possible_moves,player)
            # try the move recursively in minimax function and get score
            sim_score = self.minimax(game_state,other_player)
            # undo the move
            game_state.board[possible_moves] = " "
            game_state.current_winner = None
            sim_score['position'] = possible_moves # store the position undertaken - its value is already stored after recursion but position isn't recursed

            # update the dictionary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
                    # Max function : store max value
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
                    # Min function : storing min for min player
        return best











