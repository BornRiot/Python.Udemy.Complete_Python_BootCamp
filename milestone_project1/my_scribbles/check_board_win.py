the_table = [None, "O", "O", "O", "4", "5", "6", "7", "8", "9"]


def print_game_table(game_table):
    print(game_table[1] + "|" + game_table[2] + '|' + game_table[3])
    print("-|-|-")
    print(game_table[4] + "|" + game_table[5] + '|' + game_table[6])
    print("-|-|-")
    print(game_table[7] + "|" + game_table[8] + '|' + game_table[9])


def arrayCheck(nums):

    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for i in range(len(nums)-2):
        # Check in sets of 3 if we have 1,2,3 in a row
        if nums[i+1]=='O' and nums[i+2]=='O' and nums[i+3]=='O':
            return True
    return False


print(arrayCheck(the_table))