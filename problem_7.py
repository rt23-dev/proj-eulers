# 1001st prime

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

def nth_prime(n):
    primes = []
    a = 2  # start from 2, the first prime
    while len(primes) < n:
        if len(find_factors(a)) == 2:  # primes have exactly 2 factors
            primes.append(a)
        a += 1
    return primes[-1]  # return the last (nth) prime

print(nth_prime(10001))