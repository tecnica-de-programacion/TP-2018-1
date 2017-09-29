class Dog():
    """This is a representation for a dog´s class"""
    sound = "guarf!"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.sound)


class GuideDog():
    """This is a representation for a guide dog´s class"""

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.sound)

    def guide(self):
        print("is guiding")

###############################################################

class Dog():
    """This is a representation for a dog´s class"""
    sound = "guarf!"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.sound)

class GuideDog(Dog) :
    """This is a representation for a guide dog´s class"""

    def __init__(self, name, breed):
        super().__init__(name, breed)

    def guide(self):
        print("is guiding")

class DrugsDog(Dog):

    def __init__(self, name, breed):
        super().__init__(name, breed)
        self.sound = "guaau guaaaau drugs"

    def find_drugs(self, theres_drugs):
        print("looking for drogs")
        if theres_drugs:
            self.bark()
        else:
            print("no drugs")

porfirio = GuideDog("porfirio", "malamut")
porfirio.bark()
print(porfirio.name, porfirio.breed)
porfirio.guide()

luky = Dog("luky", "labrador")

print(isinstance(porfirio, GuideDog))
print(isinstance(porfirio, Dog))

print(isinstance(luky, GuideDog))
print(isinstance(luky, Dog))

k9 = DrugsDog("k9", "german shepard")
k9.bark()
k9.find_drugs(True)
k9.find_drugs(False)
