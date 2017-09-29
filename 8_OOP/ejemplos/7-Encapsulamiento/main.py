
class Dog():
    """This is a representation for a dog´s class"""
    general_tag = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.__set_tag()

    def __set_tag(self):
        print("set tag")
        self.__tag = Dog.general_tag
        Dog.general_tag += 1

    @property
    def tag(self):
        return "{:09}".format(self.__tag)

luky = Dog("luky", "Chihuahua")
chachis = Dog("chachis", "Chihuahua")
print(luky.tag)
print(chachis.tag)

print(luky.__tag)
print(chachis.__tag)
luky.__set_tag()
chachis.__set_tag()