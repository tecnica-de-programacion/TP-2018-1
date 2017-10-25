class Currency:
    def __init__(self, name, rate):
        self.__name = name
        self.__rate = rate

    @property
    def name(self):
        return self.__name

    def get_convertion(self, currency, ammount):
        return ammount * self.__rate
