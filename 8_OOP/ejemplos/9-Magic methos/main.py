class Dog():
    """This is a representation for a dog´s class"""
    general_tag = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tag = Dog.general_tag
        Dog.general_tag += 1

    def __repr__(self):
        return "Dog({}, {})".format(self.name, self.breed)

    def __str__(self):
        return "Name: {}, Breed: {}, Tag: {:09}".format(self.name, self.breed, self.tag)

    def __add__(self, other):
        return [self, other]


luky = Dog("luky", "Chihuahua")
pedro = Dog("pedro", "Chihuahua")
print(luky)
print(luky.__repr__())

print(1 + 2)
print(int.__add__(1, 2))

print(luky + pedro)

