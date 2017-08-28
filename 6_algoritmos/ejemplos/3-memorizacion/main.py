cache = {
    1: 1,
    2: 1
}    
def fibonacci_memoize(n):
    if n not in cache.keys():
        cache[n] = fibonacci_memoize(n-1) + fibonacci_memoize(n-2)
        return cache[n]
    else:
        return cache[n]

def fibonacci(n) :
    cache = {
        1: 1,
        2: 1
    }    
    
    def fibonacci_memoize(n):
        try:
            return cache[n]
        except Exception:
            cache[n] = fibonacci_memoize(n-1) + fibonacci_memoize(n-2)
            return cache[n]
    
    return fibonacci_memoize(n)