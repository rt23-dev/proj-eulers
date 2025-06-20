# Digit Cancelling Fractions

for n in range(10, 100):
    for d in range(n+1, 100):
        if str(n)[1] == str(d)[0] and int(str(d)[1]) != 0:
            if n/d == int(str(n)[0])/int(str(d)[1]):
                print(n,d)
        if str(n)[0] == str(d)[1]:
            if n/d == int(str(n)[1])/int(str(d)[0]):
                print(n,d)

# Above code only gives numerators and denominators. Other computations done outside.

print(16*19*26*49)
print(64*95*65*98)