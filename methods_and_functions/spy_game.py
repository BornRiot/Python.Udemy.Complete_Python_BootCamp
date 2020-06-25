"""This module is used to solve the spy_game challenge"""
def spy_game_c(nums):

    code = [0,0,7,'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works

    return len(code) == 1

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
print(spy_game([1,0,2,4,0,5,7]))
print('This is the correct answer')
print(spy_game_c([1, 0, 0, 7, 0, 1, 5, 98, 47, 69]))
