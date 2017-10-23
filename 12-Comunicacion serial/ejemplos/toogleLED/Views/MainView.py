from tkinter import Tk, N, S, E, W
from Views.ToggleButton import ToggleButton

class MainView(Tk):
    class Constants:
        title = "Toggle Led"
        heigth = 300
        width = 300
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self, tap_handler = None):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.__toogle = ToggleButton(self, tap_toggle_handler = tap_handler)
        self.__toogle.grid(row=0, column=0, sticky = self.Constants.center)

        self.grid_rowconfigure(0, weight=True)
        self.grid_columnconfigure(0, weight=True)
