"""
Module docstring
"""
# define the board
the_table = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Display the game board
def print_game_table(game_table):
    print(game_table[0] + "|" + game_table[1] + '|' + game_table[2])
    print("-|-|-")
    print(game_table[3] + "|" + game_table[4] + '|' + game_table[5])
    print("-|-|-")
    print(game_table[6] + "|" + game_table[7] + '|' + game_table[8])


print_game_table(the_table)
