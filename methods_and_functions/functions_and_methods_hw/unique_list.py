"""
This module houses code to return the unique elements in a list
from the orginal list.
"""


def unique_list(the_list):
    """This is my function docstring"""
    def to_new_set():
        return list(set(the_list))
    return to_new_set


vals = unique_list([11, 11, 25, 25, 36, 98, 8, 8, 47])
print(vals())
