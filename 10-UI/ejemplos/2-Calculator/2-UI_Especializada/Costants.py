class Costants:

    class Main:
        heigth = 475
        width = 300
        button_size = 75
        result_size = 100

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    class Keyboard:   
        matrix_heigth = 5
        matrix = [ 
            ["AC", "+/-", "%", "/"],
            ["1", "2", "3", "x"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", None, ".", "="]
        ]

    class Colors:
        color = '#40E0D0'

    class Events:
        rigthClick = '<Button-1>'