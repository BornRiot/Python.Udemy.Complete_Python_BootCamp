"""
This module is used to solve the count_case problem in a string from the
functions and methods homework. This solution uses the collections module
and islower function to count the case of the letters in the sentence
"""
# Author: Marvin DaCosta, Created June 27, 2020, Last Modified: June 28, 2020

# Possible solution for using the collections module
# https://bit.ly/3gaheq3
from collections import Counter # Import Counter from collections

# Sanple string to use in program
SAMPLE_STRING = 'Hello Mr. Rogers, how are you this fine Tuesday?'





def use_counter(the_string):
    """This is my function docstring"""
    for case in the_string:
        if case.isupper():
            upper_count = Counter(case)
            print(upper_count)
        elif case.islower():
            lower_count = Counter(case)
            print(lower_count)

use_counter(SAMPLE_STRING)
