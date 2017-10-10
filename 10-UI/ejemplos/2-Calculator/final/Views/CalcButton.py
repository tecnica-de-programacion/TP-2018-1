from tkinter import Label, W, E, N, S
from Helpers.CustomeTypes import Number, BinaryOperator, UnaryOperator
from enum import Enum

class CalcButtonType(Enum):
    BINARY = ('#F7901D', '#FFFFFF')
    UNARY = ('#C3C4C6', '#202020')
    NUMBER = ('#CFD1D3', '#202020')

class CalcButton(Label):
    class Constants:
        size = 75
        border_type = 'groove'
        selected_border_type = 'solid'
        border_width = 1
        center = W + E + N + S
        font = ("Quicksand", 28)

    class Events:
        rigthClick = '<Button-1>'

    def __init__(self, master, key_type, action = None):
        super().__init__(master)
        self.__action = action
        self.key = key_type
        self.configure(text = key_type.value)
        self.configure(font=self.Constants.font)
        bg, foreground = self.__get_color(key_type)
        self.configure(bg = bg, foreground = foreground)
        self.configure(borderwidth = self.Constants.border_width, relief = self.Constants.border_type)
        self.bind(self.Events.rigthClick, self.__did_tap)

    def position(self, row, colum, span):
        self.grid(row = row, column = colum, columnspan=span, sticky = self.Constants.center)

    def __get_color(self, key_type):
        if isinstance(key_type, Number):
            return CalcButtonType.NUMBER.value
        elif isinstance(key_type, BinaryOperator) or key_type == UnaryOperator.EQUAL:
            return CalcButtonType.BINARY.value
        else:
            return CalcButtonType.UNARY.value

    def __did_tap(self, event):
        if self.__action is None:
            return
        self.__action(self.key)

    # def select(self):
    #     self.configure(borderwidth = self.Constants.border_width, relief = self.Constants.selected_border_type)
    #
    # def unselect(self):
    #     self.configure(borderwidth = self.Constants.border_width, relief = self.Constants.border_type)

