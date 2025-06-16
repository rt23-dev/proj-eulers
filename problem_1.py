# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

def prob_1(n):
    i = 0
    valid = []
    while i < n:
        if i % 3 == 0 or i % 5 == 0:
            valid.append(i)
        i += 1

    ans = sum(valid)
    return ans

print(prob_1(1000))

