"""
Module docstring
"""
# define the board
the_board = list()


# Define how the board will be displayed
def print_the_board(get_board):
    print(get_board[0:3])
    print(get_board[3:6])
    print(get_board[6:9])


print_the_board(the_board)


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


get_choice = the_user_choice()
print("This is the choice", get_choice)
