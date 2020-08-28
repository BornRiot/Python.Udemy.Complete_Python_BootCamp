# python one.py
print('hello')


def my_func():
    print("Something")


# Demonstrates the use  the __name__ and __main__  for running
# python code


def func1():
    print("FUNC() IN ONE.PY")


print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
    my_func()
    print("One is being ran directly")
else:
    print("ONE.PY IS BEING IMPORTED")
