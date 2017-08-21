def diamond(n):
    if (n <= 0) or (n % 2 == 0):
        return None

    diamond = get_flor(n, n)
    items_in_flor = n - 2

    while items_in_flor > 0 :
        new_flor = get_flor(n, items_in_flor)
        diamond = new_flor + diamond + new_flor
        items_in_flor -= 2

    return diamond

def get_flor(max_elements, num_in_flor):
    spaces = ((max_elements - num_in_flor) // 2) * ' '
    return spaces + (num_in_flor * '*') + '\n'
