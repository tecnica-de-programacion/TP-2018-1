# Crean una función que reciba una lista de números, y regrese un arreglo que no contenga elementos repetidos

## Entrada: [3, 57, 24, -37, 3, 17, 5, 5, 57]
## Salida: [3, 57, 24, -37, 17, 5]

## Entrada: [5, 5, 5, 5, 5, 5]
## Salida: [5]

def clean_duplicates(num_list):
    clean_list = []
    for num in num_list:
        if num not in clean_list:
            clean_list.append(num)
    return clean_list
