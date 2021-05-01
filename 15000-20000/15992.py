import sys
input = sys.stdin.readline

MOD = 1000000009
MAX = 1000

dp = [[0]*(MAX+1) for _ in range(MAX+1)]
dp[1][1], dp[2][1], dp[2][2] = 1, 1, 1
dp[3][1], dp[3][2], dp[3][3] = 1, 2, 1

for i in range(4,MAX+1):
    for j in range(1,i+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % MOD

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    print(dp[n][m])


"""
dp[i][j]
i : 정수
j : 사용한 수

dp[i][j] = dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]
조건 : j < m
"""
