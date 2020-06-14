"""This is my module docstring  """


def paper_doll(*args):
    """My function docstring"""
    to_str = str(args[0])
    the_mod_str = ''

    for item in range(len(args[0])):
        the_mod_str = the_mod_str + to_str[item] * 3
    return the_mod_str


print(paper_doll("Mississippi"))
