from tkinter import Label, W, E, N, S
import locale

class ResultLabel(Label):
    class Constants:
        size = 100
        border_type = 'flat'
        border_width = 1
        font = ("Quicksand", 40)
        bg, foreground = ('#202020', '#FFFFFF')
        initial_value = "0"
        center = W + E + N + S
        bottom_left = S + E
        span = 4

    def __init__(self, mainView):
        super().__init__(mainView)
        self.__value = 0
        self.configure(text = self.Constants.initial_value)
        self.configure(font = self.Constants.font, anchor= self.Constants.bottom_left)
        self.configure(bg = self.Constants.bg, foreground = self.Constants.foreground)
        self.configure(borderwidth = self.Constants.border_width, relief = self.Constants.border_type)
        self.value = 10000000

    def position(self, row, colum):
        self.grid(row = row, column = colum, columnspan = self.Constants.span, sticky = self.Constants.center)

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, number):
        self.__value = number
        locale.setlocale(locale.LC_ALL, 'en_US')
        self.configure(text = locale.format('%d', self.__value, grouping=True))
        




    