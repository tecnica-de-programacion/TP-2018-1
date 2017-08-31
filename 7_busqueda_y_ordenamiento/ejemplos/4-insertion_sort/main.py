items = [64, 25, 12, 22, 11]
 
def insertion_sort(numbers):
    result = numbers.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and key < result[j] :
                result[j+1] = result[j]
                j -= 1
        result[j + 1] = key
    return result

print(items)
print(insertion_sort(items))