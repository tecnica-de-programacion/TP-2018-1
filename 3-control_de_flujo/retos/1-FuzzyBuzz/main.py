# No optimizado para cambios
def fuzzy_buzz(value):
    num = int(value) + 1
    result = ''
    for i in range(1, num):
        if i % 15 == 0:
            result += 'FuzzyBuzz'
        elif i % 5 == 0:
            result += 'Buzz'
        elif i % 3 == 0:
            result += 'Fuzzy'
        else:
            result += '{}'.format(i)
        result += ", " if i < (num - 1) else ""
    else:
        return result

# Optimizado para cambios
def fuzzybuzz(n):
    num = int(n) + 1
    result = ''
    for i in range(1, num):
        output = ''
        if i % 3 == 0: output += 'Fuzzy'
        if i % 5 == 0: output += 'Buzz'
        if output == '': output += '{}'.format(i)
        result += output
        result += ', ' if i < (num - 1) else ''
    else:
        return result
