def count_evens(my_list):
    return list.__len__([num for num in my_list if num % 2 == 0])

def count_evens2(my_list):
    return len([num for num in my_list if num % 2 == 0])


print(count_evens(([25,14,18,16,4,6])))
print(count_evens2(([25,14,18,16,4,6])))
crack = [10,8,6,4,2,8,12]
list_len = len([num for num in crack if num % 2 == 0])
print(list_len)
