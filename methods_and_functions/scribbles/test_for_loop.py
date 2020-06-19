"""
This program will br used to test the use of a for loop to solve the black
jack problem
"""
def my_func(*args):
    """
    This is my module docstring for my function. It is ued to test
    resolutions for the black jack program
    """
    #Create a list of numbers from arguments given in function parameter
    a_new_list = list(args)

    #Create for loops to iterate through elements in the list
    for a_new_list_i, a_new_list_v in enumerate(a_new_list):
        for x in a_new_list:
            print(a_new_list)
            print(a_new_list_i)
            return x == a_new_list_v


print(my_func(1, 5, 9))
