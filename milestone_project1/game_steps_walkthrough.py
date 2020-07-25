"""
This module is used to follow the steps of the lesson walkthrough for the tic-tac-toe assignment
"""

the_table = [None, "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def print_game_table(game_table):
    print(game_table[1] + "|" + game_table[2] + '|' + game_table[3])
    print("-|-|-")
    print(game_table[4] + "|" + game_table[5] + '|' + game_table[6])
    print("-|-|-")
    print(game_table[7] + "|" + game_table[8] + '|' + game_table[9])


print_game_table(the_table)


def player_input():
    player_choice = input("Please enter a marker X or O: ")
    while player_choice != 'X' and player_choice != 'O':
        player_choice = input("Please enter a marker X or O: ")
    return player_choice


player_input()


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


win_check(the_table,'X')

print('\n' * 5)
