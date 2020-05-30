""""My module docstring"""


def is_greater(a, b):
    """"
    My function docstring
    """
    if a > b:
        return True
    elif a <= b:
        return False


def myfunc(*args):
    return sum(args)


def count_args(*args):
    my_val = len(args)
    return "The number of arguments in the parameter is: {}".format(my_val)


print(myfunc(4, 9, 8, 4, 5))

print(is_greater(5, 25))
print(count_args(4, 9, 8, 4, 5))

