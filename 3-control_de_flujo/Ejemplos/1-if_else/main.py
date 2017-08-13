# name = None
# if name != None:
#     print('Existe')
# else:
#     print('No existe')

name = input('Whats your name?: ')
age = int(input('Hi {}, How old are you?: '.format(name)))
print('Hi {}, your age is {}'.format(name, age))

if age >= 18:
    print('You are legal in México')
    if age >= 21:
        print('And you are legal in the rest of the world')
    else:
        print('But underage in the rest of the world')
    elif age > 15:
        print("You are not legal in Mexíco, you can't vote")
    elif age == 15:
        print('You are a teenager')
    else:
        print('You are a kid' if (5 < age) else 'Is a Babyyy :3')
