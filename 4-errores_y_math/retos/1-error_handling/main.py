import random

def guess_number (n) :
    user_answer = n
    
    while user_answer != answer:
        user_input = input("Adivina el numero: ")
        user_answer = int(user_input)
        dif = abs(user_answer - answer)
        try:
            user_answer = int(user_input)
            dif = abs(user_answer - answer)
        except ValueError:
            print("No es un numero")
            continue
        if dif < 5:
            print("Caliente")
        elif dif < 20:
            print("Tibio")
        elif dif < 50:
            print("Frio")
        else:
            print("Muy Frio")
    else:
        print("Correcto: El numero es {}".format(answer))



