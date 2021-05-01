import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [nums[:], nums[:]]

for i in range(1,n):
    dp[1][i] = max(dp[1][i-1] + nums[i], nums[i])
    dp[0][i] = max(dp[1][i-1], dp[0][i-1]+nums[i])

print(max(dp[0]+dp[1]))


"""
# 케이스
1. 제거
2. 제거 x
- 현재 값을 제거한 경우
- 이전에 제거한 경우 중 최댓값

dp[1][i]: i번째를 마지막으로 선택했을 때 가장 큰 합 (제거 안한 경우)
dp[0][i]: i번째를 마지막으로 선택했을 때 가장 큰 합 (제거 한 경우)

dp[i] = dp[i-1] + nums[i]
"""