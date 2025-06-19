# summation of primes

# O(sqrt(N))

from math import sqrt

def prime_check(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

def sum_of_primes(l, p):
    sum = 0
    for i in range(p, (1-l), -1):
        isPrime = prime_check(i)
        if isPrime:
            sum += i
    return sum

print(sum_of_primes(1, 2000000))