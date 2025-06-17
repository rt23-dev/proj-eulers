# Digit fifth powers

valid = []
num = 100
while num < 1000000: # arbitary big number
    tot = 0
    for digit in str(num):
        tot += int(digit)**5
    if tot == num:
        valid.append(num)
    num += 1

print(sum(valid))
