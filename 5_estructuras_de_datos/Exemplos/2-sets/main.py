veg = set(['apio', 'cebolla', 'cebolla', 'verengena', 'apio']) # no usar {} para un set bacio
fruts = {'platano', 'naraja', 'limon', 'pera'}
print('Verduras:', veg)
print('Frutas:', fruts)

veg.add('aguacate')
fruts.add('aguacate')

print('---'*10)
print('Verduras:', veg)
print('Frutas:', fruts)

print('---'*10)
print('Frutas')
for frut in fruts:
  print('-', frut)

print('---'*10)
print('Is "limon" in?')
print('Frutas:', 'limon' in fruts)
print('Vegetales:', 'limon' in veg)


shoping_list = {'platano', 'naraja', 'limon', 'pera'}
print('---'*10)
print('Elementos diferentes:', fruts.isdisjoint(veg))
print('Elementos diferentes:', shoping_list.isdisjoint(veg))

print('---'*10)
print('SubSet:', shoping_list.issubset(fruts))
print('SubSet:', fruts.issubset(shoping_list))
print('SubSet:', fruts <= shoping_list)

print('---'*10)
print('Union', fruts.union(veg))
print('Union', fruts | veg)

print('---'*10)
print('Intersection', fruts.intersection(veg))
print('Intersection', fruts & veg)

print('---'*10)
#print('Difference', fruts.difference(veg))
print('Difference', fruts - veg)
print('Difference', veg - fruts)

print('---'*10)
#print('Symetric Difference', fruts.symmetric_difference(veg))
print('Symetric Difference', fruts ^ veg)

print('---'*10)
frust_copy = fruts.copy()
print('Copy is', frust_copy is fruts)
print('Copy equal', frust_copy == fruts)

print('---'*10)
frust_copy.discard('limon')
frust_copy.discard('limon')
#frust_copy.remove('limon')
#frust_copy.remove('limon')
print('Discar/Remove', frust_copy)

print('---'*10)
print('Pop', frust_copy.pop())

print('---'*10)
frust_copy.clear()
print('Clear', frust_copy)

print('---'*10)
frozen = frozenset([1, 2, 3, 3, 3])
print(frozen) # frozenset({1, 2, 3})

# frozen.add(5) # Error
# frozen.discard(3) # Error
# frozen.remove(3) # Error
