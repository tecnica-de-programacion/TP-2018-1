from Views.MainView import MainView
from Models.Currency import Currency

class MainApp():
    def __init__(self):
        self.__master = MainView(convert_handler = self.__convert)

    def run(self):
        self.__currency = Currency("USD", 18.90)
        self.__master.mainloop()

    def __convert(self, from_currency, to_currency, ammount):
        result = self.__currency.get_convertion(to_currency, ammount)
        self.__master.update_result(result)

if __name__ == "__main__":
    app = MainApp()
    app.run()


