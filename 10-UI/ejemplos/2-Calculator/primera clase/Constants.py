class Constants:

    class Main:
        title = "Calculator"
        heigth = 475
        width = 300

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)