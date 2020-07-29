def register_players_marker():
    player2_choice = ""
    """Register the players choice of playing as  X or O """
    player1_choice = input("Player 1, please enter a marker X or O: ")
    player1_choice = player1_choice.upper()
    while player1_choice != 'X' and player1_choice != 'O':
        player1_choice = input("Sorry, wrong input. Please enter a marker X or O: ")
        player1_choice = player1_choice.upper()
    if player1_choice == 'X':
        player2_choice = 'O'
    elif player1_choice == 'O':
        player2_choice = 'X'
    return player1_choice, player2_choice

def display_marker_choice(p1_choice, p2_choice):
    print("Player 1 will be playing as: "+p1_choice)
    print("Player 2 will be playing as: "+p2_choice)


first_player, second_player = register_players_marker()

display_marker_choice(first_player,second_player)