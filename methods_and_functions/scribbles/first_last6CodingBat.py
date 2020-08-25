
def check_for_vowel(word):
    vowels = ['a','e','i','o','u']
    u_vowels = ['A','E','I','O','U']
    first_letter = word[0]
    if first_letter in vowels or first_letter in u_vowels:
        return True

def first_last6(nums):
    first_ind = nums[0]
    last_num = nums.pop()
    return last_num
print(first_last6([2,5,7,9]))

print(check_for_vowel("Asbestos"))
