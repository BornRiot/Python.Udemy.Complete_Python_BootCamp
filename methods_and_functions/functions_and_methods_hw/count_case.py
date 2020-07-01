"""
This module is used to solve the count_case problem in a string from the
functions and methods homework. This solution uses a for loop and islower
function to count the case of the letters in the sentence
"""

# Author: Marvin DaCosta, Created June 27, 2020, Last Modified: June 28, 2020

# YouTube video on how to use collections in python:
# https://bit.ly/2NBaCV6

# Create a sample string to be used in function
SAMPLE_STRING = 'Hello Mr. Rogers, how are you this fine Tuesday?'


# Create a function to loop through each character in the string
def count_loop(the_string):
    """
    This function is used to loop through each charcter in the string and
    count each lower and upper case character and then return the count for each
    """
    count_u = 0
    count_l = 0
    for case in the_string:
        if case.isupper():
            count_u += 1
        elif case.islower():
            count_l += 1
    return count_l, count_u


lower, upper = count_loop(SAMPLE_STRING)
print("There are", upper, "upper case  and ", lower, \
      "lower case characters in the string")
