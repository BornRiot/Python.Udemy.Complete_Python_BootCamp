"""Topic covbered in theis lecture is list comprehension. this is an alternativ
e to using a for loop with the append function"""
mylist = []
mystring = 'hello'
for letter in mystring:
    mylist.append(letter)
mylist = [letter for letter in mystring]
print(mylist)
mylist = [x for x in 'word']
print(mylist)
mylist = [x for x in range(0, 11)]
print(mylist)
mylist = [x ** 2 for x in range(0, 11)]
print(mylist)
mylist = [x for x in range(0, 11) if x % 2 == 0]
print(mylist)
print(mylist)
celcius = [0, 10, 20, 34.5]

fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
print(fahrenheit)
fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9 / 5) * temp + 32))
    print(fahrenheit)
results = [x if x % 2 == 0 else 'odd' for x in range(0, 11)]
print(results)
print('This is a new heading ')
my_list = []
for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        mylist.append(x * y)
print(mylist)

print('at video marker 10:58')
my_list = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(my_list)

# freeform
# the following lines of code is used to append elements from a tuple to a list
the_list = []
the_tup = (2, 5, 9, 7)
for ele in the_tup:
    the_list.append(ele)
print(the_list)
# using list comprehension
the_list = [list(x for y in the_tup)]
print(the_list)
sec_lis = [y for y in the_list.pop()]
print('thua is sec liar ')
print(sec_lis)
print("using list comprehension ")

mylist1 = [1, 2, 3, 4, 5, 5, 6]
mylit2 = ['a', 'b', 'c']

new_var = list(zip(mylist1, mylit2))
print(new_var)
print('after this')
some_list = []

for the_juice, the_sauce in new_var:
    some_list.append(the_juice)
    some_list.append(the_sauce)
print(some_list)
