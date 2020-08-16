class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof"

    def eat(self):
        self.speak()


first_Dog = Dog("Mike")
first_Dog.speak()
