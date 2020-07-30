# You can print out an error message to the user stating that
# the input entered is incorrect


# Check if the user input entered is both a digit and within
# a specified range. This is a rewrite of the function

def user_choice():
    # Variables

    # Initial
    choice = "0"
    acceptable_range = range(0, 11)
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


the_input = user_choice()
print(the_input)
