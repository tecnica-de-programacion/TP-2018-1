from Views.CalcButton import CalcButton
from Helpers.CustomTypes import Number, BinaryOperator, UnaryOperator

class KeypadView():
    class Constants:
        heigth = 5
        width = 4
        matrix = [
            [UnaryOperator.AC, UnaryOperator.CHANGE, UnaryOperator.PORCENTAGE, BinaryOperator.DIVISOR],
            [Number.SEVEN, Number.EIGHT, Number.NINE, BinaryOperator.MULTIPLAY],
            [Number.FOUR, Number.FIVE, Number.SIX, BinaryOperator.LESS],
            [Number.ONE, Number.TWO, Number.THREE, BinaryOperator.PLUSS],
            [Number.ZERO, None, UnaryOperator.DOT, UnaryOperator.EQUAL]
        ]

    def __init__(self, master, tap_number_handler = None, tap_operator_handler = None):
        self.__tap_number_handler = tap_number_handler
        self.__tap_operator_handler = tap_operator_handler

        for index_row, row in enumerate(self.Constants.matrix):
            for index_column, key in enumerate(row):
                if not key: continue
                button = CalcButton(master, key, action = self.__did_tap)
                span = 1 if key != Number.ZERO else 2
                button.position(index_row + 1, index_column, columnspan = span)

    def __did_tap(self, sender):
        if self.__tap_number_handler is None or self.__tap_operator_handler is None: return

        if isinstance(sender, Number):
            self.__tap_number_handler(sender)
        else:
            self.__tap_operator_handler(sender)
