import sys
input = sys.stdin.readline

n,k = map(int, input().split())
dp = [10001]*(k+1)
dp[0] = 0

for _ in range(1,n+1):
    coin = int(input())
    for i in range(coin,k+1):
        dp[i] = min(dp[i-coin]+1, dp[i])

print(dp[i] if dp[i]!=10001 else -1)

"""
# 동전 2

dp[i] : 합이 i가 되는 최소 동전 개수
dp[i] = dp[i-동전들]+1
"""