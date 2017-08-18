import random

print('Random 0 a 1', random.random())
print('Random de x a y', random.randint(0, 100))

print('Random dentro de un arreglo', random.choice(['win', 'lose', 'draw']))

deck = 'ace two three four'.split()
print('Andes de Shuffle:', deck)
random.shuffle(deck)                        
print('Despues de Shuffle:', deck)
print('Muestras', random.sample([10, 20, 30, 40, 50], k=4))
