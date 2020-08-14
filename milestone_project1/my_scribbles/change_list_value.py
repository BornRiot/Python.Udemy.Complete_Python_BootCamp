game_board = ['#', '7', '8', '9', '4', '5', '6', '1', '2', '3']


def change_stuff(value):
    for index, item in enumerate(game_board):
        if item == str(value):
            game_board[index] = 'L'


change_stuff(4)

print(game_board)
