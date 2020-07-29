the_table = [None, "1","2","3","4","5","6","7","8","9"]

def get_player_choice():
    player_one = ""
    player_two = ""
    while player_one != "O" or player_one != "X":
        player_one = input("Please enter choice")
        if player_one == "X":
            player_two ="O"

    return player_one,player_two

first_player, second_player = get_player_choice()
print(first_player)
print(second_player)