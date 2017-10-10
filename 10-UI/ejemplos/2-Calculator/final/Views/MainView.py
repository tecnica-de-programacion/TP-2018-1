from tkinter import Tk
from Views.ResultLabel import ResultLabel
from Views.KeypadView import KeypadView
from Views.CalcButton import CalcButton
from Views.KeypadView import KeypadView

class MainView(Tk):
    class Constants:
        title = "Calculator"
        heigth = 475
        width = 300

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self, tap_number_handler = None, tap_operator_handler = None):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.width, self.Constants.heigth)
        self.__configure_ui(tap_number_handler, tap_operator_handler)
        self.__configure_grid()

    def __configure_ui(self, tap_number_handler, tap_operator_handler):
        self.__result_label = ResultLabel(self)
        self.__result_label.position(0, 0)
        self.__keypad = KeypadView(self, tap_number_handler = tap_number_handler, tap_operator_handler = tap_operator_handler)

    def __configure_grid(self):
        self.grid_rowconfigure(0, weight = True, minsize = ResultLabel.Constants.size)
        for row_index in range(1, KeypadView.Constants.heigth + 1):
            self.grid_rowconfigure(row_index, weight = True, minsize = CalcButton.Constants.size)

        for column_index in range(KeypadView.Constants.width):
            self.grid_columnconfigure(column_index, weight = True, minsize = CalcButton.Constants.size)

    def display(self, value):
        self.__result_label.value(value)





