from tkinter import Label, N, S, E, W

class ResultLabel(Label):
    class Constants:
        size = 100
        border_type = 'flat'
        border_width = 1
        font_family = "Quicksand"
        font_size = 68
        bg = '#202020'
        foreground = '#FFFFFF'
        initial_value = "0"
        center = W + E + N + S
        rigth = E
        span = 4

    def __init__(self, master):
        super().__init__(master)
        self.configure(text="0")
        self.configure(bg = self.Constants.bg)
        self.configure(foreground = self.Constants.foreground)
        self.configure(font = (self.Constants.font_family, self.Constants.font_size), anchor = self.Constants.rigth)

    def position(self, row, colum):
        self.grid(row = row, column = colum, sticky=self.Constants.center, columnspan = self.Constants.span)

