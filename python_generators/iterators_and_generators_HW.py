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
num = random.randint(1, 10)


def rand_num(low, high, n):
    for n in range(n):
        yield n
