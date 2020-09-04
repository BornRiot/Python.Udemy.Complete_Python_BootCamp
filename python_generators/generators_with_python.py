def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result


def create_cubes2(n):
    for z in range(n):
        yield z ** 3


print(create_cubes(10))
for x in create_cubes(10):
    print(x)

# Instead of having the entire list stored in memory Python Generators can be used to
# Send back a single value and then later resume to pick up  where it  left off
# It allows the process of generating a sequence over time instead holding it all at once
for b in create_cubes2(10):  # This allows for more memory efficiency
    print(b)


# Create Fibonacci sequence using generators
def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


print("Fibonacci sequence  begins ")
for number in gen_fibon(10):
    print(number)


# The key to understanding generators id through the next function and the iter function
def simple_gen():
    for x in range(3):
        yield x


for num in simple_gen():
    print(num)

# Assign simple_gen() to a variable
g = simple_gen()
print(g)
print(next(g))  # print next value in g simple_generator
print(next(g))  # print the next value after that

# Demonstrate the use of iter to iterate over sequential objects
d = 'hello'
# next(d) will produce an error warning that d is not an iterator
# to solve the problem use the iter function
d_iter = iter(d)
print(next(d_iter))
