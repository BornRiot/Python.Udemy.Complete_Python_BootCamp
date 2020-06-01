"""My module docstring """
some_string = "The sTirng"

my_list = [x for x in some_string]
for x in my_list:
    if x.__eq__(" "):
        my_list = my_list.pop(x.index(" "))
print(my_list)
print("This is an update to test Sublime Merge Pull Request")
print("Register new branch")
print("this is a change to the file")
print("This is just some more changes  ")