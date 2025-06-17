# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# factors of 2520: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10...  primes: 1, 2, 3, 5, 7 product of primes = 210, 
# then account for all powers of numbers

def find_factors(n):
    multiples = []
    i = 1
    while i < (n+1):
        if n%i  == 0:
            multiples.append(i)
        i += 1
    return multiples

def even_div(a):
    ans = 1
    factors = []
    for i in range(a):
        if len(find_factors(i)) == 2:
            ans *= i
            factors.append(i)
    for factor in factors:
        n = 2
        while factor**n < a:
            print(factor, "^", n)
            ans *= factor
            n += 1
    return ans
    
print(even_div(20))


        
        



