def guess_number (answer) :
    user_answer = 0
    while user_answer != answer:
        user_input = input("Adivina el numero: ")
        user_answer = int(user_input)
        dif = abs(user_answer - answer)
        if dif == 0:
            continue
        elif dif < 5:
            print("Caliente")
        elif dif < 20:
            print("Tibio")
        elif dif < 50:
            print("Frio")
        else:
            print("Muy Frio")
    print("Correcto: El numero es {}".format(answer))

guess_number(20)
