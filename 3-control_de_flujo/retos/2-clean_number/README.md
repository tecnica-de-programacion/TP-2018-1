Reto 2: Clean Number
======

Completa a función clean_number, la cual que recibe un string 'value' que representaun número con nomenclatura humana y retornar el número como un typo computable.

En caso de que se detecten caracteres no computables regresar: None

Ejemplo:
=====

```
Entrada: ‘3 056, 450’
Salida: 3056450 #Int
```
```
Entrada: ’17.50’
Salida: 17.50 #Float
```
```
Entrada: ’numero 17.50’
Salida: None
```
```
Entrada: ’20,400.50’
Salida: 20400.50 #Float
```
```
Entrada: ’20,400.50,00’
Salida: None
```