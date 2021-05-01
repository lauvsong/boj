import sys
input = sys.stdin.readline

N = int(input())
dp = [[0]*10 for _ in range(N+1)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2,N+1):
    for j in range(10):
        if j == 0: 
            dp[i][j] = dp[i-1][j+1]
        elif j == 9: 
            dp[i][j] = dp[i-1][j-1]
        else: 
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

print(sum(dp[N]) % 1000000000)

"""
dp[i][j]
i : 몇개까지 탐색
j : 현재 숫자

# 점화식
dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

0일 경우 : dp[i-1][j+1]
9일 경우 : dp[i-1][j-1]
"""