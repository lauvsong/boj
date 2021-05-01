import sys
input = sys.stdin.readline

N = int(input())
dp = [0,1,1]
for i in range(3,N+1):
    dp.append(sum(dp[-2:]))

print(dp[-1])

"""
dp[i] : i번째 자리 이친수 개수

# 점화식
dp[i] = dp[i-1] + dp[i-2]
"""