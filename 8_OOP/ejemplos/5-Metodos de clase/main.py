class Dog():
    """This is a representation for a dog´s class"""
    general_tag = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tag = Dog.general_tag
        Dog.general_tag += 1
        self.info = "Name: {}, Breed: {}, Tag: {:09}".format(self.name, self.breed, self.tag)

    @classmethod
    def total_tags(cls):
        print("Number of dogs:", cls.general_tag)


class DogsCataloger():
    @staticmethod
    def catalog_breed(dogs_list):
        catalog = {}
        for dog in dogs_list:
            if catalog.get(dog.breed, None):
                catalog[dog.breed] += 1
            else:
                catalog[dog.breed] = 1
        return catalog


luky = Dog("luky", "Chihuahua")
print(luky.info)

spike = Dog("spike", "Golden")
print(spike.info)

Dog.total_tags()

dogs = [luky, spike]
print(DogsCataloger.catalog_breed(dogs))
