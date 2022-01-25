import sys
input = sys.stdin.readline

MOD = 1e9 + 3

n = int(input())
k = int(input())

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][1] = i

for i in range(2, n+1):
    for j in range(2, k+1):
        if i == n:
            dp[i][j] = (dp[i-3][j-1] + dp[i-1][j]) % MOD
        else:
            dp[i][j] = (dp[i-2][j-1] + dp[i-1][j]) % MOD

print(int(dp[n][k]))



"""
# 문제
N개의 색상환에서 서로 다른 K개의 색을 선택하는 경우의 수 (인접한 두색 동시 선택 X)

# 백트래킹?
-> 시간 초과 예상

# 상태
dp[i][j] : i 색상환 까지 j개를 선택했을 때의 경우의 수

dp[i][j] = dp[i-2][j-1] + dp[i-1][j]

dp[i-2][j-1] : 두개 전까지 개수의 색상환에서 j-1개 선택한거
dp[i-1][j] : 바로 이전까지 개수의 색상환에서 j개 선택한거

"""