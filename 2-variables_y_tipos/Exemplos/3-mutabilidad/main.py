numbers = [2, 4, 5, 1, 3]

sorted_numbers = list(reversed(numbers))
print('Numbers', numbers)
print('Sorted_numbers', sorted_numbers)
print('Numbers == Sorted_numbers', sorted_numbers == numbers)
print('Numbers is Sorted_numbers', sorted_numbers is numbers)

print('---' * 5)
numbers.reverse()
print('Numbers', numbers)
print('Sorted_numbers', sorted_numbers)
print('Numbers == Sorted_numbers', sorted_numbers == numbers)
print('Numbers is Sorted_numbers', sorted_numbers is numbers)
