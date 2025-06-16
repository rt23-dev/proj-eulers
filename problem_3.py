# The prime factors of 13195 are 5, 7, 13, 29.
# What is the largest prime factor of the number 600851475143?

def find_multiples(n):
    multiples = []
    i = 1
    while i < (n+1):
        if n%i  == 0:
            multiples.append(i)
        i += 1
    return multiples

primes = []
for i in find_multiples(600851475143):
    if len(find_multiples(i)) == 2:
        primes.append(i)
        ans = max(primes)

print(ans)