"""
This module is used to create my first project in the course.
The projects calls for creating a tic-tac-toe game using python
"""
# define place elements in the  board. Visual list star at 1 not 0
the_table = [None, "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# Code to display the game board
def print_game_table(game_table):
    print(game_table[1] + "|" + game_table[2] + '|' + game_table[3])
    print("-|-|-")
    print(game_table[4] + "|" + game_table[5] + '|' + game_table[6])
    print("-|-|-")
    print(game_table[7] + "|" + game_table[8] + '|' + game_table[9])


print_game_table(the_table)


def replacement_choice(game_table, position):
    """Code for replacing user choice when option is chosen """
    user_placement = input("Type a string to place at position:")
    game_table[position] = user_placement
    return game_table


def game_on_choice():
    """Function docstring"""
    choice = "Wrong"

    while choice not in ['Y', 'N']:
        choice = input("Keep playing?: (Y or N): ")
        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand. Please choose Y or N:")
    if choice == 'Y':
        return True
    else:
        print("Game Over")
        return False


game_on = True
while game_on:
    take_position = int(input("Please enter a position to be replaced(1-9): "))

    the_table = replacement_choice(the_table, take_position)

    print_game_table(the_table)

    game_on = game_on_choice()

print_game_table(the_table)
