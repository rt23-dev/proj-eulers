# number spiral diagonals

top_right = 0
top_left = 0
bottom_right = 0
bottom_left = 0
for i in range(3, 1002, 2):
    top_right += i**2
    top_left += i**2 - i+1
    bottom_right += i**2 - 2*(i-1)
    bottom_left += i**2 - 3*(i-1)

total = 1 + top_right + bottom_left + top_left + bottom_right
print(total)