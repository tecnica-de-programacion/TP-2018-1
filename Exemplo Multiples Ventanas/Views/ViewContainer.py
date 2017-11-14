from tkinter import Tk, Frame, N, S, E, W

class ViewContainer(Tk):
    class Constants:
        center = N + S + E + W

    def __init__(self):
        super().__init__()
        self.__container = Frame(self)
        self.__container.pack()
        self.__container.grid_rowconfigure(0, weight=1)
        self.__container.grid_columnconfigure(0, weight=1)

    @property
    def container (self):
        return self.__container

    def set_views (self, views):
        for views in views:
            views.grid(row=0, column=0, sticky= self.Constants.center)
