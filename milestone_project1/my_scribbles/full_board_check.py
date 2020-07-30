test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'Y']


def full_board_check(board):
    new_list = list()
    for index, letter in enumerate(board[1:10]):
        if letter == 'X' or letter == 'O':
            new_list.append(1)
        else:
            new_list.append(0)
    return all(new_list)


print(full_board_check(test_board))
