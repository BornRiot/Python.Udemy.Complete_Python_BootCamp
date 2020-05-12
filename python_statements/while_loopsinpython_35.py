# Syntax for while loop:
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1  # can be shortened to x += 1

else:
    print('X is not less than 5')

x = [1, 2, 3]
for item in x:
    # comment: something has to be here to continue
    pass
print('end of my script')

my_string = 'Sammy'
for letter in my_string:
    print(letter)
    print('Stop')

the_newString = 'Sammy '
for letter in the_newString:
    if letter == 'a':
        continue
    print(letter)

    the_3String = 'Sammy'
    for ketter in the_3String:
        if letter == 'a':
            break
        print(ketter)

x = 0
# find more examples of the break, continue and pass keywords in  python
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
# = 50
# while x < 5
# print(f'The current value of x is {x} )
# x += 1
