i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("Termina Loop")

i = 0
while i < 10:
    if i == 9:
        print("Game Over")
        continue
    # if i == 3:
    #     break
    print("i is now {}".format(i))
    i += 1
else:
    print("Termina Loop")
