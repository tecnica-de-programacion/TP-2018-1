from tkinter import Frame, Label, Button
from CostomeType.View import View

class ViewOne(Frame):
    def __init__(self, parent, change_view_hadler = None):
        super().__init__(parent)
        self.__change_view_hadler = change_view_hadler
        label = Label(self, text="Page One!!!")
        label.pack(pady=10, padx=10)

        button1 = Button(self, text="Back to Home",
                            command=lambda: self.__did_tap_change_button(View.Start))
        button1.pack()

        button2 = Button(self, text="Page Two",
                            command=lambda: self.__did_tap_change_button(View.Two))
        button2.pack()

    def __did_tap_change_button(self, view):
        if self.__change_view_hadler is None:
            return
        self.__change_view_hadler(view)