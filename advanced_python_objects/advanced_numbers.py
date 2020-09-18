"""Lesson and program covers built in methods for numbers in python"""

# convert int to hexidecimal
print('This is the hexidecimal equivalent to 12:', hex(12))
print('This is the hexidecimal equivalent to 512:', hex(512))

# convert int to binary
print('This is the binary equivalent to 1234:', bin(1234))


# calling to the power of a number:
print("Raising to the power of a number using **", 2**4)
print("Power of a number using pow:", pow(2,4))
print("pow with three args uses the 3rd num for getting remainder:", pow(2,4,3))

#use of the abs() function:
print('abs() returns the absolute value, ex: abs(-12) =', abs(-12))

#use of the round() function to round numbers:
print('The round() function can be used to round numbers in python')
print('Example: round(3.14592) to 2 decimal places = ', round(3.14592,2))
