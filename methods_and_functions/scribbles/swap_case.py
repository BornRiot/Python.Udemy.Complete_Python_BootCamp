"""This is my module docstring """

def myfunc (some_str):
    """This is my module docstring"""
    new_string = str(some_str).lower()
    next_string = ""
    for i, v in enumerate(new_string):
        if i % 2 == 0:
           next_string +=  v.upper()
        else:
            next_string += v.lower()
    return next_string


print(myfunc("anthropomorphism"))