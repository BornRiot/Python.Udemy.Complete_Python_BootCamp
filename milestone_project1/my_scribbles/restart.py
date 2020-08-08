test_board = [None, "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def display_board(game_table):
    """
    function that can print out a board. Sets up the board as a list,
    where each index 1-9 corresponds with a number on
    a number pad, so there is  a 3 by 3 board representation.
    """
    print(game_table[1] + "|" + game_table[2] + '|' + game_table[3])
    print("-|-|-")
    print(game_table[4] + "|" + game_table[5] + '|' + game_table[6])
    print("-|-|-")
    print(game_table[7] + "|" + game_table[8] + '|' + game_table[9])
def replay():
    """Function docstring"""
    choice = "Wrong"

    while choice not in ['Y', 'N']:
        choice = input("Do you want to replay the game: (Y or N) ")
        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand. Please choose Y or N")
    if choice == 'Y':
        return True
    else:
        print("Good Bye")
        return False


def win_check(board, mark):
    """
    function that takes in a board and a mark (X or O) and
    then checks to see if that mark has won.
    """

    # This is the instructor's solution code for the win_check function.
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def full_board_check(board):
    """
    function that checks if the board is full and returns
    a boolean value. True if full, False otherwise
    """
    new_list = list()
    for index, letter in enumerate(board[1:9]):
        if letter == 'X':
            new_list.append(1)
        elif letter == 'O':
            new_list.append(1)
        else:
            new_list.append(0)
    return all(new_list)


game_on = True
x_won = win_check(test_board, 'X')
o_won = win_check(test_board, "O")
while game_on:
    space = int(input("Enter index"))
    test_board[space] = input("Enter value")
    display_board(test_board)
    boar_full = full_board_check(test_board)
    if boar_full:
        game_on = replay()
    elif win_check(test_board,'O') or win_check(test_board,"X"):
        game_on = replay()
    # elif x_won:
    #     print("X has won")
    #     game_on = replay()
