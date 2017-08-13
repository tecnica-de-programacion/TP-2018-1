value = input('Inserta un numero: ')

try:
    int_value = int(value)
    is_int = True
except Exception as e:
    print('Exception:', e)
    is_int = False
else:
    print(5 + int_value)
finally:
    print('Es' if is_int else 'No es', 'un Numero')
