import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0]*(N+1) for _ in range(K+1)]
dp[0][0] = 1

for i in range(1,K+1):
    for j in range(N+1):
        for t in range(j+1):
            dp[i][j] += dp[i-1][j-t]
            dp[i][j] %= 1000000000

print(dp[K][N])
        

"""
dp[k][i] : 갯수가 k일 때 합이 i가 되는 경우의 수
dp[k][i] += dp[k-1][i-t] 
"""