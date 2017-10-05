from tkinter import Tk, font
from Costants import Costants
from Views.CalcButton import CalcButton
from Views.ResultLabel import ResultLabel

class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry(Costants.Main.size())
        self.button_matrix = []
        self.configure_ui()
    
    def configure_ui(self):
        self.__result_lable = ResultLabel(self)
        self.__result_lable.position(0, 0)

        for index_row, row in enumerate(Costants.Keyboard.matrix):
            for index_colum, colum in enumerate(row):
                if not colum:
                    continue
                b = CalcButton(self, colum, self.__cbHandler)
                span = 1 if colum != "0" else 2
                b.position(index_row + 1, index_colum, span)
        
        self.grid_rowconfigure(0, minsize = Costants.Main.result_size)
        for index in range(Costants.Keyboard.matrix_heigth):
            self.grid_rowconfigure(index + 1, minsize = Costants.Main.button_size)
            self.grid_columnconfigure(index, minsize = Costants.Main.button_size)
            
    def __cbHandler(self, event, eventEmiter):
        print(eventEmiter.id)

if __name__ == "__main__":
    app = MainWindow()
    print(font.families())
    app.mainloop()