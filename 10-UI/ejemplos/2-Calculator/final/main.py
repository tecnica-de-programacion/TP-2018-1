from Views.MainView import MainView
from Models.CalculatorBrain import CalculatorBrain
from Helpers.CustomeTypes import BinaryOperator, UnaryOperator

class MainApp():

    def __init__(self):
        self.__is_typing_number = True
        self.__master = MainView(tap_number_handler = self.__did_number_tapped, tap_operator_handler = self.__operator_tapped)
        self.__brain = CalculatorBrain(update_hadler = self.__update_diaplay)

    def run(self):
        self.__master.mainloop()

    def __did_number_tapped(self, number):
        if self.__is_typing_number:
            self.__brain.type_number(number)
        else:
            self.__brain.clean_display()
            self.__brain.type_number(number)
            self.__is_typing_number = True

    def __operator_tapped(self, operator):

        if UnaryOperator.EQUAL == operator:
            self.__brain.perform_pending_operation()
            self.__is_typing_number = False
        elif UnaryOperator.DOT == operator:
            if self.__is_typing_number:
                self.__brain.add_dot()
            else:
                self.__brain.clean_display()
                self.__brain.add_dot()
                self.__is_typing_number = True
        elif isinstance(operator, UnaryOperator):
            self.__is_typing_number = False
            self.__brain.perform_unary(operator)
        elif isinstance(operator, BinaryOperator):
            self.__is_typing_number = False
            self.__brain.safe_perform_pending_operation()
            self.__brain.pending_operation(operator)

    def __update_diaplay(self):
        self.__master.display(self.__brain.display)

if __name__ == "__main__":
    app = MainApp()
    app.run()