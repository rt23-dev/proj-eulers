# integer right triangles

#a^2 + b^2 = c^2
#a + b + c = p

def count_solutions(p):
    count = 0
    for a in range(1, p // 3):  # a must be less than p/3
        for b in range(a, (p - a) // 2):  # b < c → b < (p - a)/2
            c = p - a - b
            if a * a + b * b == c * c:
                count += 1
    return count

max_count = 0
max_p = 0
for p in range(598, 1000):
    count = count_solutions(p)
    if count > max_count:
        max_count = count
        max_p = p

print(max_p)
