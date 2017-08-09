greeting = "Hola como estas"
print(greeting)

greeting2 = 'Hola como "estas" otra vez'
print(greeting2)

greeting_multiline = """
Hola
como
estas
"""
print(greeting_multiline)

# longitud de string
print(len(greeting))

# existe en
print("Hola" in greeting)
print("hola" in greeting)

# caracteres de string
print(greeting[0])
print(greeting[-1])

# rangos o subStrings
print(greeting[5:9])
print(greeting[:4])
print(greeting[5:])
print(greeting[0::2])

string = 'ejaugnel nu se nohtyP'
print(string[::-1])

# count
string = '9,000.0'
print(string.count('0'))
print(string.count('.'))

# String Interpolations
print("Hola {0}, como estas".format("Miguel"))

print("Hola {0}, {1}".format("Miguel", "¿Como esta tu dia?"))
print("Hola {}, {}".format("Miguel", "¿Como esta tu dia?"))
print("""
Miguel es: {0},
Diana es: {1},
Juan es: {0}
""".format("Hombre","Mujer"))

for i in range(0,9):
    print("Index: {0:2}, two: {1:4}, three: {2:<4} ,".format(i, i*i, i**3))

print("Miguel, tiene %d, %s" % (24, "hola"))

print("Imaginario %12f" % (22/7))
print("Imaginario %.2f" % (22/7))
print("Imaginario %12.5f" % (222/7))

for i in range(0,9):
    print("Index: %d, two: %4d, three: %4d ," % (i, i*i, i**3))

print("hola " + "hola")
print("hola " * 5)
