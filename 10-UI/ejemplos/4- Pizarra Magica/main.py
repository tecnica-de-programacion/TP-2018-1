from Views.MainView import MainView

class MainApp():

    def __init__(self):
        self.__master = MainView(start_handler = self.press, motion_handler = self.motion, space_handler = self.clean)
        self.x = None
        self.y = None
        self.last_x = None
        self.last_y = None

    def run(self):
        self.__master.mainloop()

    def motion(self, event):
        self.x = event.x
        self.y = event.y
        self.__master.draw_line(self.x, self.y, self.last_x, self.last_y)
        self.last_x = self.x
        self.last_y = self.y

    def press(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def clean(self):
        self.__master.clean()

if __name__ == "__main__":
    app = MainApp()
    app.run()