def fibonacci(n):
    actual_value = 1
    last_value = 1
    for i in range(n - 1):
        before = last_value
        last_value = actual_value + last_value
        actual_value = before
        
        #actual_value, last_value = last_value, actual_value + last_value
    return actual_value
    
def fibonacci_r(n):
 if n == 1 or n == 2:
  return 1
 return fibonacci_r(n - 1) + fibonacci_r(n - 2)
