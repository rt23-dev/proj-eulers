# Longest Collatz

def collatz(n):
    seq = []
    while n != 1:
        seq.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    seq.append(1)
    return seq

max_len = 0
max_i = 0

for i in range(100000, 1000000):
    current_len = len(collatz(i))
    if current_len > max_len:
        max_len = current_len
        max_i = i

print("Starting number:", max_i)
print("Sequence length:", max_len)
