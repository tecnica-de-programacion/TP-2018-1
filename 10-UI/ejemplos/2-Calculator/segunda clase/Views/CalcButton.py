from tkinter import Label, W, E, N, S
from Helpers.CustomTypes import Number, BinaryOperator, UnaryOperator
from enum import Enum

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

        self.bind(self.Events.click, self.__did_tap)

    def position(self, row, column):
        self.grid(row = row, column = column, sticky = self.Constants.center)

    def __did_tap(self, event):
        if self.__action is None: return
        self.__action(self.key)
