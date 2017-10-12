from Views.MainView import MainView
from Helpers.CustomTypes import Number, BinaryOperator, UnaryOperator

class MainApp():

    def __init__(self):
        self.__master = MainView(tap_number_handler = self.__did_number_tapped, tap_operator_handler = self.__did_operator_tapped)

        self.__display_text = "0"
        self.__display_number = 0
        self.__is_typing_number = True
        self.__master.display(self.__display_text)

    def run(self):
        self.__master.mainloop()

    def __did_number_tapped(self, number):
        if self.__is_typing_number:
            self.__display_text = number.value if self.__display_text == Number.ZERO.value else self.__display_text + number.value
        else:
            self.__display_number = float(self.__display_text)
            self.__display_text = number.value
            self.__is_typing_number = True
        self.__update_diplay()

    def __did_operator_tapped(self, operator):
        if operator == UnaryOperator.DOT:
            self.__add_dot()
        else:
            self.__is_typing_number = False

    def __update_diplay(self):
        self.__master.display(self.__display_text)

    def __add_dot(self):
        if UnaryOperator.DOT.value in self.__display_text:
            return
        self.__display_text += UnaryOperator.DOT.value
        self.__update_diplay()

if __name__ == "__main__":
    app = MainApp()
    app.run()