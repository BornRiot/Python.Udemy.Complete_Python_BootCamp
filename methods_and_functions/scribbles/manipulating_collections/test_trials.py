"""DOCSTRING"""
test_list = [1, 2, 3, -4, 5, 6, 7, 8, 9, -10]
test_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
TEST_STRING = "This is a test string"
test_dictionary = {'a1': 5, 'b2': 3.4, 'c3': [1, 2, 3], 'd4': "word"}


def list_func(num):
    """STRING"""

    for i in range(len(num)):
        print(i)
    # temp_hold = 1
    # for v in num:
    #     temp_hold *= v
        #
        # print(temp_hold)
    # for x in range(len(num)-2):
    #     if num[x]*num[x+1] < num[x+1]*num[x+2]:
    #         temp_hold = num[x]*num[x+1]
    #         print(temp_hold)
    #         temp_hold+=1
    # Separate operation
    # topple = 0
    # for c in num:
    #     print(topple * c)
    #     topple += 2
    # res = 10
    # for x in num:
    #     res *= x
    #
    # return res, indentation is very important in python
    # Separate operation
    # for x in range(len(num)+1):
    #     print(x*2) multiply all elements in a list by 2


def tuple_func():
    pass


def string_func():
    pass


def dict_func():
    pass


print(list_func(test_list))
