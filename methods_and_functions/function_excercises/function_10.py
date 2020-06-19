"""My module docstring """



def myfunc2(some_str):
    """This is my module docstring"""
    new_string = str(some_str).lower()
    next_string = ""
    for i, v in enumerate(new_string):
        if i % 2 == 0:
            next_string += v.upper()
        else:
            next_string += v.lower()
    return next_string


def myfunc(*args):
    """My function docstring"""
    mynewstring = ''

    mystring = str(args[0])

    for num in range(len(args[0])):

        if num % 2 == 0:

            mynewstring = mynewstring + mystring[num].upper()

        else:

            mynewstring = mynewstring + mystring[num].lower()

    return mynewstring


print(myfunc("ringside"))
