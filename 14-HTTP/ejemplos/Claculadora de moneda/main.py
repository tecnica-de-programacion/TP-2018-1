from Views.MainView import MainView
from Models.CurrencyManager import CurrencyManager

class MainApp():
    def __init__(self):
        self.__master = MainView(convert_handler = self.__convert)

    def run(self):
        self.__currency = CurrencyManager.get_currency_data("USD")
        self.__master.mainloop()

    def __convert(self, from_currency, to_currency, ammount):
        result = self.__currency.get_convertion(to_currency, ammount)
        self.__master.update_result(result)

if __name__ == "__main__":
    app = MainApp()
    app.run()


