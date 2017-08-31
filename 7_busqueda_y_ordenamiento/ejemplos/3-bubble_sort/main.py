items = [64, 25, 12, 22, 11]
 
def bubble_sort(numbers):
    result = numbers.copy()
    size = len(numbers)

    for i in range(size):
        for j in range(0, size - i - 1):
            if result[j] > result[j + 1] :
                result[j], result[j + 1] = result[j + 1], result[j]
    return result
  
print(items)
print(bubble_sort(items))
