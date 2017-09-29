class Dog ():
    pass

firulais = Dog()
firulais.name = "firulais"
firulais.breed = "labrador"

def bark() :
    print("guarfffff!")

print(firulais.name)
print(firulais.breed)
firulais.bark

#################

class Dog():
    """This is a representation for a dog´s class"""

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def run(self):
        print(self.name, "is runing")

    def bark(self):
        print("guarf!")


luky = Dog("luky", "Chihuahua")
luky.run()
luky.bark()
Dog.bark(luky)

spike = Dog("spike", "Golden")
spike.run()
spike.bark()

