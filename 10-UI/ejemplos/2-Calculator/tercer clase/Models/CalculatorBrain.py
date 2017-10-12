from Helpers.CustomTypes import BinaryOperator, UnaryOperator

class CalculatorBrain:

    def __init__(self, update_handler = None):
        self.__result = 0
        self.__pending_operation = None
        self.__update_handler = update_handler

    @property
    def result(self):
        return self.__result
    
    def clean(self):
        self.__pending_operation = None
        return 0

    def __update(self):
        if self.__update_handler is None:
            return
        self.__update_handler()

    def pending_operation(self, operator, value):
        self.__pending_operation = self.__get_operation(operator, value)
    
    def perform_pending_operation(self):
        if self.__pending_operation is None:
            return

        self.__result = self.__pending_operation(self.__result)
        self.__update()

    def __get_operation(self, operator, value):
        operations = {
            UnaryOperator.AC.value: self.clean,
            UnaryOperator.CHANGE.value: lambda x: -x,
            UnaryOperator.PORCENTAGE.value: lambda x: x / 100,
            BinaryOperator.MULTIPLAY.value: lambda x, y=value: y * x,
            BinaryOperator.DIVISOR.value: lambda x, y=value: y / x,
            BinaryOperator.PLUSS.value: lambda x, y=value: y + x,
            BinaryOperator.LESS.value: lambda x, y=value: y - x
        }
        return operations.get(operator.value, None)
