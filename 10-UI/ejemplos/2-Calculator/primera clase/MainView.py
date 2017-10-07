from tkinter import Tk
from ResultLabel import ResultLabel

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

    def __configure_ui(self):
        self.__result_label = ResultLabel(self)

        self.grid_rowconfigure(0, minsize = ResultLabel.Constants.size)
        self.grid_columnconfigure(0, minsize = self.Constants.width)

