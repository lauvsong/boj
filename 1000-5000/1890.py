import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if (num := grid[i][j]) == 0: break
        if 0 <= i+num < N:
            dp[i+num][j] += dp[i][j]
        if 0 <= j+num < N:
            dp[i][j+num] += dp[i][j]

print(dp[N-1][N-1])
"""
# 점프
dp[r][c] : 여기까지 오는 경로의 개수
dp[r+num][c] += dp[r][c]
dp[r][c+num] += dp[r][c]
"""