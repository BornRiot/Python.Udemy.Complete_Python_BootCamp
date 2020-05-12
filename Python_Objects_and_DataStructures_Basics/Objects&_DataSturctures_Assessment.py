# def: numbers- numerical data type that can be used to perform calculations in python
# def: Strings- immutable objects used to output text o the screen in python
# def: list - objects used to hold an ordered pair of data such as integers, decimals and strings. can be changed
# def: tuples- data object used to store a group of elements that are not changeable. elements are ordered.

myObject = [9, 0, 35, 'word']
myObject2 = (4, 3,3, 'word')
myObject3 = {2, 'something'}
print(type(myObject))
print(type(myObject2))
print(type(myObject3))
print(myObject3)
# The object below is an exampple of a dictionary which can hold an array of different object types
myDict = {'taste': "sweet ",
          'color': "blue",
          'weight': " 5PBS",
          'numbers': 4,
          'decimal': 4.2
          , 'taste': "sour"}
# if there are duplicate members in a dictionary, python will only recognize the value of the second repeated diction
# ary object
# of the second
# How to print objects in a dictionary in python:
x = myDict['taste']
# print(x)
# print(myObject)
# print(myObject2)
print(tuple(myObject))
myObject[1] = 'something'

# Numbers assignments: write equation  that uses multi, div, add, subtra to get value 100.25
print(150 - 5**2 + .25 * 1 - (100/(5*5))-21)
# Final answer for this question
# you cannot simply add an integer and a string together in python to be printed on the screen
# a method of type casting has to be used. Example shown below
posANS1 = 44
posANS2 = 29
posANS3 = 34
print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)
print("this is the answer of P1 is:  " + str(posANS1))
print("this is the answer of P2 is:  " + str(posANS2))
print("this is the answer of P3 is:  " + str(posANS3))
whatIsThis = 3 + 1.5 + 4
print(type(whatIsThis))
print(whatIsThis)
print(5**5)
print(5**2)
myDivisor = 100
print(pow(225, .5))

n = "hello"
print(n[4::-1])
# This is an example of slicing. The uses the methos to reverse the string.

# Given the string hello, give two methods of producing the letter 'o' using indexing.
# The code below uses indexing to grab the o in "hello"
s = 'hello'
# Print out the 'o'

# Method 1:
print(s[4])
# Method 2
print(s[4:5:1])

# build a list two separate ways
first_list = (0,0,0)

h = 0
second_list = (h, h, h)
print(second_list)

a = (4, 0, 9, 5)
b =(7, 5, 0)
c = (7, 2, 8, 0, 9)

final_list = (a[1], b[2], c[3])
print(final_list)


list3 = [1,2,[3,4,'hello']]
print(list3)
list3[2][2] = "goodbye"
print(list3[2][2])


# sort this list

list4 = [5, 3, 4, 6, 1]
list4.sort( )

print(list4)
print(type(list4))

# Examples of lists, tuples, sets, dictionaries.
# This is a list
first_ex = [2,4,6,8]
# This is a tuple
sec_ex = (1,3,5,7)
# This is a set
third_ex = {20,18,16,14}
# This is a dictionary
fourth_ex = {'key1': "first element "}
print("The third example is a: ", type(third_ex))
print(type(fourth_ex))


# d = {'k1': {'k2': 'hello'}}
# print(d['k1']['k2'])

d = {'k1': [{'nested_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nested_key'][1][0])

print(d['k1'])


# This will be hard and annoying!
d = {'k1':
         [1,2,
          {'k2':
               ['this is tricky',
                {'tough':
                     [1,2,
                      ['hello']
                      ]}]}]}
print(d['k1'][0]['k2']['tough']) 