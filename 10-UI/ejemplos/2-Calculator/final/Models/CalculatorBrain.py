from Helpers.CustomeTypes import Operation, Number, UnaryOperator, BinaryOperator

class CalculatorBrain:

    def __init__(self, update_hadler = None):
        self.__result = 0
        self.__display = str(self.__result)
        self.__pendig_operation = None
        self.__is_operation_pending = False
        self.__update_hadler = update_hadler

    @property
    def result(self):
        return self.__result

    @property
    def display(self):
        return self.__display

    def type_number(self, number):
        self.__display = number.value if self.__display == Number.ZERO.value else self.__display + number.value
        self.__result = float(self.__display) if "." in self.__display  else int(self.__display)
        self.__update()

    def add_dot(self):
        if UnaryOperator.DOT.value in self.__display:
            return
        self.__display += UnaryOperator.DOT.value
        self.__result = float(self.__display)
        self.__update()

    def perform_unary(self, operator):
        operation = self.__get_operation(operator, None)
        if operation is None: return
        self.__result = operation(self.__result)
        self.__display = str(self.__result)
        self.__update()

    def pending_operation(self, operator):
        self.__pendig_operation = self.__get_operation(operator, self.__result)
        self.__is_operation_pending = True

    def safe_perform_pending_operation(self):
        if not self.__is_operation_pending: return
        self.perform_pending_operation()

    def perform_pending_operation(self):
        if self.__pendig_operation is None: return
        operation = self.__pendig_operation
        self.__result = operation(self.__result)
        self.__display = str(self.__result)
        self.__is_operation_pending = False
        self.__update()

    def __update(self):
        if self.__update_hadler is None:
            return
        self.__update_hadler()

    def __get_operation(self, operator, value):
        operations = {
            UnaryOperator.AC.value: self.clean,
            UnaryOperator.CHANGE.value: lambda x: -x,
            UnaryOperator.PORCENTAGE.value: lambda x: x / 100,
            BinaryOperator.MULTIPLAY.value: lambda x, y = value: y * x,
            BinaryOperator.DIVISOR.value: lambda x, y = value: y / x,
            BinaryOperator.PLUSS.value: lambda x, y = value: y + x,
            BinaryOperator.LESS.value: lambda x, y = value: y - x
        }
        return operations.get(operator.value, None)

    def clean(self, data):
        self.__result = 0
        self.__display = str(self.__result)
        self.__pendig_operation = None
        return 0

    def clean_display(self):
        self.__result = 0
        self.__display = str(self.__result)
