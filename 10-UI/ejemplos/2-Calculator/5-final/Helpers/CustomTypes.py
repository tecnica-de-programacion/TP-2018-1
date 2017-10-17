from enum import Enum

class Number(Enum):
    ZERO = "0"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"

class BinaryOperator(Enum):
    MULTIPLAY = "×"
    DIVISOR = "÷"
    PLUSS = "+"
    LESS = "-"

class UnaryOperator(Enum):
    AC = "AC"
    PORCENTAGE = "%"
    CHANGE = "±"
    EQUAL = "="
    DOT = "."