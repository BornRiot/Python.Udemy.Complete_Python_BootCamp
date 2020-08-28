# Question 1
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except:
      print("The operation of raising a letter to a certain power is not supported")



    # Question 2
def func1():
    x = 5
    y = 0
    try:
        z = x/y
        return z
    except:
        print("Cannot divide by zero")
    finally:
        print("All Done")

answer = func1()
answer


# Quedtion 3
def ask():
    while True:
        try:
            number = int(input("Inout an Integer:"))
            result = number**2

        except:
            print("An error occurred! Please try again!")
            continue
        else:
            print("Thank you, your number squared is: {0}".format(result))
            break

ask()

