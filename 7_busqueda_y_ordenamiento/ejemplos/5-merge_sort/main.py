items = [64, 25, 12, 22, 11]

def merge(left, right):
    left_size = len(left)
    right_size = len(right)
    if not left_size or not right_size:
        return left or right
    
    result = []
    i, j = 0, 0
    while (len(result) < left_size + right_size):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == left_size or j == right_size:
            result.extend(left[i:] or right[j:])
            break 
    return result

def merge_sort(numbers):
    if len(numbers) < 2:
        return numbers
    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])
    return merge(left, right)

print(items)
print(merge_sort(items))
