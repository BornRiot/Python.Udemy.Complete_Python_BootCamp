test_board = ['#', 'X', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X']



def replay():
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


def is_full(my_board):
    check_val = []
    for letter in my_board[1:9]:
        if letter == 'X' or letter == 'O':
            check_val.append(1)
        else:
            check_val.append(0)
    return all(check_val)

game_on = False
if is_full(test_board):
    game_on = replay()

if game_on:
    test_board.clear()
    print(test_board)

