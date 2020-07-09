"""
This module is used to solve the multiply challenge in the
Functions and Methods Homework.
"""
#temp_hold = numbers[v]*numbers[v+1]

def multiply(numbers):
    total = 1
    for v in numbers:
        total *= v
        print(total)




print(multiply([1, 2, 3, -4]))
