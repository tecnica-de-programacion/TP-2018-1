from tkinter import Tk, Frame, Label, Button, W, E, S, N, BOTH, Y, X, LEFT

class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("counter")
        self.geometry("300x300")
        self.__counter = 0
        self.configure_ui()
    
    def configure_ui(self):
        self.__more_button = Button(self, text="+", command = self.__add)
        self.__less_button = Button(self, text="-", command = self.__less)
        self.__counter_label = Label(self, bg= "red")
        self.__set_counter()

        # self.__more_button.pack(side=LEFT, fill=BOTH, expand=True)
        # self.__counter_label.pack(side=LEFT, fill=BOTH, expand=True)
        # self.__less_button.pack(side=LEFT, fill=BOTH, expand=True)

        self.__more_button.grid(row=0, column=0, sticky = W + E)
        self.__counter_label.grid(row=0, column=1, sticky = W + E)
        self.__less_button.grid(row=0, column=2, sticky = W + E)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)

    def __add(self):
        self.__counter += 1
        self.__set_counter()

    def __less(self):
        self.__counter -= 1
        self.__set_counter()

    def __set_counter(self):
        counter = str(self.__counter)
        self.__counter_label.config(text=counter)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()