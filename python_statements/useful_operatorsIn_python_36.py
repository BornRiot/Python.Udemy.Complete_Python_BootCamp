from random import shuffle
from random import randint

"""
this program  is used to cover the topic of useful operators in python.
"""
mylist = [1, 2, 3]
for num in range(10):
    print(num)

# the previous code can be edited to use the folllowing syntax
# for num in range(0, 10,2)
# print(num)

# trying to get output from just range(0,1,10) will just return the function

# you can create a list using the range function:
d = list(range(0, 11, 2))
print(d)

# the enumerate function
index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1
print('End of first example')

# this is a second example

sec_index = 0
word = 'abcde'
for letter in word:
    print(word[sec_index])
    sec_index += 1

# the preceding code can be written to not only show the letters but also there index values
word = 'abcde'

for item in enumerate(word):
    print(item)
# can also print the index, letter seperately
print('new example starts below  this line')
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')
my_list1 = [1, 2, 3, 4, 5, 5, 6]
my_list2 = ['a', 'b', 'c']

new_var = zip(my_list1, my_list2)
print('line before un-print')
print(new_var)  # cannot print the items like this
for item in zip(my_list1, my_list2):
    print(item)  # the zip function is used to pair the elements from both list together
# creation of mylist3 to be used with the other list
mylist3 = [100, 200, 300]
for item in zip(my_list1, my_list2, mylist3):
    print(item)
# the zip function will not return elements if they cannot all be paired together or end up uneven
# use list function to create list from zips
this_new_list = list(zip(my_list1, my_list2))
# output the new list
print(this_new_list)
print('that was the result')
print('x' in [1, 2, 3])
print('x' in ['x', 'y', 'z'])
print('a' in 'a world')
d = {'mykey': 345}
print('mykey' in d.items())
print(345 in d.values())
mylist = [10, 20, 30, 40, 100]
print(min(mylist))
print(max(mylist))

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(mylist)
print(mylist)  # the list has been shuffled
# assign the shuffled list to a new list
the_lastlist = shuffle(mylist)  # caanot be done, method only  runs in place
print(the_lastlist)


therand = randint(0, 100)
print(therand)
my_num = randint(0, 200)
print(my_num)
# take input from user
input('Enter something')
# store input in a variable
the_name = input("Whats your name")
print(the_name)
# create input that ask for favorite number then cast it to float
result = input("Whats your favorite number")
print(type(result))
result = float(result)
print(type(result))
