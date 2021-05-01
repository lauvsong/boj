import sys
input = sys.stdin.readline

t = int(input())
n = tuple(int(input()) for _ in range(t))

MAX = max(n)
dp = [1]*(MAX+1)

for i in range(2,MAX+1):
    dp[i] += dp[i-2]

for i in range(3,MAX+1):
    dp[i] += dp[i-3]

for v in n:
    print(dp[v])