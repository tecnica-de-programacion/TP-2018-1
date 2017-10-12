from tkinter import Tk, Canvas, ALL
from enum import Enum

class MainView(Tk):
    class Constants:
        title = "Pizarra Magica"
        heigth = 400
        width = 500

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

        space = "space"

    class Events(Enum):
        DRAG = "<B1-Motion>"
        PRESS = "<Button-1>"
        KEYPRESS = "<Key>"

    def __init__(self, start_handler = None, motion_handler = None, space_handler = None):
        super().__init__()
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())
        self.minsize(self.Constants.width, self.Constants.heigth)
        self.__configure_ui()
        self.__configure_grid()
        self.start_handler = start_handler
        self.motion_handler = motion_handler
        self.space_handler = space_handler


    def __configure_ui(self):
        self.__canvas = Canvas(self, width = self.Constants.width, height = self.Constants.heigth)
        self.__canvas.bind(self.Events.PRESS.value, self.__press)
        self.__canvas.bind(self.Events.DRAG.value, self.__motion)
        self.__canvas.bind(self.Events.KEYPRESS.value, self.__key)
        self.__canvas.focus_set()
        self.__canvas.grid(row = 0, column = 0)

    def __configure_grid(self):
        self.grid_columnconfigure(0, weight = True)
        self.grid_rowconfigure(0, weight = True)

    def draw_line(self, x1, y1, x2, y2):
        self.__canvas.create_line(x1, y1, x2, y2, fill="red")

    def clean(self):
        self.__canvas.delete(ALL)

    def __motion(self, event):
        if self.motion_handler is None: return
        self.motion_handler(event)

    def __press(self, event):
        if self.start_handler is None: return
        self.start_handler(event)

    def __key(self, event):
        if self.space_handler is None: return
        if  event.keysym == self.Constants.space:
            self.space_handler()