# name = None
# if name != None:
#     print('Existe')
# else:
#     print('No existe')

name = input("What is your name? : ")
age = int(input("Hi {}, How old are you?: ".format(name)))
print("Your age is: {}".format(age))

if age >= 18:
    print("Eres mayor de edad en Mexico")
    if age >= 21:
        print("Y tambien el el mundo")
    else:
        print("pero en otros paises aun eres menor de edad")
elif age > 15:
    print("Eres menor de edad, no puedes votar")
elif age == 15:
    print("Cuando son tus 15")
else:
    mensaje = "Eres menor de edad y puberto" if (5 >= age >= 0) else "Eres un bebe :3"
    print("{}".format(mensaje))
