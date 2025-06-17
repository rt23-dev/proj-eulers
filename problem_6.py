# Sum Square difference

# need to compute 2*(sum of each number in range(100) multipled by every other number in range(100))

def sum_sq_diff(n):
    ans = 0
    for i in range(n+1):
        for j in range(n+1):
            if i != j:
                ans += (i*j)
    return (ans)

print(sum_sq_diff(100))

