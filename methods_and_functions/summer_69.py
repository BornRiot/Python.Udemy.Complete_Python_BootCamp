"""
Used answer specified in course materials
"""
def summer_69_c(arr):
    total = 0
    add = True
    for num in arr:
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



print(summer_69_c([2, 1, 6, 9, 11]))
