"""
This module holds the ran_check function that corresponds to
the challenge question
"""

def ran_check(num, low, high):
    """
    This is the function that is used to solve the ran_check challenge
    """
    return num in range(low, high+1)

print(ran_check(4,1,9))


# for i in range(0,6+1):
#     print(i)
