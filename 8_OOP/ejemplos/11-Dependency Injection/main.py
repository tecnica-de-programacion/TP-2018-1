# class Car:
#     def __init__(self, dors, fuel_tank, performance, type = "gasoline"):
#         self.dors = dors
#         self.__isEngeeneOn = False
#         self.__fuel_tank = fuel_tank
#         self.__performance = performance
#         self.__fuel = 0
#         self.type = type
#
#     @property
#     def isOn(self):
#         return self._isEngeeneOn
#
#     @property
#     def fuel_tank_level(self):
#         return (100 * self.__fuel) / self.__fuel_tank
#
#     def turn_on(self):
#         self.__isEngeeneOn = True
#
#     def turn_off(self):
#         self.__isEngeeneOn = False
#
#     def charge_full(self, liters):
#         self.__fuel = self.__fuel + liters
#
#     def drive(self, kilometers):
#         self.__fuel -= kilometers / self.__performance

#########################################################################

# class GasolineEngeen:
#     def __init__(self, fuel_tank, performance):
#         self.__isOn = False
#         self.__fuel_tank = fuel_tank
#         self.__performance = performance
#         self.__fuel = 0
#         self.fuel_type = "gasoline"
#
#     @property
#     def isOn(self):
#         return self.__isOn
#
#     def turn_on(self):
#         self.__isOn = True
#
#     def turn_off(self):
#         self.__isOn = False
#
#     @property
#     def fuel_tank_level(self):
#         return (100 * self.__fuel) / self.__fuel_tank
#
#     def charge_full(self, liters):
#         self.__fuel += liters
#
#     def drive(self, kilometers):
#         self.__fuel -= kilometers / self.__performance
#
#
# class ElectricEngeen():
#     def __init__(self, performance):
#         self.__isOn = False
#         self.__performance = performance
#         self.__baterry_charge = 0
#         self.type = "electric"
#
#     @property
#     def isOn(self):
#         return self.__isOn
#
#     def turn_on(self):
#         self.__isOn = True
#
#     def turn_off(self):
#         self.__isOn = False
#
#     @property
#     def fuel_tank_level(self):
#         return self.__baterry_charge
#
#     def charge_full(self, time):
#         self.__baterry_charge += time
#
#     def drive(self, kilometers):
#         self.__fuel -= kilometers / self.__performance
#
# class Car:
#     def __init__(self, color, dors, engeen):
#         self.dors = dors
#         self.color = color
#         self.engeen = engeen
#
#     @property
#     def isOn(self):
#         return self.engeen.isOn
#
#     @property
#     def fuel_tank_level(self):
#         return self.engeen.fuel_tank_level
#
#     def turn_on(self):
#         self.engeen.turn_on()
#
#     def turn_off(self):
#         self.engeen.turn_off()
#
#     def charge_full(self, liters):
#         self.engeen.charge_full(liters)
#
#     def drive(self, kilometers):
#         self.engeen.drive(kilometers)
#
# electric_engeen = ElectricEngeen(10)
# engeen = GasolineEngeen(60, 12)
#
# electric_red = Car("red", 4, electric_engeen)
# electric_blue = Car("blue", 2, electric_engeen)
# gasoline_blue = Car("blue", 2, engeen)
#
# gasoline_blue.turn_on()
# print(gasoline_blue.isOn)


#########################################################################
import abc
class Engeen(abc.ABC):
    __isOn = False

    @property
    def isOn(self):
        return self.__isOn

    def turn_on(self):
        self.__isOn = True

    def turn_off(self):
        self.__isOn = False

    @abc.abstractmethod
    def fuel_tank_level(self):
        pass

    @abc.abstractmethod
    def charge_full(self, time):
        pass

    @abc.abstractmethod
    def drive(self, kilometers):
        pass

class GasolineEngeen(Engeen):
    def __init__(self, fuel_tank, performance):
        self.__fuel_tank = fuel_tank
        self.__performance = performance
        self.__fuel = 0
        self.fuel_type = "gasoline"

    @property
    def fuel_tank_level(self):
        return (100 * self.__fuel) / self.__fuel_tank

    def charge_full(self, liters):
        self.__fuel += liters

    def drive(self, kilometers):
        self.__fuel -= kilometers / self.__performance


class ElectricEngeen(Engeen):
    def __init__(self, performance):
        self.__performance = performance
        self.__baterry_charge = 0
        self.type = "electric"

    @property
    def fuel_tank_level(self):
        return self.__baterry_charge

    def charge_full(self, time):
        self.__baterry_charge += time

    def drive(self, kilometers):
        self.__fuel -= kilometers / self.__performance

class Car:
    def __init__(self, color, dors, engeen):
        self.dors = dors
        self.color = color
        if isinstance(engeen, Engeen):
            self.engeen = engeen
        else:
            raise ValueError('Not Valid Engeen')

    @property
    def isOn(self):
        return self.engeen.isOn

    @property
    def fuel_tank_level(self):
        return self.engeen.fuel_tank_level

    def turn_on(self):
        self.engeen.turn_on()

    def turn_off(self):
        self.engeen.turn_off()

    def charge_full(self, liters):
        self.engeen.charge_full(liters)

    def drive(self, kilometers):
        self.engeen.drive(kilometers)

electric_engeen = ElectricEngeen(10)
engeen = GasolineEngeen(60, 12)

electric_red = Car("red", 4, electric_engeen)
electric_blue = Car("blue", 2, electric_engeen)
gasoline_blue = Car("blue", 2, engeen)

gasoline_blue.turn_on()
print(gasoline_blue.isOn)

disel = Car("blue", 2, "disel")
