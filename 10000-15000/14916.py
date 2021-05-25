import sys
input = sys.stdin.readline

n = int(input())
dp = [1000001]*(n+1)
dp[0] = 0

coins = (2,5)

for coin in coins:
    for i in range(coin, n+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[n] if dp[n] != 1000001 else -1)


"""
동전의 최소 개수

dp[i] : i원일 때 최소 개수

dp[i] = min(dp[i], dp[i-coin]+1)
"""