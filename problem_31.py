# Coin sums

denominations = [1, 2, 5, 10, 20, 50, 100, 200]
sum = 200

def count(coins, sum):
    n = len(coins)
    dp = [0]*(sum+1)
    dp[0] = 1
    for i in range(n):
        for j in range(coins[i], sum+1):
            dp[j] += dp[j - coins[i]]
    return dp[sum]

print(count(denominations, sum))
