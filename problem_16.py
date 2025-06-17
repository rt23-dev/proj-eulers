# Power digit sum

def sum_digits(n):
    sum = 0
    num = 2**n
    for dig in str(num):
        sum += int(dig)
    return sum

print(sum_digits(1000))
