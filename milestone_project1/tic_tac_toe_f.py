"""
This module is used to follow the steps of the lesson walk through to create
the tic-tac-toe game. This is the final module for the course challenge
"""
from random import randint  # import used in the choose_first function

# List used as a representation of the game board
legacy_board = ['#', '7', '8', '9', '4', '5', '6', '1', '2', '3']
game_board = ['#', '7', '8', '9', '4', '5', '6', '1', '2', '3']


class Player:
    def __init__(self, player_id, name, marker):
        self.player_id = player_id
        self.name = name
        self.marker = marker

    def display_marker_choice(self):
        """
        Function that displays the marker choice of each player
        """
        print(self.player_id + " will be playing as " + self.marker)

    def place_marker(self, board, marker, value):
        """
        Function that takes in the board list object, a marker ('X' or 'O'),
        and a desired position (number 1-9) and assigns it to the board.
        """
        for index, item in enumerate(board):
            if item == str(value):
                board[index] = marker

    def win_check(self, board, mark):
        """
        function that takes in a board and a mark (X or O) and
        then checks to see if that mark has won.
        """

        # This is the instructor's solution code for the win_check function.
        return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
                (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
                (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
                (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
                (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
                (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
                (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
                (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

    def space_check(self, board, position):
        """
        function that returns a boolean indicating
        whether a space on the board is freely available.
        """
        return board[position] != 'X' and board[position] != 'O'

    def player_choice(self, board):
        """
        Function that asks for a player's
        next position (as a number 1-9) and then uses the function space_check
        to check if it's a free position.
        """
        next_position = int(input("Enter a position(1-9): "))
        is_free = self.space_check(board, next_position)
        if not is_free:
            return "Tha position on the game board is not free"
        else:
            return next_position


# Implementation of the game
print('Welcome to Tic Tac Toe')
game_setup = False
player_one = Player("Player 1", 'Mike', '')
player_two = Player("Player 2", 'Mike', '')


def choose_first(ply1, ply2):
    """
    function that uses the random module to randomly
    decide which player goes first.
    """
    get_first = randint(1, 2)
    if get_first == 1:
        print("Player 1 will be going first: ")
        return ply1
    elif get_first == 2:
        print("Player 2 will be going first: ")
        return ply2


def player_input():
    """
     Function that takes in a player input and assign their marker as 'X' or 'O'
    """
    player_1 = None
    player_2 = None
    accepted = ['X', 'O']
    print("Players, please choose your markers X or O")
    while player_1 not in accepted:
        player_1 = input("Player 1 first: ")
    print("Player 1 has chosen " + player_1)
    while player_2 not in accepted:
        player_2 = input("Player 2, please choose the opposite of player 1: ")
    print("Player 2 has chosen " + player_2)
    return player_1, player_2


def full_board_check(board):
    """
    function that checks if the board is full and returns
    a boolean value. True if full, False otherwise
    """
    new_list = list()
    for index, letter in enumerate(board[1:10]):
        if letter == 'X':
            new_list.append(1)
        elif letter == 'O':
            new_list.append(1)
        else:
            new_list.append(0)
    return all(new_list)


def full_board_check_2(board):
    check_val = []
    for letter in board[1:10]:
        if letter == 'X' or letter == 'O':
            check_val.append(1)
        else:
            check_val.append(0)
    return all(check_val)


def display_board(game_table):
    """
    function that can print out a board. Sets up the board as a list,
    where each index 1-9 corresponds with a number on
    a number pad, so there is  a 3 by 3 board representation.
    """
    print(game_table[1] + "|" + game_table[2] + '|' + game_table[3])
    print("-|-|-")
    print(game_table[4] + "|" + game_table[5] + '|' + game_table[6])
    print("-|-|-")
    print(game_table[7] + "|" + game_table[8] + '|' + game_table[9])


def replay():
    """Function docstring"""
    choice = "Wrong"

    while choice not in ['Y', 'N']:
        choice = input("Do you want to replay [Y or N]: ")
        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand. Please choose Y or N")
    if choice == 'Y':
        return True
    else:
        print("Game Over")
        return False


# Game set-up
while not game_setup:
    player_one.marker, player_two.marker = player_input()
    player_one.display_marker_choice()
    player_two.display_marker_choice()
    game_setup = True
turn = choose_first(player_one, player_two)
display_board(game_board)

# Implementation
game_on = True
board_full = full_board_check_2(game_board)
while not game_on:
    game_on = replay()
while game_on:
    if turn == player_one:
        if player_two.win_check(game_board, player_two.marker) or player_one.win_check(game_board, player_one.marker):
            print(player_two.player_id + " has won the game")
            if replay():
                game_board.clear()
                game_board = legacy_board.copy()
                player_one.marker, player_two.marker = player_input()
                player_one.display_marker_choice()
                player_two.display_marker_choice()
                display_board(game_board)
                turn = choose_first(player_one, player_two)
            else:
                break
        elif full_board_check_2(game_board):
            if replay():
                game_board.clear()
                game_board = legacy_board.copy()
                player_one.marker, player_two.marker = player_input()
                player_one.display_marker_choice()
                player_two.display_marker_choice()
                display_board(game_board)
                turn = choose_first(player_one, player_two)
            else:
                break
        else:
            get_pos = int(input(player_one.player_id + " enter position: "))
            player_one.place_marker(game_board, player_one.marker, get_pos)
            display_board(game_board)
            turn = player_two
    elif turn == player_two:
        if player_two.win_check(game_board, player_two.marker) or player_one.win_check(game_board, player_one.marker):
            print(player_one.player_id + " has won the game.")
            if replay():
                game_board.clear()
                game_board = legacy_board.copy()
                player_one.marker, player_two.marker = player_input()
                player_one.display_marker_choice()
                player_two.display_marker_choice()
                display_board(game_board)
                turn = choose_first(player_one, player_two)
            else:
                break
        elif full_board_check_2(game_board):
            if replay():
                game_board.clear()
                game_board = legacy_board.copy()
                player_one.marker, player_two.marker = player_input()
                player_one.display_marker_choice()
                player_two.display_marker_choice()
                display_board(game_board)
                turn = choose_first(player_one, player_two)
            else:
                break
        else:
            get_pos = int(input(player_two.player_id + " enter position: "))
            player_two.place_marker(game_board, player_two.marker, get_pos)
            display_board(game_board)
            turn = player_one
