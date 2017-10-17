from tkinter import Label, W, E, N, S
from Helpers.CustomTypes import Number, BinaryOperator, UnaryOperator
from enum import Enum

class CalcButtonType(Enum):
    BINARY = ('#F7901D', '#FFFFFF')
    UNARY = ('#C3C4C6', '#202020')
    NUMBER = ('#CFD1D3', '#202020')

class CalcButton(Label):
    class Constants:
        size = 75
        border_type = 'groove'
        border_width = 1
        center = W + E + N + S
        font = ("Quicksand", 28)

    class Events:
        click = "<Button-1>"

    def __init__(self, master, key_type, action = None):
        super().__init__(master)
        self.key = key_type
        self.__action = action
        self.configure(text = self.key.value)
        self.configure(font = self.Constants.font)
        self.configure(borderwidth = self.Constants.border_width, relief = self.Constants.border_type)
        bg, foreground = self.__get_color(key_type)
        self.configure(bg = bg, foreground = foreground)

        self.bind(self.Events.click, self.__did_tap)

    def position(self, row, column, columnspan = 1):
        self.grid(row = row, column = column, columnspan = columnspan, sticky = self.Constants.center)

    def __did_tap(self, event):
        if self.__action is None: return
        self.__action(self.key)

    def __get_color(self, key_type):
        if isinstance(key_type, Number):
            return CalcButtonType.NUMBER.value
        elif isinstance(key_type, BinaryOperator):
            return CalcButtonType.BINARY.value
        elif key_type == UnaryOperator.EQUAL:
            return CalcButtonType.BINARY.value
        elif key_type == UnaryOperator.DOT:
            return CalcButtonType.NUMBER.value
        else:
            return CalcButtonType.UNARY.value