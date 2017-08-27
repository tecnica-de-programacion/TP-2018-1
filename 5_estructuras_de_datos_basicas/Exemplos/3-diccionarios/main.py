person = {
    'first_name': 'miguel',
        'age': 24,
            'is_alive': True
}

print(person)
print(person['first_name'])
print(person['age'])
print(person['is_alive'])


person['gender'] = 'male'
print(person)

del person['gender']
# del person
print(person)

# person.clear()
# print(person['firstn_name'])

if 'first_name' in person:
    print(person['first_name'])
else:
    print('No existe', 'first_name')

print(person.get('firstn_name', None))

person2 = {
    'firstn_name': 'miguel',
        'firstn_name': 'marco',
}

print(person2)

greetings = {
    'es': 'Hola',
    'in': 'Hello',
    'fr': 'Salut',
    'it': 'Ciao',
    'gr': 'Hallo'
}

greetings2 = {
    'jp': 'shin chi ca'
}

for greet in greetings:
    print(greet, '_', greetings[greet])

print('---' * 10)

keys = list(greetings.keys())
for key in keys:
    print(key,'_',greetings[key])

print('---' * 10)
for items in greetings.items():
    print(items)
        print(items[0], items[1])

print('---' * 10)
for keys, values in greetings.items():
    print(keys, values)

print('---' * 10)
print(greetings.update(greetings2))
print(greetings)

print(greetings2.update(greetings))
print(greetings2)
