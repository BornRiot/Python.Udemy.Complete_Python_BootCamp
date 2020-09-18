"""
Module and lecture discusses advanced built in method for string objects
"""

s = 'hello world'

#change case using the capitalize():
print('change case using the capitalize():', s.capitalize())
#change to upper case using the upper():
print('change to upper  case using the upper():', s.upper())
#change to lower case using the upper():
print('change to lower case using the lower():', s.lower())

#count the occurence of specific letters in a string:
print('Count the occurence of "o" using count(o):', s.count('o'))

# find the first occurence of  letter in a string using find():
print('Find the first occurence of "o" in a string: ', s.find('o'))

# use the center() to center a string in between another:
print('This is hellow world in the middle of Zs',  s.center(20, 'z'))


# use of the expand tabs method:
print("use of the expand tabs method with backslash character:", 'hello\thi')
print('using the .expandtabs(): hello\thi'.expandtabs())

# check if all characters in a string are alphanumeric:
s = 'hello'
print('Check if alphanumeric:', s.isalnum())

# check if all charct are alphabetic:
print('Check aplabetic: ', s.isalpha())

#check if all characters are lower case:
print('all char low:', s.islower())

# Check if all charc are whitespace:
print('All char whitespace:', s.isspace())

# check if a string is a title:
print('Is string title:', s.istitle())

# check if all characters are upper:
print('All char upper:', s.isupper())

# check if a string ends with a particular character:
print('String ends with "o" using endswith():', s.endswith('o') )
print('Can also be done using s[-1]=="0": ', s[-1]=='o')


# use split() the string  at the instance of a character:
print('Split string a char e:', s.split('e'))

# use of partition() to split at the only the first instance of
# a character and print the rest od the remainding string.
a = 'hiihhihihihhhi'
print('partition at the first occurence of i in hiihhihihihhhi:', a.partition('i') )
