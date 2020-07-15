# Created a list to represent the tic tac toe board
the_game_board = list()


# Create a function to display the board in a 3 * 3 matrix
def display_board(the_board):
    print(the_board[0:3])
    print('---------------')
    print(the_board[3:6])
    print('---------------')
    print(the_board[6:9])


board = []

for row in range(3):
    board.append([])
    for column in range(3):
        board[row].append("---")


def print_board(board):
    for row in board:
        print("|".join(row))
        for mark in row:
            print(mark)


print_board(board)

# display_board(the_game_board)
