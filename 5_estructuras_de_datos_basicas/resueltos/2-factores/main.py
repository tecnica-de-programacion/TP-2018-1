def factors_range(n, m):
    result = {}
    for num in range(n, m + 1):
        result[num] = get_factors(num)
    return result


def get_factors(n):
    factors = []
    step = 1 if (n % 2 == 0) else 2
    possible_factors = range(step + 1, (n//2) + 1, step)

    for num in possible_factors:
        if n % num == 0:
            factors.append(num)
    return factors if len(factors) > 0 else None
