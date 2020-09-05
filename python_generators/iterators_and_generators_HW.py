"""
Module is used to complete the Iterators and Generators Hone Work
"""
import random


# P1: Create a generator that generates the squares of numbers up to some number N.
def gen_squares(n):
    for a in range(n):
        yield a ** 2


# Test gen_squares
for x in gen_squares(10):
    print(x)


# P2:Create a generator that yields "n" random numbers between a low and high number (that are inputs).
def rand_num(low, high, n):
    for l in range(n):
        yield random.randint(low, high)


print("The list of random numbers are: ")
for num2 in rand_num(1, 10, 12):
    print(num2)

# Question 3: Use the iter() function to convert the string below into an iterator.
s = 'hello'
iter_s = iter(s)
for letter in iter_s:
    print(letter)

# Question 4: Explain a use case for a generator using a yield statement where you would not want to use a normal
# function with a return statement.

# Answer: If you have a really large set of data the you are trying to iterate through
# without consuming too much memory


# Bonus Question:
# gen_com is a method for using  comprehension as you would in list to produce data based on
# defined requirements
