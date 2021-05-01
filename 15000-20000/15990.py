import sys
input = sys.stdin.readline

t = int(input())
n = [int(input()) for _ in range(t)]

MAX = max(n)
MOD = 1000000009

dp = [[0]*4 for _ in range(MAX + 1)]
dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]

for i in range(4, MAX + 1):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD

for v in n:
    print(sum(dp[v]) % MOD)