"""
This module documents the definition and how to use
decorators in a python program.
"""
# Python has decorators which allow users to tack on extra functionality
# to an already existing function. It uses the @ operator to do so.

# manually buidling out a decorator function:
def func():
    return 1

print(func) #return function position
print(func()) # return value output of function

def hello():
    return "Hello!"

print(hello())
print(hello)

#assign hello function to variable:
greet = hello
print(greet())
del hello
print(greet()) #greet will still return hello because it is pointing
# to the function object



print('New Topic begins here: ')
def hello(name ='Jose'):
    print('The hello() has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is welcome() inside hello'
    print(greet())
    print(welcome())
    print('This is the end of the hello function!')

hello()

# re-write  of the hello() function that returns another function:
print("rewirte begins here:")
def hello(name ='Jose'):
    print('The hello() has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is welcome() inside hello'

    print('I am going to return a function!')
    if name == 'Jose':
        return greet
    else:
        return hello
my_new_func = hello()
print(my_new_func())


print('New function begins here:')
def cool():
    def super_cool():
        return  'I am very cool'

    return super_cool

some_func = cool()
print(some_func())

print('New Topic begins below this line:')
#Passing in functions:
def hello():
    return 'Hi Jose!'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())
other(hello)

print('Example of how to use decorators  begins below this line')
def new_decorator(original_func):

    def wrap_func(original_func):
        print('Some extra code, before the original function ')
        original_func()
        print('Some extra code, after the original function ')
    return wrap_func

def func_needs_decorator():
    print('I want to be decorated!')
func_needs_decorator()
decorated_func = new_decorator(func_needs_decorator) #Code has to be written
# like this in order to be executed
decorated_func(func_needs_decorator)

print('Using the @ symbol')
@new_decorator
def func_needs_decorator2(some):
    print('I want to be decorated')
func_needs_decorator2(func_needs_decorator)
