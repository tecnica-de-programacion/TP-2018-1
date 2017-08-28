def factorial(num):
    if num <= 1:
        return 1
    next_factorial = factorial(num - 1)
    return num * next_factorial

print(factorial(5))
