def lesser_of_two_evens(a,b):
    """My attempt of challenge"""
    if a % 2 != 0 or b % 2 != 0:
        if a > b:
            return a
        elif b > a:
            return b
    elif a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        elif b < a:
            return b

def lesser_of_two_evens_c(a,b):
    """Correct answer"""
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_evens(20,30))
print("this is the correct answer:")
print(lesser_of_two_evens(20,30))
