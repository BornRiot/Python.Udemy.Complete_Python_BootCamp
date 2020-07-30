the_table = [None, "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def print_game_table(game_table):
    print(game_table[1] + "|" + game_table[2] + '|' + game_table[3])
    print("-|-|-")
    print(game_table[4] + "|" + game_table[5] + '|' + game_table[6])
    print("-|-|-")
    print(game_table[7] + "|" + game_table[8] + '|' + game_table[9])


def replacement_choice(game_table, position, piece):
    """Code for replacing user choice when option is chosen """

    game_table[position] = piece
    return game_table

def game_on_choice():
    """Function docstring"""
    choice = "Wrong"

    while choice not in ['Y', 'N']:
        choice = input("Keep playing? (Y or N): ")
        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand. Please choose Y or N:")
    if choice == 'Y':
        return True
    else:
        print("Game Over")
        return False

player_one_piece = input("Player 1, please select X or O to play with: ")
def player_one():

    take_position = int(input("Please enter a position to be replaced(1-9): "))

    replacement_choice(the_table, take_position, player_one_piece)

    print_game_table(the_table)

def player_two():
    player_two_piece = ""
    if player_one_piece == 'X':
        player_two_piece='O'
    elif player_one_piece == 'O':
        player_two_piece = 'X'

    take_position = int(input("Player 2, please enter a position to be replaced: "))

    replacement_choice(the_table, take_position, player_two_piece)

    print_game_table(the_table)


game_on = True
while game_on:
    player_one()
    player_two()

    game_on = game_on_choice()

