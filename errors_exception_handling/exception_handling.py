"""This program covers the topic of
exception handling in Python"""


# The three keyword that are used when doing exception handling are "try", "except" and "finally".

def add(n1, n2):
    print(n1 + n2)


add(10, 20)

number1 = 10
number2 = input("Please enter a number:")  # Produces an error. Adding an integer and a string
add(number1, number2)
print("Something happened!")  # This will  never print

try:
    # want to attempt this code
    # may have an error
    result = 10 + 10  # Will produce an error if you use something other than int
    # print(result)
except:
    print("Hey it looks like you aren't adding correctly!")
else:  # Execute if everything id ok eith thr code
    print("ADD WENT WELL!")
    print(result)

try:
    f = open('testfile', 'r')
    f.write("Write a test line")
except TypeError:
    print("There was a type of error")
except OSError:
    print("Ypu have an OS Error")
except:
    print("All other exceptions")
finally:
    print("I always run")


def ask_for_int():
    try:
        result = int(input("Enter an integer"))
    except:
        print("Whoops! That is not a number")
    finally:
        print("End of try/Ecept/finally")


ask_for_int()


# Below ill be a try block in a while loop
# With using while loops, you also need to use a break statement to break out of the loop
def ask_for_int2():
    while True:
        try:
            result = int(input("Please enter a number:"))
            print(result)
        except:
            print("Whoops! That is not a number ")
            continue
        else:
            print("Yes, thank you!")
            break
        finally:
            print("End of try/except/finally")


ask_for_int2()


def ask_for_int3():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end")


ask_for_int3()
