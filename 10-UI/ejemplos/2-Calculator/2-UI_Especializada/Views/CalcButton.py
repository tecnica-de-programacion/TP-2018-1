from tkinter import Label, W, E, N, S
from enum import Enum

class CalcButtonType(Enum):
    OPERATION = ('#F7901D', '#FFFFFF')
    ACTION = ('#C3C4C6', '#202020')
    NUMBER = ('#CFD1D3', '#202020')

class CalcButton(Label):
    class Constants:
        size = 75
        border_type = 'groove'
        border_width = 1
        center = W + E + N + S
        font = ("Quicksand", 28)

    class Events:
        rigthClick = '<Button-1>'

    def __init__(self, mainView, text, action):
        super().__init__(mainView)
        self.id = text
        self.configure(text = text)
        self.__set_color(text)
        self.configure(font = self.Constants.font)
        self.configure(borderwidth = self.Constants.border_width, relief = self.Constants.border_type)
        self.bind(self.Events.rigthClick, lambda event, b = self: action(event, b))

    def position(self, row, colum, span):
        self.grid(row = row, column = colum, columnspan = span, sticky = self.Constants.center)

    def __set_color(self, text):
        if text in "1234567890.":
            bg, foreground = CalcButtonType.NUMBER.value
        elif text in "/x-+=":
            bg, foreground = CalcButtonType.OPERATION.value
        else:
            bg, foreground = CalcButtonType.ACTION.value
        print(bg, foreground)
        self.configure(bg = bg, foreground = foreground)
        




    