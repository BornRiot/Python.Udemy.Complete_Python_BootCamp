"""
This module is used to document the example given in the lecture video on how to approach
the challenge with regards to being able to affect methods by calling attributes
"""


class Simple:
    def __init__(self, value):
        self.value = value

    def add_to_value(self, amount):
        self.value = self.value + amount


obj1 = Simple(400)
print(obj1.value)
obj1.add_to_value(600)
print(obj1.value)
