"""This module is used to solve the almost there problem in the section"""


def almost_there(n):
    """This is my function docstring"""
    # Get the absolute value of n
    n = abs(n)
    # Create the ranges to test for n
    hundi_range = list(range(90, 111))
    two_hundi_range = list(range(190, 211))
    # see if n is in any of the ranges
    return n in hundi_range or n in two_hundi_range


print(almost_there(150))
