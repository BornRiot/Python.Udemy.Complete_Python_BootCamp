"""
This module is used to create my first project in the course.
The projects calls for creating a tic-tac-toe game using python
"""
# define place elements in the  board
the_table = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


# Display the game board
def print_game_table(game_table):
    print(game_table[0] + "|" + game_table[1] + '|' + game_table[2])
    print("-|-|-")
    print(game_table[3] + "|" + game_table[4] + '|' + game_table[5])
    print("-|-|-")
    print(game_table[6] + "|" + game_table[7] + '|' + game_table[8])


print_game_table(the_table)


def replacement_choice(game_list, position):
    """Func string"""
    user_placement = input("Type a string to place at position:")
    game_list[position] = user_placement
    return game_list


change_stuff = replacement_choice(the_table, 8)
print_game_table(the_table)