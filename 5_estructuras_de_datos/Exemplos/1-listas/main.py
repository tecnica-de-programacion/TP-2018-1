odd = list(range(0,8,2))
even = [1,3,5,7,9]
mix = ['2', 2, 'hola', 4, True]

print('Odds:', odd)
print('Evens:', even)
print('Mix:', mix)

print('---'*10)
print('Print All', odd)
for num in odd:
    print('-', num)

print('---'*10)
print('Print All Numerated', odd)
for index, num in enumerate(odd):
    print('- {}: {}'.format(index, num))

print('---'*10)
mix[3] = 32
print('Edit', mix)

print('---'*10)
odd.append(8)
print('Pares + 8:', odd)

print('---'*10)
mix.extend(odd)
print('Extend', mix)

print('---'*10)
mix.insert(4, False)
print('Insert False in 4:', mix)

print('---'*10)
mix.remove(False)
print('Remove False:', mix)
mix.remove(2)
print('Remove 2:', mix)
del mix[3]
print('Remove True:', mix)

print('---'*10)
print('Index of 8:', odd.index(8))
#print('Index of 1:', odd.index(1))

print('---'*10)
print('In 8:', 8 in odd)
print('In 1:', 1 in odd)

print('---'*10)
print('Concat', even + odd)
print('Concat', odd + even)

print('---'*10)
print([1,2] * 3)

print('---'*10)
print('Count', mix.count('hola'))
print('Count', mix.count(10))

print('---'*10)
print('Length', len(odd))
print('Max', max(odd))
print('Min',min(odd))
#print(max(mix)) # Error, no corresponden al mismo tipo

print('---'*10)
reverse = list(reversed(odd))
odd.reverse()
print('Reversed', reverse)
print('Odd', odd)
print('Odd == Reversed', odd == reverse)
print('Odd is Reversed', odd is reverse)


print('---'*10)
numbers = [2, 4, 5, 1, 3]

sorted_numbers = sorted(numbers)
print('Numbers', numbers)
print('Sorted_numbers', sorted_numbers)
print('Numbers == Sorted_numbers', sorted_numbers == numbers)
print('Numbers is Sorted_numbers', sorted_numbers is numbers)

numbers.sort()
print('Numbers', numbers)
print('Sorted_numbers', sorted_numbers)
print('Numbers == Sorted_numbers', sorted_numbers == numbers)
print('Numbers is Sorted_numbers', sorted_numbers is numbers)

print('---'*10)
copy = odd.copy()
print('Copy', copy)
print('Odd', odd)
print('Odd == Copy', odd == copy)
print('Odd is Copy', odd is copy)
