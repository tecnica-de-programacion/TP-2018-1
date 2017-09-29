# import data_song
# import random
#
#
# class House:
#     '''This is an abstraction to reproduce the kids tale "The that house build"'''
#     data = data_song.jack_house_song
#
#     def __init__(self):
#         space_len = len(self.data["init"]) + 1
#         spaces = " " * space_len
#         self.separator = "\n" + spaces
#
#     def phrase(self, lines):
#         '''Return the tale as log as number of lines asked'''
#         if lines <= 0:
#             raw_text = []
#         else:
#             index = -1 * lines
#             raw_text = self.data["lines"][index:]
#         raw_text.append(self.data["end"])
#         tale = self.separator.join(raw_text)
#         return "{} {}".format(self.data["init"], tale)
#
#
# print("***" * 5, "House", "***" * 5)
# jack_house = House()
# print(jack_house.phrase(12))
#
#
# class RandomHouse:
#     '''This is an abstraction to reproduce the kids tale "The that house build" but Random'''
#     data = data_song.jack_house_song
#
#     def __init__(self):
#         space_len = len(self.data["init"]) + 1
#         spaces = " " * space_len
#         self.separator = "\n" + spaces
#
#     def phrase(self, lines):
#         '''Return the tale as log as number of lines asked'''
#         random.shuffle(self.data["lines"])
#         if lines <= 0:
#             raw_text = []
#         else:
#             index = -1 * lines
#             raw_text = self.data["lines"][index:]
#         raw_text.append(self.data["end"])
#         tale = self.separator.join(raw_text)
#         return "{} {}".format(self.data["init"], tale)
#
#
# print("***" * 5, "Random House", "***" * 5)
# random_jack_house = RandomHouse()
# print(random_jack_house.phrase(12))
#
#
# class EcoHouse:
#     '''This is an abstraction to reproduce the kids tale "The that house build" but Random'''
#     data = data_song.jack_house_song
#
#     def __init__(self):
#         space_len = len(self.data["init"]) + 1
#         spaces = " " * space_len
#         self.separator = "\n" + spaces
#
#     def phrase(self, lines):
#         '''Return the tale as log as number of lines asked'''
#         ecoData = list(map(lambda x: x + " " + x, self.data["lines"]))
#         if lines <= 0:
#             raw_text = []
#         else:
#             index = -1 * lines
#             raw_text = ecoData[index:]
#         raw_text.append(self.data["end"])
#         tale = self.separator.join(raw_text)
#         return "{} {}".format(self.data["init"], tale)
#
#
# print("***" * 5, "Eco House", "***" * 5)
# eco_jack_house = EcoHouse()
# print(eco_jack_house.phrase(12))

##################################################################

import data_song
import random
import abc


class Order(abc.ABC):
    @abc.abstractmethod
    def lines(self, data):
        pass


class DefaulrOrder(Order):
    def lines(self, data):
        return data


class RandomOrder(Order):
    def lines(self, data):
        ramdomData = data.copy()
        random.shuffle(ramdomData)
        return ramdomData


class Repeat(abc.ABC):
    @abc.abstractmethod
    def lines(self, data):
        pass


class DefaulrRepeat(Repeat):
    def lines(self, data):
        return data


class EcoRepeat(Repeat):
    def lines(self, data):
        return list(map(lambda x: x + " " + x, data))


class House:
    '''This is an abstraction to reproduce the kids tale "The that house build"'''
    data = data_song.jack_house_song

    def __init__(self, order=DefaulrOrder(), repeat=DefaulrRepeat()):
        self.lines = self.data["lines"]
        self.lines = order.lines(self.lines)
        self.lines = repeat.lines(self.lines)
        space_len = len(self.data["init"]) + 1
        spaces = " " * space_len
        self.separator = "\n" + spaces

    def phrase(self, lines):
        '''Return the tale as log as number of lines asked'''
        if lines <= 0:
            raw_text = []
        else:
            index = -1 * lines
            raw_text = self.lines[index:]
        raw_text.append(self.data["end"])
        tale = self.separator.join(raw_text)
        return "{} {}".format(self.data["init"], tale)


print("***" * 5, "House", "***" * 5)
jack_house = House()
print(jack_house.phrase(12))

print("***" * 5, "Random House", "***" * 5)
random_jack_house = House(order=RandomOrder())
print(random_jack_house.phrase(12))

print("***" * 5, "Eco House", "***" * 5)
eco_jack_house = House(repeat=EcoRepeat())
print(eco_jack_house.phrase(12))

print("***" * 5, "Eco Random House", "***" * 5)
random_eco_jack_house = House(order=RandomOrder(), repeat=EcoRepeat())
print(random_eco_jack_house.phrase(12))

##################################################################
