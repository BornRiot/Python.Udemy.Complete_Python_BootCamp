"""
This is my module docstring
"""


def myfunc(x, y, z):
    """
    This is my function docstring
    """
    if z:
        return x
    else:
        return y


print(myfunc("The argument was True", "The argument was False", True))
