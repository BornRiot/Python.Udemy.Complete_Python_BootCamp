def makes_twenty(n1,n2):
    """My attempt"""
    if n1 == 20 or n2 == 20 :
        return True
    elif n1 + n2 == 20:
        return True
    else:
        return False

def makes_twenty_c(n1,n2):
    """Correct answer"""
    return (n1+n2)==20 or n1==20 or n2==20


print(makes_twenty(10,11))
print("This is the correct answer:")
print(makes_twenty_c(10,11))
