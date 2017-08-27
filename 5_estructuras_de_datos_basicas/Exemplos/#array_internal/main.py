from array import array

a = array('i', [1, 2, 3, 4, 5])
print(a)
print(array.itemsize)

a[0] = 6
a.append(7)

for item in a:
  print(item)
