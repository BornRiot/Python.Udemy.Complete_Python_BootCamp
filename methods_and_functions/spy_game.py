"""This module is used to solve the spy_game challenge"""


def spy_game(nums):
    """This function is used to run the program when given the arguments"""
    perfect_agent = [0, 0, 7]
    result = set(x in nums for x in perfect_agent)

    flag = 0
    for ans in result:
        if not ans:
            flag = 1
    final_result = True
    if flag == 0:
        final_result = True
    else:
        final_result = False
    return final_result


print(spy_game([1, 0, 0, 7, 0, 1, 5, 98, 47, 69]))
