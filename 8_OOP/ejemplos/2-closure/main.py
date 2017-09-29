def multiplication_maker(x):
    def operation(y):
        return y * x
    return operation

m_by_5 = multiplication_maker(5)
m_by_3 = multiplication_maker(3)

print(m_by_5)
print(m_by_3)
print(m_by_5(2))
print(m_by_3(2))
help(multiplication_maker)
help(m_by_5)
help(operaion)

################################################

def greeting_factory (greeting):
    def greeting_action (person):
        return greeting + " " + person
    return {
        "greeting": greeting,
        "action": greeting_action
    }

greeting_es = greeting_factory("Hola")
print(greeting_es["greeting"])
print(greeting_es["action"]("miguel"))