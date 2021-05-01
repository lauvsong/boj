# 퇴사 2
import sys
input = sys.stdin.readline

t = []
p = []
n = int(input())
for _ in range(n):
    time, price = map(int, input().split())
    t.append(time)
    p.append(price)

dp = [0]*(n+1)
for i in range(n):
    if (k := i+t[i]) < n+1:
        dp[k] = max(dp[i]+p[i], dp[k])
    dp[i+1] = max(dp[i], dp[i+1])

print(dp[n])

"""
dp[i] = i일에 얻을 수 있는 최대 수익

# 점화식
dp[i+T[i]] = max(dp[i]+P[i], dp[i+T[i]])
"""