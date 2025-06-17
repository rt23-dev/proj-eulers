# permuted multiples

def find_digits(n):
    digits = []
    for dig in str(n):
        digits.append(dig)
        digits.sort()
    return digits

i = 1
while not (find_digits(i) == find_digits(2*i) == find_digits(3*i) == find_digits(4*i) == find_digits(5*i) == find_digits(6*i)):
    i += 1

print(i)

        
