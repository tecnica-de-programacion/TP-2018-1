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
        bottom_left = E
        span = 4

    def __init__(self, master):
        super().__init__(master)
        self.configure(text="0")
        self.configure(bg = self.Constants.bg)
        self.configure(foreground = self.Constants.foreground)
        self.grid(row=0, column=0, sticky= self.Constants.center)


