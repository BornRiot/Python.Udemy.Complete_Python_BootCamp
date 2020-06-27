from collections import defaultdict

"""
This module is used to solve the count_case problem in a string from the
functions and methods homework.
"""
# YouTube video on how to use collections in python:
# https://bit.ly/2NBaCV6

# Create a sample string to be used in function
SAMPLE_STRING = 'Hello Mr. Rogers, how are you this fine Tuesday?'


# Create a function to loop through each character in the string

def count_collection(some_string):
    global upper_d, lower_d
    the_dict = defaultdict(int)
    the_dict_U = defaultdict(int)

    for characters in SAMPLE_STRING:
        the_dict[characters.islower()] += 1
        the_dict_U[characters.isupper()] += 1
        upper_d = the_dict_U.values()
        lower_d = the_dict.values()
    return upper_d, lower_d


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

the_item = count_collection(SAMPLE_STRING)
for z, y in the_item:
    print(z, y)
