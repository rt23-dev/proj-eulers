# 1000 digit fibonacci number
import math

def fib():
    a, b = 1, 1
    i = 2

    while True:
        a, b = b, a+b
        i += 1
        if math.log10(b) >= 999:
            return i
print(fib())