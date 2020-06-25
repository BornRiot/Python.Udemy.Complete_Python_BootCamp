"""
This module is used to sole the count primes challenge
"""
def count_primes_c(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


def count_primes(num):
    count = 0
    for val in range(0, num + 1):
        if val > 1:
            for n in range(2, val//2 + 2):
                if (val % n) == 0:
                    break
                else:
                    if n == val//2 + 1:
                        count += 1
                        print(val)
    print("The number of primes are: ", count)

count_primes(100)
print("Ths is the correct answer")
print(count_primes_c(100))
