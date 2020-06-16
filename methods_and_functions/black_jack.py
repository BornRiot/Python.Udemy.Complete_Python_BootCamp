"""This module is used to simulate the playing of Black Jack"""
#this is a line of code to change a list into a tupled list.
#It includes the index along with the value: #Turn list into tuple list:
#result = list(enumerate(the_cards))


# def black_jack(*args):
#     "This is my function docstring"
#     result = None
#     the_cards = [x for x in args]
#     for index_y in the_cards:
#         if sum(the_cards) == 21:
#             result = "Black Jack"
#         elif index_y == 11 or [index_y+1] == 11 or [index_y+ 2] == 11:
#             result = sum(the_cards) - 11
#             if sum(the_cards) == 21:
#                 result = "Black"
#             elif sum(the_cards) < 21:
#                 print(sum(the_cards))
#                 result = sum(the_cards)
#             else:
#                 result = "Bust"
#         return result

def check_vals(list1, val):
    for c in list1:
        if val == c:
            return True
        else:
            return False
def black_jack(*args):
    """This is my function docstring"""
    result = None # Create a none value  to be used to store and return
    # final results
    the_cards = list(args)
    for the_cards_i, the_cards_v  in enumerate(the_cards):
        if the_cards_v == 0:
            #Look into using nested for loops to check value
            result = "Do this"
        if sum(the_cards) == 21:
            result = "Black Jack"















    return result



print(black_jack(10, 5, 11))
