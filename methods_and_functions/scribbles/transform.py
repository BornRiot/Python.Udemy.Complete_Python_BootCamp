"""This is my module docstring"""
# https://bit.ly/2CiRBog
the_list = [1,3,5,7,9,11,13,15,17,19,21]
the_tuple = tuple(the_list)
y = list(enumerate(the_tuple))
print("Here is Y:", y)
print(the_tuple)
for i, v in enumerate(the_tuple):
    print("Here is the non enumerate", the_tuple[i])
print(type(the_tuple))
print(the_tuple)
