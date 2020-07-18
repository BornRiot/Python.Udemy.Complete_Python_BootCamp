"""
This module is used to create my first project in the course.
The projects calls for creating a tic-tac-toe game using python
"""
# define place elements in the  board
the_table = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]


# Display the game board
def print_game_table(game_table):
    print(game_table[0] + "|" + game_table[1] + '|' + game_table[2])
    print("-|-|-")
    print(game_table[3] + "|" + game_table[4] + '|' + game_table[5])
    print("-|-|-")
    print(game_table[6] + "|" + game_table[7] + '|' + game_table[8])


print_game_table(the_table)


def replacement_choice(game_table, position):
    """Func string"""
    user_placement = input("Type a string to place at position:")
    game_table[position] = user_placement
    return game_table


def game_on_choice():
    """Function docstring"""
    choice = "Wrong"

    while choice not in ['Y', 'N']:
        choice = input("Keep playing: (Y or N) ")
        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand. Please choose Y or N")
    if choice == 'Y':
        return True
    else:
        print("Game Over")
        return False


game_on = True
while game_on:
    take_position = int(input("Please enter a position to be replace(0-8): "))

    the_table = replacement_choice(the_table, take_position)

    print_game_table(the_table)

    game_on = game_on_choice()

print_game_table(the_table)


def new_func(some_arg):
    print(some_arg)
