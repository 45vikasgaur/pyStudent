class Animals:
    pass

class pets(Animals):
    pass

class Dog(pets):
    @property
    def bark(self):
        print("Bow Bow!")

d = Dog()
d.bark



