# A palindromic number reads the same both ways. The largest palindrome made from the product of two 
# 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def check_palindrome(n):
    reverse = 0 
    temp = n
    while (temp != 0):
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10
    return reverse == n

def prob_4():
    upper_bound = 999*999
    i, j = 999, 999
    while i > 900 and upper_bound >= i*j:
        j = 999
        while j > 900:
            if check_palindrome(i*j):
                return  i*j
            j = j - 1
        i -= 1

print(prob_4())