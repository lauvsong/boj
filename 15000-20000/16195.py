import sys
input = sys.stdin.readline

MOD = 1000000009
MAX = 1001

dp = [[0]*(MAX) for _ in range(MAX)]
dp[1][1] = 1
dp[2][1], dp[2][2] = 1,1
dp[3][1], dp[3][2], dp[3][3] = 1,2,1

for i in range(4,MAX):
    for j in range(1,i+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % MOD

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    print(sum(dp[n][:m+1]) % MOD)