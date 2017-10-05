from tkinter import Tk, PhotoImage, Label, LEFT, W, E, S, N
from Costants import Costants

class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry(Costants.Main.size())
        self.button_matrix = []
        self.configure_ui()
    
    def configure_ui(self):
        self.__result_lable = Label(self, text="0", bg = Costants.Colors.color, borderwidth=1, relief="solid")
        self.__result_lable.grid(column = 0, columnspan = 4 , sticky = W + E + N + S)

        for index_row, row in enumerate(Costants.Keyboard.matrix):
            for index_colum, colum in enumerate(row):
                if not colum:
                    continue
                b = Label(self, text=colum)
                b.configure(bg = Costants.Colors.color, borderwidth=1, relief="solid")

                # def handler(event,  b = b):
                #     return self.__cbHandler(event, b)

                b.bind(Costants.Events.rigthClick, lambda event, b = b: self.__cbHandler(event, b))
                b.id = colum
                span = 1 if colum != "0" else 2
                b.grid(row=index_row + 1, column=index_colum, columnspan = span, sticky = W + E + N + S)
        
        self.grid_rowconfigure(0, minsize = Costants.Main.result_size)
        for index in range(Costants.Keyboard.matrix_heigth):
            self.grid_rowconfigure(index + 1, minsize = Costants.Main.button_size)
            self.grid_columnconfigure(index, minsize = Costants.Main.button_size)
            
    def __cbHandler(self, event, eventEmiter):
        print(eventEmiter.id)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()