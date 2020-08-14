the_table = [None, "X", "2", "3", "X", "5", "6", "X", "8", "9"]


def print_game_table(game_table):
    print(game_table[1] + "|" + game_table[2] + '|' + game_table[3])
    print("-|-|-")
    print(game_table[4] + "|" + game_table[5] + '|' + game_table[6])
    print("-|-|-")
    print(game_table[7] + "|" + game_table[8] + '|' + game_table[9])


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


print_game_table(the_table)
x_win =win_check(the_table, 'X')
