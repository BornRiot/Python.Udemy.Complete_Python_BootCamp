"""This module correcspond to the code along leture with same title"""


d = {'k1':1, 'k2':2}
print(d['k2'])
for x in d.keys():
    print(x)

# Syntax for dictionary comprehension:
the_comp = {x:x**2 for x in range(10)}
print(the_comp)

# Assign keys in a dictionary that are not based on the values:
no_val_keys = {k:v**2 for k,v in zip(['a','b', 'c'], range(3))}
print(no_val_keys)

# iterate over dictionary items:
print('The items in dictionary d are:')
for k in d.items():
    print(k)

# iterate over dictionary values:
print('The values in dictionary d are: ')
for k in d.values():
    print(k)

# iterate over dictionary keys:
print('The keys in dictionary d are:')
for k in d.keys():
    print(k)
