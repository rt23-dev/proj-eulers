# Special Pythogorean Triplet

i = 1
while i < 1000:
    j = i
    while j < 1000:
        k = j
        while k < 1000:
            if i**2 + j**2 == k**2 and i+j+k == 1000:
                print(i, j, k, "Sum:", i+j+k)
                print(i*j*k)
            k += 1
        j += 1
    i += 1