for i in range(0,10) :
    print(i)

for i in range(0,100,5) :
    print(i)

for i in range(100,0,-5) :
    print(i)

for i in range(0,100,-5) :
    print(i)

for i in range(1,10) :
    for j in range(1, 10):
        print("{0}x{1} = {2}   ".format(i, j, i*j), end='\t')
    print("")

for character in 'Hello, Whats up?' :
    print(character)


shopping_list = ["milk", "sugar", "cream", "chocolate", "fish"]
for item in shopping_list :
    if item == "fish":
        # break
        continue
    print(item)
else:
    print("Loop end")


https://www.youtube.com/watch?v=VBokjWj_cEA



# shopping_list = ["milk", "sugar", "cream", "chocolate"]
not_in_my_coffee = ""
for item in shopping_list:
    if item == "fish":
        not_in_my_coffee = item
print("No '{}' in my coffee".format(not_in_my_coffee))
