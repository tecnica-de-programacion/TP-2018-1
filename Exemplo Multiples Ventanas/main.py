from Views.ViewContainer import ViewContainer
from Views.StartView import StartView
from Views.ViewOne import ViewOne
from Views.ViewTwo import ViewTwo
from CostomeType.View import View

class MainApp():

    def __init__(self):
        self.__master = ViewContainer()

        start = StartView(self.__master.container, change_view_hadler=self.__did_change_view)
        one = ViewOne(self.__master.container, change_view_hadler=self.__did_change_view)
        two = ViewTwo(self.__master.container, change_view_hadler=self.__did_change_view)

        self.__frames = {
            View.Start: start,
            View.One: one,
            View.Two: two
        }

        self.__master.set_views(self.__frames.values())
        self.__did_change_view(View.Start)

    def run(self):
        self.__master.mainloop()

    def __did_change_view(self, view):
        frame = self.__frames[view]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.run()