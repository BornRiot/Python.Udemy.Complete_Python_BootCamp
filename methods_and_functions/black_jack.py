"""
This module is used to solve the black jack problem in the methods section
through simulating  the playing of Black Jack
"""
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

print(black_jack(5, 6, 7))
