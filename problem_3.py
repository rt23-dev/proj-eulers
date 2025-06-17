# Largest prime factor

def find_factors(n):
    if n < 2:
        return []
    factors = [1]
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
        i += 1
    factors.append(n)
    return factors

def lpf(n):
    primes = []
    for factor in find_factors(n):
        if len(find_factors(factor)) == 2:
            primes.append(factor)
    return primes[-1]

print(lpf(600851475143))