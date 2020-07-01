"""
This module houses code to return the unique elements in a list
from the orginal list.
"""

def unique_list(the_list):
    """Docstring"""
    the_set = set(the_list)

    def new_list(the_set):
        the_final_list = list(the_set)
        print(the_final_list)

        return new_list

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
