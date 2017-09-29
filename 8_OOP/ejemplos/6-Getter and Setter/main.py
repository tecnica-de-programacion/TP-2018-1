class Employe():
    """This is a representation for a Employe"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = "{} {}".format(first_name, last_name)


emp_1 = Employe("Lalo", "Landa")
print(emp_1.full_name)

emp_1.first_name = "Eduardo"
print(emp_1.full_name)

#########################################################

class Employe():
    """This is a representation for a Employe"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


emp_1 = Employe("Lalo", "Landa")
print(emp_1.full_name())

emp_1.first_name = "Eduardo"
print(emp_1.full_name())

#########################################################

class Employe():
    """This is a representation for a Employe"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


emp_1 = Employe("Lalo", "Landa")
print(emp_1.full_name)

emp_1.first_name = "Eduardo"
print(emp_1.full_name)

######################################################################

class Employe():
    """This is a representation for a Employe"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


emp_1 = Employe("Lalo", "Landa")
print(emp_1.full_name)

emp_1.first_name = "Eduardo"
print(emp_1.full_name)

emp_1.full_name = "Lalo Landa"

###########################################################################

class Employe():
    """This is a representation for a Employe"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, full_name):
        first, last = full_name.split(" ")
        self.first_name = first
        self.last_name = last


emp_1 = Employe("Lalo", "Landa")
print(emp_1.full_name)

emp_1.first_name = "Eduardo"
print(emp_1.full_name)

emp_1.full_name = "Lalo Landa"
print(emp_1.first_name)
print(emp_1.full_name)