""" This program covers the topic and use of the Python debugger """
# More info on the python debugger and documentation can be found online and in the jupyter notebooks
# link to documentation: https://bit.ly/3bkFjax
import pdb

x = [1, 3, 4]
y = 2
z = 3
result = y + z
print(result)

pdb.set_trace()
result2 = y + x
print(result2)
