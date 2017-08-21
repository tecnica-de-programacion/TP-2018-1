
greeting = 'Hola como'
second_greeting = greeting
print('Greeting', greeting)
print('Second greeting', second_greeting)
second_greeting += ' estas'
print('Greeting', greeting)
print('Second greeting', second_greeting)

animals = ['dog', 'cat', 'mouse', 'monkey']
second_animals = animals
print('Animals', greeting)
print('Second animals', second_animals)
animals.append('lion')

print('Animals', greeting)
print('Second animals', second_animals)

print('---' * 10)
animals = ['dog', 'cat', 'mouse', 'monkey']
copy_value = animals.copy()
copy_reference = animals.copy()
print('Animals', animals)
print('Copy Value', copy_value)
print('Copy Reference', copy_reference )
print('Animals == Copy Value', animals == copy_value)
print('Animals is Copy Value', animals is cocopy_valuepy)
print('Animals == Copy Reference', animals == copy)
print('Animals is Copy Reference', animals is copy)

print('---' * 10)
animals.append('lion')
print('Animals', animals)
print('Copy', copy)
print('Animals == Copy', animals == copy)
print('Animals is Copy', animals is copy)
