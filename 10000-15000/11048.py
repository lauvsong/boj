import sys
input = sys.stdin.readline

N,M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N+1)]
for r in range(1,N+1):
    for c in range(1,M+1):
        dp[r][c] = max(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + grid[r-1][c-1]

print(dp[N][M])


"""
dp[r][c] = max(dp[r-1][c], dp[r][c-1], dp[r-1,c-1]) + dp[r][c]
"""