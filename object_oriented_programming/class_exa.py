class MyClass:
    "This is my second class"
    a = 10

    def func(self):
        print('Hello')

the_val = input("What is the value")
# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)
print("this is a line of code")
