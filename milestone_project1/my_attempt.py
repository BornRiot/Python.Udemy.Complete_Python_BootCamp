"""
Module docstring
"""
# define the board
the_board = list()


def append_board_item(game_board, item):
    if len(game_board) < 9:
        game_board.append(item)
    else:
        print("Cannot append item. Limit reached ")


# Define how the board will be displayed
def print_the_board(get_board):
    print(get_board[0:3])
    print(get_board[3:6])
    print(get_board[6:9])


def the_user_choice():
    # You can print out an error message to the user stating that
    # the input entered is incorrect

    # Check if the user input entered is both a digit and within
    # a specified range. This is a rewrite of the function

    # Variables

    # Initial
    choice = "0"
    acceptable_range = range(0, 10)
    within_range = False

    # Two conditions to check
    # Digit or within  range == False
    while not choice.isdigit() or not within_range:

        if not choice.isdigit():
            print("You have entered a non-digit")
        choice = input("Please enter a number (0-10): ")

        # Range check
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of range")
                within_range = False

    return int(choice)


append_board_item(the_board, 's')
append_board_item(the_board, 's')
append_board_item(the_board, 's')
append_board_item(the_board, 's')
append_board_item(the_board, 's')
append_board_item(the_board, 's')
append_board_item(the_board, 's')
append_board_item(the_board, 's')
append_board_item(the_board, 's')
append_board_item(the_board, 's')
# append_board_item(the_board, 's')

print_the_board(the_board)
