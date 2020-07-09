"""
This module holds all the resources needed to run the finished files of the game
tic tac toe
"""
game_list = [0, 1, 2]


def display_game(the_list):
    """F"""
    print("Here is the current list: ")
    print(the_list)


display_game(game_list)


def position_choice():
    """Function docstring"""
    choice = "Wrong"

    while choice not in ['0', '1', '2']:
        choice = input("Pick a position (0,1,2): ")
        if choice not in ['0', '1', '2']:
            print("Sorry, invalid choice")
    return int(choice)


def replacement_choice(game_list, position):
    """Func string"""
    user_placement = input("Type a string to place at position:")
    game_list[position] = user_placement
    return game_list


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
game_list = [0, 1, 2]

while game_on:
    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = game_on_choice()
