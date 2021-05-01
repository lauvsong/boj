import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = []
    dp.append([0]+list(map(int, input().split())))
    dp.append([0]+list(map(int, input().split())))

    for i in range(2, n+1):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][-1], dp[1][-1]))

"""
# 점화식
dp[1][j] += max(dp[0][j-1], dp[0][j-2])
"""