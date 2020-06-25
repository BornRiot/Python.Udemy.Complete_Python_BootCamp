"""
This module is used to solve the black jack problem in the methods section
through simulating  the playing of Black Jack
"""
def blackjack_c(a,b,c):

    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'

def black_jack(*args):
    """
    This function is used to create the necessary elements to
    carry out the process of playing the game
    """
    the_cards = list(args)
    results = None
    if sum(the_cards) <= 21:
        results = sum(the_cards)
    elif sum(the_cards) > 21 and 11 in  the_cards:
        new_sum_val = sum(the_cards) - 10
        if new_sum_val > 21:
            results = 'BUST'
        else:
            results = new_sum_val
    elif sum(the_cards) > 21:
        results = 'BUST'
    return results

print(black_jack(7, 6, 11))
print("this is the correct answer:")
print(blackjack_c(7, 6, 11))
