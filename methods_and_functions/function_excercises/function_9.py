"""
My module docstring
"""


def my_func(*args):
    """
    This is my function docstring
    """
    nums = [x for x in args if x % 2 == 0]
    return nums


print(my_func(2, 4, 8, 9, 20, 36, 59, 98, 47, 58, 69))
