"""
This module is used to follow the steps of the lesson walkthrough to create
the tic-tac-toe game.
"""
from random import randint  # import used in the choose_first function

# List used as a representation of the game board
test_board = [None, "1", "2", "3", "4", "5", "6", "7", "8", "9"]


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


def player_input():
    """
    Function that takes in a player input and assign their marker as 'X' or 'O'
    """
    player2_choice = ""
    """Register the players choice of playing as  X or O """
    player1_choice = input("Player 1, please enter a marker X or O: ")
    player1_choice = player1_choice.upper()
    while player1_choice != 'X' and player1_choice != 'O':
        player1_choice = input("Sorry, wrong input. Please enter a marker X or O: ")
        player1_choice = player1_choice.upper()
    if player1_choice == 'X':
        player2_choice = 'O'
    elif player1_choice == 'O':
        player2_choice = 'X'
    return player1_choice, player2_choice


def display_marker_choice(p1_choice, p2_choice):
    """
    Function that displays the marker choice of each player
    """
    print("Player 1 will be playing as: " + p1_choice)
    print("Player 2 will be playing as: " + p2_choice)


def place_marker(board, marker, position):
    """
    Function that takes in the board list object, a marker ('X' or 'O'),
    and a desired position (number 1-9) and assigns it to the board.
    """
    board[position] = marker


def win_check(board, mark):
    """
    function that takes in a board and a mark (X or O) and
    then checks to see if that mark has won.
    """

    # This is the course solution code. Not mine
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first(ply1, ply2):
    """
    function that uses the random module to randomly
    decide which player goes first.
    """
    get_first = randint(1, 2)
    if get_first == 1:
        print(ply1 + " will be going first")
    elif get_first == 2:
        print(ply2 + " will be going first")


def space_check(board, position):
    """
    function that returns a boolean indicating
    whether a space on the board is freely available.
    """
    return board[position] != 'X' and board[position] != 'O'


def full_board_check(board):
    """
    function that checks if the board is full and returns
    a boolean value. True if full, False otherwise
    """
    new_list = list()
    for index, letter in enumerate(board[1:10]):
        if letter == 'X' or letter == 'O':
            new_list.append(1)
        else:
            new_list.append(0)
    return all(new_list)


print('\n' * 5)
