import sys
input = sys.stdin.readline

n = int(input())
t,p = [], []
for _ in range(n):
    time, price = map(int, input().split())
    t.append(time)
    p.append(price)

dp = [0]*(n+1)
for i in range(n):
    if (k := i+t[i]) <= n:
        dp[k] = max(dp[k], dp[i]+p[i])
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[n])
"""
dp[i+t[i]] = max(dp[i+t[i]], dp[i] + p[i])
"""