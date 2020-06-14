"""This is my module docstirng"""

def has_33(the_list):
    """This is my function docstirng"""
    some_list = [3, 3]
    return set(some_list).issubset(set(the_list))

print(has_33([6, 3, 3]))
