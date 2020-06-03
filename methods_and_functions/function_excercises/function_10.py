"""My module docstring """

"""My module docstring """


def myfunc(*args):
    mynewstring = ''

    mystring = str(args[0])

    for num in range(len(args[0])):

        if num % 2 == 0:

            mynewstring = mynewstring + mystring[num].upper()

        else:

            mynewstring = mynewstring + mystring[num].lower()

    return mynewstring


print(myfunc("ringside"))
