items = [64, 25, 12, 22, 11]
 
def section_sort(numbers): 
    sorted_numbers = numbers.copy()
    for i in range(len(sorted_numbers)):
        min_index = i
        for j in range(i + 1, len(sorted_numbers)):
            if sorted_numbers[min_index] > sorted_numbers[j]:
                min_index = j
        sorted_numbers[i], sorted_numbers[min_index] = sorted_numbers[min_index], sorted_numbers[i]
    return sorted_numbers

print(section_sort(items))
print(items)

 