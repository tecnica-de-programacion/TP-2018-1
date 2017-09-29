class Dog():
    """This is a representation for a dog´s class"""

    sound = "guarf!"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def run(self):
        print(self.name, "is runing")

    def bark(self):
        print("****" * 5)
        print(self.sound)
        print(Dog.sound)


luky = Dog("luky", "Chihuahua")
luky.run()
luky.bark()
Dog.bark(luky)

spike = Dog("spike", "Golden")
spike.run()
spike.sound = "guarffffffffffff!"
spike.bark()

Dog.sound = "guauuuu!"
spike.bark()