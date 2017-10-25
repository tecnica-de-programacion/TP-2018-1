from tkinter import Tk, Label, Entry, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "Cambio de Moneda"
        heigth = 100
        width = 550
        input_width = 250
        separator_width = 50
        center = N + S + E + W
        left = W
        event = "<Button-1>"

        convert_text = "Convertir"
        separator_text = "▶"

    def __init__(self, convert_handler = None):
        super().__init__()
        self.__convert_handler = convert_handler
        self.title(self.Constants.title)
        self.maxsize(width = self.Constants.width, height = self.Constants.heigth)
        self.minsize(width = self.Constants.width, height = self.Constants.heigth)
        self.__configure_grid()
        self.__configure_UI()

    def __configure_UI(self):
        currency_name_label = Label(self)
        currency_name_label.grid(row=0, column=0, sticky=self.Constants.left)
        currency_name_label.configure(text="USD")
        vcmd = (self.register(self._checkNumberOnly), '%d', '%P')
        self.__currency_input = Entry(self, validate='key', validatecommand=vcmd)
        self.__currency_input.grid(row=1, column=0, sticky = self.Constants.center)

        result_name_label = Label(self)
        result_name_label.grid(row=0, column=2, sticky=self.Constants.left)
        result_name_label.configure(text="MXN")
        self.__result_label = Label(self)
        self.__result_label.grid(row=1, column=2, sticky=self.Constants.left)
        self.__result_label.configure(text="0")

        separator_lable = Label(self)
        separator_lable.configure(text = self.Constants.separator_text)
        separator_lable.grid(row=1, column=1, sticky=self.Constants.center)

        self.__action_button = Label(self)
        self.__action_button.grid(row=2, column=2, sticky=self.Constants.center)
        self.__action_button.configure(text = self.Constants.convert_text)
        self.__action_button.bind(self.Constants.event, self.__did_tap_convert)

    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=True)
        self.grid_rowconfigure(1, weight=True)
        self.grid_rowconfigure(2, weight=True)
        self.grid_columnconfigure(0, minsize = self.Constants.input_width)
        self.grid_columnconfigure(2, minsize = self.Constants.input_width)
        self.grid_columnconfigure(1, minsize = self.Constants.separator_width)

    def _checkNumberOnly(self, action, value_if_allowed):
        if action != '1':
            return True
        try:
            value = float(value_if_allowed)
            return True
        except ValueError:
            return False

    def __did_tap_convert(self, event):
        if self.__convert_handler is None:
            return
        if self.__currency_input.get() != "":
            amount_to_convert = float(self.__currency_input.get())
            self.__convert_handler("USD", "MXN", amount_to_convert)

    def update_result(self, text):
        self.__result_label.configure(text = text)



