from tkinter import Tk
from Views.ResultLabel import ResultLabel
from Views.KeypadView import KeypadView, CalcButton

class MainView(Tk):
    class Constants:
        title = "Calculator"
        heigth = 475
        width = 300

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.__configure_ui()
        self.__configure_grid()

    def __configure_ui(self):
        self.__result_label = ResultLabel(self)
        self.__result_label.position(0, 0)

        self.__keypad  = KeypadView(self)

    def __configure_grid(self):
        self.grid_rowconfigure(0, minsize=ResultLabel.Constants.size)

        for row_index in range(1,KeypadView.Constants.heigth + 1):
            self.grid_rowconfigure(row_index, minsize = CalcButton.Constants.size, weight = True)

        for column_index in range(KeypadView.Constants.width):
            self.grid_columnconfigure(column_index, minsize = CalcButton.Constants.size, weight = True)

