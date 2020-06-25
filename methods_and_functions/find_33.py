"""This is my module docstirng"""

def has_33_c(nums):
    """correct answer"""
    for i in range(0, len(nums)-1):

        # nicer looking alternative in commented code
        #if nums[i] == 3 and nums[i+1] == 3:

        if nums[i:i+2] == [3,3]:
            return True

    return False

def has_33(the_list):
    """this is my answer"""
    some_list = [3, 3]
    return set(some_list).issubset(set(the_list))

print(has_33([6, 3, 3]))
print("this is the correct answer:")
print(has_33_c([6, 3, 3]))
