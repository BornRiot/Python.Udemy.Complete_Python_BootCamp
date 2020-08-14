def choose_player():
    print("players, please choose your markers X or O")
    player_1 = input("Player 1 first: ")
    print("Player 1 has chosen " + player_1)
    player_2 =input("Player 2, please choose the opposite of player 1: ")
    return player_1, player_2


first, second = choose_player()
print(first)
print(second)