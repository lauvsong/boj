import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)

for i in range(1,N+1):
    dp[i] = i
    for j in range(1,i):
        if j**2 > i: break
        dp[i] = min(dp[i-j**2]+1, dp[i])

print(dp[N])

"""
dp[i] : i 의 최소 제곱수 항 개수
dp[i] = dp[i-j**2] + 1

"""