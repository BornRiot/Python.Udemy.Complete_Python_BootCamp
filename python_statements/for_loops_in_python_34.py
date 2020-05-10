# pylint: disable=C0103
""" This program covers the topic of for loops in python """
# many objects in python  are iterable, which meanss you can go through each element in the object
# Trailing white speces generally occur at the end of the line
# Syntax of a for loop:
my_iterable = [1, 2, 3]
for item_name in my_iterable:
    print(item_name)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in my_list:
    print(num)
for jelly in my_list:
    print('Hello')
for num in my_list:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number:{num}')
list_sum = 0

for num in my_list:
    list_sum = list_sum + num
print(list_sum)  # Indenting this line directly under the list_sum will
# give you a running tally od the numbers

the_word = "Rona is here"
for letter in the_word:
    print(letter)

for ghgh in 'Hello World':
    print(ghgh)

tup = (1, 2, 3)
for item in tup:
    print(item)

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
len(mylist)

for (a, b) in mylist:
    print(a)
    print(b)
    print("ends here")

the_list = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]
for a, b, c in the_list:
    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}  # prints the index
for item in d:
    print(item)

for item in d.items():
    print(item)

    for key, value in d.items():
        print(value)
for key, value in d.items():
    print(key, value)
# free form
first_list = [(-4, 5, 8), (0, 1, 2), (1, 2, 4), (2, 4, 8)]
print(first_list[0])
# my_tup = first_list[0] + first_list[1]
# print(my_tup)
for the_stuff in first_list:
    my_tup = first_list.index(1)
    print(my_tup)

print('stop')
