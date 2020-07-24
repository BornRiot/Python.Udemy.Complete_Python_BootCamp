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

print('\n' * 5)
