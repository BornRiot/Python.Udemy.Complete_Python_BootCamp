"""
This ,odule is used to solve the Summer of 69 coding challenge
"""

def summer_69(*args):
    """This is my function docstring for this program"""
    total = 0
    add = True
    for num in args:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
print(summer_69(2, 1, 6, 9, 11))
